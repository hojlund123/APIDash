import requests
import json
import os
import logging

# Configure logging to output to standard output
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.StreamHandler()
                    ])

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

config = load_config()
api_urls = config["api_urls"]
timeout = config["timeout"]
retry_attempts = config["retry_attempts"]

# Function to fetch data from the API
def fetch_api_data(url, headers=None):
    if headers is None:
        headers = {'Accept-Charset': 'UTF-8'}
    session = requests.Session()
    retries = requests.adapters.Retry(total=retry_attempts, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount('https://', requests.adapters.HTTPAdapter(max_retries=retries))
    try:
        response = session.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()  # Raises exception for HTTP errors
        logging.info(f'Successfully fetched data from {url}')
        return response.json() if response.text else None
    except Exception as err:
        logging.error(f"Error occurred for {url}: {err}")
    return None

# Function to generate documentation for the API
def generate_documentation(api_name, api_url, api_data):
    doc = f"# {api_name} API Documentation\n\n"
    doc += f"**URL**: {api_url}\n\n"
    doc += "## Fields\n"
    doc += document_fields(api_data) if api_data else "No data available or data fetching failed."
    doc += "## Sample Response\n"
    doc += "```\n"
    doc += json.dumps(api_data, ensure_ascii=False, indent=4)[:3000]  # Limit the sample output
    doc += "\n```\n\n"
    return doc

# Recursive function to document fields
def document_fields(data, indent=0):
    doc = ""
    if isinstance(data, dict):
        for key, value in data.items():
            doc += " " * indent + f"- **{key}**: "
            if isinstance(value, list):
                doc += f"list of {'Unknown' if not value else 'dict' if isinstance(value[0], dict) else 'value'}\n"
                if value and isinstance(value[0], dict):
                    doc += document_fields(value[0], indent + 2)
            elif isinstance(value, dict):
                doc += "dictionary\n"
                doc += document_fields(value, indent + 2)
            else:
                doc += f"value\n"
    elif isinstance(data, list):
        if data and isinstance(data[0], dict):
            doc += "list of dictionaries\n"
            doc += document_fields(data[0], indent + 2)
    return doc

# Main function to create and write documentation for all APIs
def create_api_documentation(api_urls):
    if not os.path.exists('docs'):
        os.makedirs('docs')
    for url, api_key in api_urls.items():
        api_name = url.split("/")[-1] or url.split("/")[-2]  # Getting a simple name from URL
        headers = {'Authorization': f'Bearer {api_key}'} if api_key else None
        api_data = fetch_api_data(url, headers)
        documentation = generate_documentation(api_name, url, api_data)
        doc_filename = f"docs/{api_name.replace('/', '_')}_API_Documentation.md"
        with open(doc_filename, "w", encoding='utf-8') as file:
            file.write(documentation)
        logging.info(f"Documentation for {api_name} API created successfully.")

# Execute the documentation generation
create_api_documentation(api_urls)
