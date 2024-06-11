import requests
import json
import statistics
from collections import Counter

# Define API URLs
api_urls = {
    "StatBank": "https://api.statbank.dk/v1/tables",
    "Boliga": "https://api.boliga.dk",
    "EnergiDataService": "https://api.energidataservice.dk/dataset/Elspotprices",
    "DataForsyningen": "https://api.dataforsyningen.dk/postnumre"
}

# Function to fetch data from the API
def fetch_api_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

# Function to generate detailed statistics for a list of data
def analyze_data(data):
    analysis = {}
    if all(isinstance(i, str) for i in data):
        lengths = [len(i) for i in data]
        analysis['Type'] = 'String'
        analysis['Total Count'] = len(data)
        analysis['Unique Count'] = len(set(data))
        analysis['Missing Values'] = data.count('')
        analysis['Average Length'] = statistics.mean(lengths)
        analysis['Median Length'] = statistics.median(lengths)
        analysis['Mode Length'] = statistics.mode(lengths) if len(set(lengths)) > 1 else 'N/A'
        analysis['Max Length'] = max(lengths)
        analysis['Min Length'] = min(lengths)
    elif all(isinstance(i, (int, float)) for i in data):
        analysis['Type'] = 'Number'
        analysis['Total Count'] = len(data)
        analysis['Unique Count'] = len(set(data))
        analysis['Missing Values'] = data.count(None)
        analysis['Mean'] = statistics.mean(data)
        analysis['Median'] = statistics.median(data)
        if len(data) > 1:
            analysis['Standard Deviation'] = statistics.stdev(data)
            analysis['Variance'] = statistics.variance(data)
            analysis['Mode'] = statistics.mode(data) if len(set(data)) > 1 else 'N/A'
            analysis['Range'] = max(data) - min(data)
        else:
            analysis['Standard Deviation'] = 'N/A'
            analysis['Variance'] = 'N/A'
            analysis['Mode'] = 'N/A'
            analysis['Range'] = 'N/A'
        analysis['Max'] = max(data)
        analysis['Min'] = min(data)
    else:
        analysis['Type'] = 'Mixed or Unknown'
        analysis['Sample Data'] = data[:5]
    return analysis

# Recursive function to document fields and their possible values
def document_fields(data, indent=0):
    doc = ""
    if isinstance(data, dict):
        for key, value in data.items():
            doc += " " * indent + f"- **{key}**: "
            if isinstance(value, list):
                if len(value) > 0 and isinstance(value[0], dict):
                    doc += "list of dictionaries\n"
                    doc += document_fields(value[0], indent + 2)
                else:
                    analysis = analyze_data(value)
                    doc += f"list of {analysis['Type']}\n"
                    for stat_key, stat_value in analysis.items():
                        if stat_key != 'Type':
                            doc += " " * (indent + 2) + f"- {stat_key}: {stat_value}\n"
            else:
                analysis = analyze_data([value])
                doc += f"{analysis['Type']}\n"
                for stat_key, stat_value in analysis.items():
                    if stat_key != 'Type':
                        doc += " " * (indent + 2) + f"- {stat_key}: {stat_value}\n"
    elif isinstance(data, list):
        if len(data) > 0 and isinstance(data[0], dict):
            doc += "list of dictionaries\n"
            doc += document_fields(data[0], indent + 2)
        else:
            analysis = analyze_data(data)
            doc += f"list of {analysis['Type']}\n"
            for stat_key, stat_value in analysis.items():
                if stat_key != 'Type':
                    doc += " " * (indent + 2) + f"- {stat_key}: {stat_value}\n"
    return doc

# Function to generate documentation for the API
def generate_documentation(api_name, api_url, api_data):
    doc = f"# {api_name} API Documentation\n\n"
    doc += f"**URL**: {api_url}\n\n"
    doc += "## Sample Response\n"
    doc += "```\n"
    doc += json.dumps(api_data, indent=4)[:1000]  # Truncate for brevity in example
    doc += "\n```\n\n"
    doc += "## Fields\n"
    doc += document_fields(api_data)
    return doc

# Main function to create documentation for all APIs
def create_api_documentation(api_urls):
    for api_name, api_url in api_urls.items():
        api_data = fetch_api_data(api_url)
        if api_data:
            documentation = generate_documentation(api_name, api_url, api_data)
            with open(f"docs/{api_name}_API_Documentation.md", "w") as file:
                file.write(documentation)
            print(f"Documentation for {api_name} API created successfully.")
        else:
            print(f"Failed to fetch data for {api_name} API.")

# Ensure the docs directory exists
import os
if not os.path.exists('docs'):
    os.makedirs('docs')

# Run the documentation generation
create_api_documentation(api_urls)
