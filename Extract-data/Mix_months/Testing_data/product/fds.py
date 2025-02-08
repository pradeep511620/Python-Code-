import requests

# Define a list of proxy servers
proxies = [
    {'http': 'http://proxy1.example.com:8080', 'https': 'http://proxy1.example.com:8080'},
    {'http': 'http://proxy2.example.com:8080', 'https': 'http://proxy2.example.com:8080'},
    # Add more proxy servers as needed
]

# Create a session object
session = requests.Session()

# Iterate over the proxies and send requests
for proxy in proxies:
    try:
        # Set the proxy for the session
        session.proxies = proxy

        # Make a request using the session
        response = session.get('http://www.example.com')

        # Process the response as needed
        print(response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
