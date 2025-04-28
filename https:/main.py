# import requests 

# URL for Warpcast public posts API
url = "https://api.farcaster.xyz/v1/posts"

Send a GET request to the API
response = requests.get(url)

Check if the request was successful
if response.status_code == 200:
    posts = response.json()
    print(posts)
else:
    print("Failed to fetch data from Warpcast API")
