import requests
import json
import statistics
import os

# Define API URLs
api_urls = {
    "StatBank": "https://api.statbank.dk/v1/tables",
    "Boliga": "https://api.boliga.dk/api/v2/sold/v2",  # Ensure this is the correct endpoint
    "EnergiDataService": "https://api.energidataservice.dk/dataset/Elspotprices",
    "DataForsyningen": "https://api.dataforsyningen.dk/postnumre"
}

# Function to fetch data from the API
def fetch_api_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
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
        return analysis

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
    return analysis

# Recursive function to document fields and their possible values
def document_fields(data, indent=0):
    doc = ""
    if isinstance(data, dict):
        for key, value in data.items():
            doc += " " * indent + f"- **{key}**: "
            if isinstance(value, list):
                doc += "list of items\n"
                if value and isinstance(value[0], (dict, list)):
                    doc += document_fields(value[0], indent + 2)
                else:
                    analysis = analyze_data(value)
                    for stat_key, stat_value in analysis.items():
                        doc += " " * (indent + 2) + f"- {stat_key}: {stat_value}\n"
            elif isinstance(value, dict):
                doc += "dictionary\n"
                doc += document_fields(value, indent + 2)
            else:
                analysis = analyze_data([value])
                for stat_key, stat_value in analysis.items():
                    doc += " " * (indent + 2) + f"- {stat_key}: {stat_value}\n"
    elif isinstance(data, list) and data:
        if isinstance(data[0], dict):
            doc += "list of dictionaries\n"
            doc += document_fields(data[0], indent + 2)
        else:
            analysis = analyze_data(data)
            doc += f"list of {analysis['Type']}\n"
            for stat_key, stat_value in analysis.items():
                doc += " " * (indent + 2) + f"- {stat_key}: {stat_value}\n"
    return doc

# Function to generate documentation for the API
def generate_documentation(api_name, api_url, api_data):
    doc = f"# {api_name} API Documentation\n\n"
    doc += f"**URL**: {api_url}\n\n"
    doc += "## Sample Response\n"
    doc += "```\n"
    doc += json.dumps(api_data, indent=4)[:1000]  # Limit the sample output
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
