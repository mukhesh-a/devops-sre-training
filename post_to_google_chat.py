"""Post a hello message to a Google Chat space using a webhook URL."""
import requests

# Paste your Google Chat space webhook URL here (from Space -> Manage webhooks -> Add webhook)
WEBHOOK_URL = "Paste your Google Chat space webhook URL here (from Space -> Manage webhooks -> Add webhook)"

response = requests.post(WEBHOOK_URL, json={"text": "Hello"}, timeout=10)
print(response.status_code)
