import requests

response = requests.get("https://ingress.academy")
if response.status_code == 200:
    print("✅ Successfully fetched data from Ingress")
else:
    print("❌ Failed to fetch data.")
