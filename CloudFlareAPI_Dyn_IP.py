# This script was made because IP was not static and this fixes the problem.
# VeryUseful to host server for friends or others.
# Just be aware that bot will one day scanned ur Public IP, just make sure to put down a FW with strict rules
# Make sure you are NOT in DMZ mode and in isolated.
import requests


#Using the ipIFY API to fetch the present Public IP
def get_public_ip():
    try:
        # Use the ipify API to fetch the public IP
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data["ip"]
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
public_ip = get_public_ip()



# Your Cloudflare credentials and domain details
EMAIL = "YOUR EMAIL HERE"  # Replace with your Cloudflare account email
GLOBAL_API_KEY = "YOUR GLOBAL API KEY HERE"  # Replace with your Global API Key
ZONE_ID = "YOUR ZONE ID HERE"  # Replace with your Zone ID
RECORD_ID = "YOUR RECORD ID HERE"  # Replace with your Record ID - WAS HARD TO FIND, IF YOU NEED HELP WITH THAT LET ME KNOW
NEW_IP_ADDRESS = public_ip  # The new A record IP address

# Set the headers for authentication
HEADERS = {
    "X-Auth-Email": EMAIL,
    "X-Auth-Key": GLOBAL_API_KEY,
    "Content-Type": "application/json"
}

# API endpoint for updating a DNS record
url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{RECORD_ID}"

# Data payload with the new IP address
payload = {
    "type": "RECORD YOU WANT TO ADD (A)",
    "name": "YOUR DOMAIN NAME",  # Replace with your domain or subdomain
    "content": NEW_IP_ADDRESS,
    "ttl": 3600,  # Time to live in seconds
    "proxied": False  # Set True to use Cloudflare's proxy
}

# Send a PATCH request to update the DNS record
response = requests.patch(url, headers=HEADERS, json=payload)

# Check the response status
if response.status_code == 200:
    print("DNS A record updated successfully!")
else:
    print("Failed to update A record.")
    print(response.json())

