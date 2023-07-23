import requests
import base64

client_id = 'a744e34892764607a6c064f4729b1e20'
client_secret = '5184322668bf40e89fe584fd60feb768'

# Encode the client_id and client_secret in base64 format
auth_str = f"{client_id}:{client_secret}"
base64_auth_str = base64.b64encode(auth_str.encode()).decode()

# Set up the headers and data for the request
url = 'https://accounts.spotify.com/api/token'
headers = {
    'Authorization': 'Basic ' + base64_auth_str
}
data = {
    'grant_type': 'client_credentials'
}

# Send the POST request to get the access token
response = requests.post(url, headers=headers, data=data)

# Check if the request was successful (status code 200) and parse the response
if response.status_code == 200:
    body = response.json()
    token = body['access_token']
    print(body)
else:
    print(f"Error: {response.status_code}")
