import requests
import json
import statistics
import os

# Define API URLs
api_urls = {
    "StatBank": "https://api.statbank.dk/v1/tables",  # Statistics Denmark API
    "Boliga": "https://api.boliga.dk/api/v2/sold/v2",  # Real estate prices
    "EnergiDataService": "https://api.energidataservice.dk/dataset/Elspotprices",  # Energy prices and consumption
    "DataForsyningen": "https://api.dataforsyningen.dk/postnumre",  # Address and postal code data
    "Rejseplanen": "https://www.rejseplanen.dk/webapp/index.html?language=en_EN#/webservice",  # Public transport schedules and routes
    "DanskRetstidende": "https://api.retsinformation.dk/v1/documents",  # Danish legal information and laws
    "CvrAPI": "https://api.cvr.dk/v1/virksomhed",  # Danish Business Register (CVR)
    "DanmarksMeteorologiskeInstitut": "https://dmigw.govcloud.dk/v2/metObs/collections/observation/items",  # Danish Meteorological Institute (DMI) - Weather observations
    "SundhedData": "https://api.sundhed.dk/v1/healthdata",  # Health data from Sundhed.dk
    "JobNet": "https://job.jobnet.dk/CV/FindCV",  # Job listings from Jobnet.dk
    "FolketingetAPI": "https://oda.ft.dk/api/1/",  # Data from the Danish Parliament
    "Geodatastyrelsen": "https://api.dataforsyningen.dk/hoejdemodel",  # Elevation models and geospatial data
    "KrakAPI": "https://api.krak.dk/v2.1/places",  # Place search and business listings
    "Virksomhedsstyrelsen": "https://cvrapi.dk/api",  # Company data API
    "Kulturarv": "https://api.kulturarv.dk/docs",  # Danish cultural heritage API
    "DanmarksStatistik": "https://api.statbank.dk/v1/",  # Statistics Denmark API
    "BygningsOgBoligRegister": "https://bbr.dk/BBRPublic",  # Building and housing register data
    "SundhedsdataStyrelsen": "https://www.esundhed.dk/Indhold/Service/Serviceoversigt",  # Danish Health Data Authority
    "MitID": "https://mitid.dk/public-api",  # MitID authentication and data access API
    "Vejdirektoratet": "https://www.vejdirektoratet.dk/api",  # Danish Road Directorate - Traffic information and road data
    "DanskPoliti": "https://politi.dk/api/v2/",  # Danish police data and crime reports
    "Kulturministeriet": "https://api.kultur.dk/v1/museums",  # Cultural institutions and museums data
    "E-boks": "https://api.e-boks.dk/v1/",  # Secure digital mailbox for Denmark
    "Tinglysning": "https://api.tinglysning.dk/",  # Danish land registration data
    "Folkebiblioteker": "https://api.bibliotek.dk/opensearch",  # Public library catalog data
    "Virksomhedsregnskab": "https://api.regnskab.dk/v1/company/",  # Company financial statements
    "NemID": "https://nemid.dk/api",  # Digital signature and authentication API
    "DanmarksAdresser": "https://api.dataforsyningen.dk/adresser",  # Danish address data
    "SkatAPI": "https://skat.dk/api",  # Danish Tax Authority data
    "OpenDataDK": "https://portal.opendata.dk/api/3/action/",  # Open data portal for Denmark
    "Bilstatistik": "https://bilstatistik.dk/api/v1/",  # Car statistics and registrations
    "DKKursus": "https://www.kursus.dk/api",  # Courses and training programs in Denmark
    "Foraeldreintra": "https://api.foraeldreintra.dk/v1",  # Parent communication platform for Danish schools
    "Husleje": "https://husleje.dk/api/v2/",  # Rent data in Denmark
    "Dagtilbud": "https://dagtilbud.dk/api/v1/",  # Daycare and early education data
    "DanskSprognævn": "https://dsn.dk/api/v2/",  # Danish Language Council data
    "NetcompanyAPI": "https://netcompany.dk/api",  # Services from Netcompany
    "TourismDK": "https://api.visitdenmark.com/v1/places",  # Danish tourism data
    "DanskBredbånd": "https://bredbaand.dk/api/v2/",  # Broadband coverage and speed data
    "BedreBolig": "https://bedrebolig.dk/api/v1/",  # Energy efficiency data for buildings
    "Arbejdstilsynet": "https://at.dk/api",  # Danish Working Environment Authority data
    "Erhvervsstyrelsen": "https://api.erhvervsstyrelsen.dk/",  # Danish Business Authority data
    "Energistyrelsen": "https://ens.dk/api",  # Danish Energy Agency data
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
