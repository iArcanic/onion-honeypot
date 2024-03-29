import requests

# Define the URL of the HTTP server
url = 'http://http-honeypot:5000'  # Replace 'http-honeypot' with the hostname of your HTTP honeypot container

try:
    # Send a GET request to the HTTP server
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Connection established successfully with the HTTP server")
    else:
        print(f"Failed to establish connection with the HTTP server. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while connecting to the HTTP server: {e}")
