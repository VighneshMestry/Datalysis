import requests

url = 'http://localhost:8501/api/signup'

# Replace the placeholders with the actual data you want to send
data = {
    'email': 'user@example.com',
    'password': 'mypassword',
    'name': 'John Doe'
}

response = requests.post(url, data=data)

if response.status_code == 200:
    print('Signup successful!')
else:
    print(f'Signup failed with status code {response.status_code}')
