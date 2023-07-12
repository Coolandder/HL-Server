import json

import requests

words = json.load(open('words.json', 'r'))
response = requests.post('http://localhost:3000/load-words', json=words)
print(response.status_code)