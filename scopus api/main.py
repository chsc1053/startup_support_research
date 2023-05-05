import requests, json
import pandas as pd

# Scopus API key
API_KEY = '046ebcb86c11856c2c9d978b0570109f'

# API endpoint
BASE_URL = 'https://api.elsevier.com/content/search/scopus'

# User input
# query = input('Enter your query: ')
query = 'solar energy'

# API request parameters
params = {
    'apiKey': API_KEY,
    'query': query,
    # 'field': 'dc:identifier,dc:title,dc:creator,dc:description,authkeywords',
    'view': 'STANDARD',
    'count': 1
}

# API request
response = requests.get(BASE_URL, params=params)

# Check if request was successful
if response.status_code == 200:
    # Extract data from API response
    data = response.json()['search-results']['entry']
    # print(data)

    for i in range(len(data)):
        data[i].pop('@_fa')
        data[i].pop('prism:url')
        data[i]['SCOPUS_ID'] = data[i].pop('dc:identifier')[10:]
        data[i]['eid'] = data[i].pop('eid')
        data[i]['Title'] = data[i].pop('dc:title')
        data[i]['Creator'] = data[i].pop('dc:creator')
        data[i]['Publication Name'] = data[i].pop('prism:publicationName')
        data[i]['ISSN'] = data[i].pop('prism:issn')
        data[i]['eISSN'] = data[i].pop('prism:eIssn')
        data[i]['Volume'] = data[i].pop('prism:volume')
        data[i]['Page Range'] = data[i].pop('prism:pageRange')
        data[i]['Cover Date'] = data[i].pop('prism:coverDate')
        data[i]['Cover Display Date'] = data[i].pop('prism:coverDisplayDate')
        data[i]['DOI'] = data[i].pop('prism:doi')
        data[i]['pii'] = data[i].pop('pii')
        data[i]['citedby-count'] = data[i].pop('citedby-count')
        data[i]['Affiliation Name'] = data[i]['affiliation'][i]['affilname']
        data[i]['Affiliation City'] = data[i]['affiliation'][i]['affiliation-city']
        data[i]['Affiliation Country'] = data[i]['affiliation'][i]['affiliation-country']
        data[i].pop('affiliation')
        data[i]['Aggregation Type'] = data[i].pop('prism:aggregationType')
        data[i]['Subtype'] = data[i].pop('subtype')
        data[i]['Subtype Description'] = data[i].pop('subtypeDescription')
        data[i]['Source ID'] = data[i].pop('source-id')
        data[i]['Open Access'] = data[i].pop('openaccess')
        data[i]['Open Access Flag'] = data[i].pop('openaccessFlag')
        
        abstract_link =  data[i]['link'][2]['@href']
        print(abstract_link)

        #fetch abstract from abstract_link and apeennd to data[i]

        data[i].pop('link')
    
    print(data)

    # Convert data to a Pandas DataFrame
    df = pd.DataFrame(data)

    # Save data to JSON file with indented format
    df.to_json('output.json', orient='records', indent=4)

    # Save data to CSV file
    df.to_csv('output.csv', index=False)
else:
    print('Error:', response.status_code)