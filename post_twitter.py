import os
import requests

# Load environment variables
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

url = "https://api.twitter.com/2/tweets"

headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json"
}

post_data = {
    "text": "Hello Twitter (X) 👋 - This post was published directly using Python! 🚀"
}

response = requests.post(url, headers=headers, json=post_data)

if response.status_code == 201:
    print("✅ Tweet posted successfully!")
else:
    print(f"❌ Failed to post. Status: {response.status_code}, Response: {response.text}")
