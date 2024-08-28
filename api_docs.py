import requests
import json
import statistics
import os

# Define API URLs
api_urls = {
    "StatBank": "https://api.statbank.dk/v1/tables",
    "Boliga": "https://api.boliga.dk/api/v2/sold/v2",  # Make sure this is the correct URL
    "EnergiDataService": "https://api.energidataservice.dk/dataset/Elspotprices",
    "DataForsyningen": "https://api.dataforsyningen.dk/postnumre"
}

# Function to fetch data from the API with UTF-8 handling
def fetch_api_data(url):
    headers = {'Accept-Charset': 'UTF-8'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises exception for HTTP errors
        # Force response encoding to UTF-8
        response.encoding = 'utf-8'
        if response.text:
            return response.json()
        else:
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

# Function to generate detailed statistics for a list of data
def analyze_data(data):
    analysis = {'Type': 'Unknown'}
    if not data:
        return analysis  # Return early if data is empty

    try:
        if all(isinstance(i, str) for i in data):
            lengths = [len(i) for i in data] if data else []
            analysis.update({
                'Type': 'String',
                'Total Count': len(data),
                'Unique Count': len(set(data)),
                'Missing Values': data.count(''),
                'Average Length': statistics.mean(lengths) if lengths else 0,
                'Median Length': statistics.median(lengths) if lengths else 0,
                'Mode Length': statistics.mode(lengths) if lengths and len(set(lengths)) > 1 else 'N/A',
                'Max Length': max(lengths) if lengths else 0,
                'Min Length': min(lengths) if lengths else 0
            })
        elif all(isinstance(i, (int, float)) for i in data):
            analysis.update({
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
            })
    except Exception as e:
        print(f"Error processing data: {e}")
    return analysis

# Additional functions would remain similar, with UTF-8 encoded file writing

# Ensure UTF-8 encoding during JSON serialization
def serialize_json(data):
    return json.dumps(data, ensure_ascii=False, indent=4)

# Generate documentation with UTF-8 encoded JSON
def generate_documentation(api_name, api_url, api_data):
    doc = f"# {api_name} API Documentation\n\n"
    doc += f"**URL**: {api_url}\n\n"
    doc += "## Sample Response\n"
    doc += "```\n"
    doc += serialize_json(api_data)[:1000]  # Limit the sample output, using a custom serializer
    doc += "\n```\n\n"
    doc += "## Fields\n"
    if api_data:
        doc += document_fields(api_data)
    else:
        doc += "No data available or data fetching failed."
    return doc

# Main function to create and write documentation for all APIs
def create_api_documentation(api_urls):
    for api_name, api_url in api_urls.items():
        api_data = fetch_api_data(api_url)
        if api_data:
            documentation = generate_documentation(api_name, api_url, api_data)
            with open(f"docs/{api_name}_API_Documentation.md", "w", encoding='utf-8') as file:
                file.write(documentation)
            print(f"Documentation for {api_name} API created successfully.")
        else:
            print(f"Failed to fetch data for {api_name} API. Check the API endpoint and network status.")

# Ensure the 'docs' directory exists
if not os.path.exists('docs'):
    os.makedirs('docs')

# Execute the documentation generation
create_api_documentation(api_urls)
