import requests
import json
import statistics
import os

# Define API URLs
api_urls = {
    "StatBank": "https://api.statbank.dk/v1/tables",
    "Boliga": "https://api.boliga.dk/api/v2/sold/v2",  # Confirm correct URL
    "EnergiDataService": "https://api.energidataservice.dk/dataset/Elspotprices",
    "DataForsyningen": "https://api.dataforsyningen.dk/postnumre"
}

# Function to fetch data from the API
def fetch_api_data(url):
    headers = {'Accept-Charset': 'UTF-8'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises exception for HTTP errors
        response.encoding = 'utf-8'  # Force response encoding to UTF-8
        return response.json() if response.text else None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

# Function to generate detailed statistics for a list of data
def analyze_data(data):
    if not data:
        return {'Type': 'None', 'Total Count': 0}
    try:
        if all(isinstance(i, str) for i in data):
            lengths = [len(i) for i in data]
            return {
                'Type': 'String',
                'Total Count': len(data),
                'Unique Count': len(set(data)),
                'Missing Values': data.count(''),
                'Average Length': statistics.mean(lengths) if lengths else 0,
                'Median Length': statistics.median(lengths) if lengths else 0,
                'Mode Length': statistics.mode(lengths) if lengths and len(set(lengths)) > 1 else 'N/A',
                'Max Length': max(lengths) if lengths else 0,
                'Min Length': min(lengths) if lengths else 0
            }
        elif all(isinstance(i, (int, float)) for i in data):
            return {
                'Type': 'Number',
                'Total Count': len(data),
                'Unique Count': len(set(data)),
                'Missing Values': data.count(None),
                'Mean': statistics.mean(data) if data else 0,
                'Median': statistics.median(data) if data else 0,
                'Standard Deviation': statistics.stdev(data) if len(data) > 1 else 'N/A',
                'Variance': statistics.variance(data) if len(data) > 1 else 'N/A',
                'Mode': statistics.mode(data) if data and len(set(data)) > 1 else 'N/A',
                'Range': max(data) - min(data) if data else 0,
                'Max': max(data) if data else 0,
                'Min': min(data) if data else 0
            }
    except Exception as e:
        print(f"Error processing data: {e}")
    return {'Type': 'Unknown'}

# Recursive function to document fields
def document_fields(data, indent=0):
    doc = ""
    if isinstance(data, dict):
        for key, value in data.items():
            doc += " " * indent + f"- **{key}**: "
            if isinstance(value, list):
                doc += f"list of {analyze_data(value)['Type']}\n"
                if value and isinstance(value[0], dict):
                    doc += document_fields(value[0], indent + 2)
            elif isinstance(value, dict):
                doc += "dictionary\n"
                doc += document_fields(value, indent + 2)
            else:
                doc += f"{analyze_data([value])['Type']}\n"
    elif isinstance(data, list):
        if data and isinstance(data[0], dict):
            doc += "list of dictionaries\n"
            doc += document_fields(data[0], indent + 2)
    return doc

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

# Main function to create and write documentation for all APIs
def create_api_documentation(api_urls):
    if not os.path.exists('docs'):
        os.makedirs('docs')
    for api_name, api_url in api_urls.items():
        api_data = fetch_api_data(api_url)
        if api_data:
            documentation = generate_documentation(api_name, api_url, api_data)
            with open(f"docs/{api_name}_API_Documentation.md", "w", encoding='utf-8') as file:
                file.write(documentation)
            print(f"Documentation for {api_name} API created successfully.")
        else:
            print(f"Failed to fetch data for {api_name} API. Check the API endpoint and network status.")

# Execute the documentation generation
create_api_documentation(api_urls)
