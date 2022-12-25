import requests
import json

# Set the API endpoint URL and the desired number of proxies to retrieve
url = "https://proxylist.geonode.com/api/proxy-list?limit=500&sort_by=lastChecked&sort_type=desc"

# Open the text file in write mode
with open("proxies.txt", "w") as f:
  # Iterate over the pages from 1 to 15
  for page in range(1, 18):
    # Set the page parameter in the URL
    url_with_page = f"{url}&page={page}"
    # Send a GET request to the API endpoint and parse the response as JSON
    response = requests.get(url_with_page)
    data = response.json()
    # Extract the list of proxies from the JSON data
    proxies = data["data"]
    # Iterate over the list of proxies and write the IP:PORT for each proxy to the text file
    for proxy in proxies:
      ip = proxy["ip"]
      port = proxy["port"]
      f.write(f"{ip}:{port}\n")
