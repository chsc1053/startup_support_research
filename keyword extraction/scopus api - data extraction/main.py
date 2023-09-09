import requests
import pandas as pd

# Scopus API key
# API_KEY = '046ebcb86c11856c2c9d978b0570109f'
API_KEY = '7523d7b1a47c95487a4cdd29b27624ef'

# API endpoint
BASE_URL = 'https://api.elsevier.com/content/search/scopus'

# User input
# query = input('Enter your query: ')
query = "data science"

# API request parameters
params = {
    'apiKey': API_KEY,
    'query': query,
    #'view': 'COMPLETE',
    'field': 'dc:identifier,dc:title,prism:coverDate,prism:aggregationType,subtypeDescription,dc:description,authkeywords',
    # 'field': 'dc:identifier,dc:title,prism:coverDate,prism:aggregationType,subtypeDescription',
    'count': 10
}

# API request
response = requests.get(BASE_URL, params=params)

# Check if request was successful
if response.status_code == 200:
    # Extract data from API response
    data = response.json()['search-results']['entry']
    # for i in data:
    #     print(i,"\n\n")

    for i in range(len(data)):
        data[i].pop('@_fa')
        data[i].pop('prism:url')
        data[i]['Scopus ID'] = data[i].pop('dc:identifier')[10:]
        data[i]['Title'] = data[i].pop('dc:title')
        data[i]['Cover Date'] = data[i].pop('prism:coverDate')
        data[i]['Aggregation Type'] = data[i].pop('prism:aggregationType') 
        data[i].pop('subtype')
        data[i]['Subtype'] = data[i].pop('subtypeDescription')
            
    # for i in data:
    #     print(i,"\n\n")

    # Convert data to a Pandas DataFrame
    df = pd.DataFrame(data)

    print(df)

    # Save data to JSON file with indented format
    df.to_json('./output.json', orient='records', indent=4)

    # Save data to CSV file
    df.to_csv('./output.csv', index=False)

    print("Write successful")
else:
    print('Error:', response.status_code)


'''
Scopus Search Views

STANDARD

link ref=scopus - Scopus abstract detail page URL

dc:identifier - Scopus ID

dc:title - Article Title

prism:aggregationType - Source Type

subtypeDescription - Document Type description

citedby-count - Cited-by Count

prism:publicationName - Source Title

prism:volume - Volume

prism:coverDate - Publication Date(YYYY-MM-DD)

dc:creator  - First Author

openaccess - Open Access status

affilname - Affiliation name

affiliation-city - Affiliation city

affiliation-country - Affiliation country

COMPLETE

dc:description - Abstract

authkeywords - Author Keywords
'''