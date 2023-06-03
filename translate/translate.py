import requests

# Query
query = "sun rises in the east"
# Source Language
source = "en"
# Target Language
target = "te"

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
payload = {
	"q": query,
	"target": target,
	"source": source
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "f288a97e29mshc6ead1a886ce47fp13545cjsna9dde3633643",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

output = response.json()['data']['translations'][0]['translatedText']

print(source,":",query)
print(target,":",output)

# Create a file object
file = open("./output.txt", "w", encoding="utf-8")

# Write text to the file
file.write(response.json()['data']['translations'][0]['translatedText'])

# Close the file
file.close()