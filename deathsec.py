import requests

def make_api_requests(api_url, payload):
    response = requests.post(api_url, json=payload)
    return response.json()

# Example of how to use the function
api_url = 'http://example.com/api'
payload = {'key': 'value'}
response_data = make_api_requests(api_url, payload)
print(response_data)
