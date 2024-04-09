import urllib3
from pymisp import PyMISP

# Suppress SSL certificate verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define MISP URL, API key, and SSL certificate validation
misp_url = "add your MISP URL"
misp_key = "add your API key"
misp_verifycert = False

# Initialize PyMISP instance
misp = PyMISP(misp_url, misp_key, misp_verifycert)

# Input search value
search_value = input("Enter the value of the IOC to search for: ")

# Search for IOCs
response = misp.search(controller='attributes', value=search_value, pythonify=True)

# Print the entire response
print(response)

# Print results
if response:
    if isinstance(response, list):
        print("Found IOCs:")
        for attribute in response:
            comment = attribute.get('comment', 'N/A')  # Get 'comment' attribute or use 'N/A' if it doesn't exist
            category = attribute.get('category', 'N/A')  # Get 'category' attribute or use 'N/A' if it doesn't exist
            print(f"Type: {attribute['type']} | Value: {attribute['value']} | Comment: {comment} | Category: {category}")
    else:
        print("Found IOC:")
        comment = response.get('comment', 'N/A')  # Get 'comment' attribute or use 'N/A' if it doesn't exist
        category = response.get('category', 'N/A')  # Get 'category' attribute or use 'N/A' if it doesn't exist
        print(f"Type: {response['type']} | Value: {response['value']} | Comment: {comment} | Category: {category}")
else:
    print("No IOC found for the given search criteria.")
