import requests, uuid, json

query = 'Microsoft is ending support for Cortana in Windows. In a support page spotted by XDA Developers and Windows Central, the company says it will \"no longer support Cortana in Windows as a standalone app\" starting later this year.'
source_language = 'en'
target_languages = ['te','hi','ta']
target_languages_full = ['Telugu','Hindi','Tamil']

key = "6d5784ec03fb4d03a33c2fd56991b5c0"
endpoint = "https://api.cognitive.microsofttranslator.com"
location = "centralindia"
path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': source_language,
    'to': target_languages
}
headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}
body = [{
    'text': query
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

outputs = []
for i in range(len(target_languages)):
    outputs.append(response[0]["translations"][i]["text"])


print(source_language,":\n",query)

file = open("./output.txt", "w", encoding="utf-8")
file.write(source_language + ":\n" + query)
file.close()

file = open("./output.txt", "a", encoding="utf-8")
for i in range(len(target_languages)):
    print("\n",target_languages_full[i],":\n",outputs[i])
    file.write("\n\n" + target_languages_full[i] + ":\n" + outputs[i])
file.close()