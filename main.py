import requests  
from netaddr import IPNetwork, IPAddress  
  
def load_cidrs_from_github(user, repo):  
    cidrs = []  
    url = f"https://api.github.com/repos/{user}/{repo}/contents/ip"  
    headers = {"Accept": "application/vnd.github.v3+json"} # GitHub requires setting Accept header  
    r = requests.get(url, headers=headers)  
    r.raise_for_status() # ensure we notice bad responses  
    files = r.json()  
  
    for file in files:  
        if file["name"].endswith(".txt"):  
            file_url = file["download_url"]  
            file_content = requests.get(file_url).text  
            cidrs.extend(file_content.split('\n'))  
  
    return cidrs  
  
def is_ip_in_cidrs(ip, cidrs):  
    for cidr in cidrs:  
        cidr = cidr.strip()  # Remove leading/trailing whitespace  
        if cidr:  # Skip empty lines  
            try:  
                if IPAddress(ip) in IPNetwork(cidr):  
                    return True  
            except AddrFormatError:  
                print(f"Invalid CIDR format: {cidr}")  
    return False 
  
# Load CIDR ranges from Github  
cidrs = load_cidrs_from_github('groovy-sky', 'azure-ip-ranges')  
  
# Check if IP is in CIDRs  
print(is_ip_in_cidrs('4.149.254.67', cidrs))  # Returns True if IP is in any CIDR range, else False 