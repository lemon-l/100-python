import requests


url = 'https://ibaotu.com/'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers = headers)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('https://ibaotu.com/', data =payload)
print(r.text)