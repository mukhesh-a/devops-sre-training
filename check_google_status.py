"""Check and print the HTTP status code of the Google website."""
import requests

response = requests.get("https://www.google.com", timeout=10)
print(response.status_code)