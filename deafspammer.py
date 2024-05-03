import requests

def make_api_requests(api_url, payload):
    while True:
        response = requests.post(api_url, json=payload)
        print(response.json())

# Example of how to use the function
api_url = 'http://example.com/api'
payload = {'key': 'value'}
make_api_requests(api_url, payload)
