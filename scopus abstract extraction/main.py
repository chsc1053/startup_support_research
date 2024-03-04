import requests
import pandas as pd

# Scopus API key
API_KEY = ''
# API_KEY = ''

# API endpoint
BASE_URL = 'https://api.elsevier.com/content/search/scopus'

# User input
# query = input('Enter keyword cluster (keywords seperated by comma, no extra spaces): ')
query = "natural language processing,artificial intelligence"

keywords = query.split(",")
query = " OR ".join(keywords)

# API request parameters
params = {
    'apiKey': API_KEY,
    'query': query,
    #'view': 'COMPLETE',
    # 'field': 'dc:identifier,dc:title,subtypeDescription,dc:description',
    'field': 'dc:identifier,dc:title,subtypeDescription',
    'count': 25
}

# API request
response = requests.get(BASE_URL, params=params)

abstracts = []
# Check if request was successful
if response.status_code == 200:
    # Extract data from API response
    data = response.json()['search-results']['entry']
    # for i in data:
    #     print(i,"\n\n")
    count = 0
    for i in range(len(data)):
        if(count > 5):
            break
        data[i].pop('@_fa')
        data[i].pop('prism:url')
        data[i]['Scopus ID'] = data[i].pop('dc:identifier')[10:]
        data[i]['Title'] = data[i].pop('dc:title')
        data[i].pop('subtype')
        data[i]['Subtype'] = data[i].pop('subtypeDescription')
        # data[i]['Abstract'] = data[i].pop('dc:description')

        if(data[i]['Subtype'] == "Article" and count < 5):
            # abstracts.append(data[i]['Abstract'])
            abstracts.append(i)
            count += 1
            
    # for i in data:
    #     print(i,"\n\n")

    # Convert data to a Pandas DataFrame
    df = pd.DataFrame(data)
    print(df)

    print(abstracts)
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
