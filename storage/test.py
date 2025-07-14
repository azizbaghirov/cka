import requests

response = requests.get("https://api.github.com")
if response.status_code == 200:
    print("✅ Successfully fetched data from GitHub API!")
else:
    print("❌ Failed to fetch data.")
