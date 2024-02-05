import requests  
from netaddr import IPNetwork, IPAddress, AddrFormatError  
import argparse  
from concurrent.futures import ThreadPoolExecutor  
import re  
  
# Hard-code GitHub username and repo  
user = 'groovy-sky'  
repo = 'azure-ip-ranges'  
  
# Load CIDRs from GitHub
def load_cidrs_from_github(user, repo):  
    url = f"https://api.github.com/repos/{user}/{repo}/contents/ip"  
    headers = {"Accept": "application/vnd.github.v3+json"}  
    r = requests.get(url, headers=headers)  
    r.raise_for_status()  
    files = r.json()  
    return files  

# Check if IP is in CIDRs
def is_ip_in_cidrs(ip, file):  
    try:  
        file_content = requests.get(file["download_url"]).text  
        cidrs = file_content.split('\n')  
        for cidr in cidrs:  
            cidr = cidr.strip()  
            if cidr:  
                try:  
                    if IPAddress(ip) in IPNetwork(cidr):  
                        return file["download_url"], cidr  
                except AddrFormatError:  
                    pass  
    except Exception as e:  
        print(f"Error processing file {file['download_url']}: {e}")  
    return None  
  
# Initialize parser  
parser = argparse.ArgumentParser(description="Check if IP is in any CIDR range in a GitHub repository")  
parser.add_argument("ip", help="IP address to check")  
  
args = parser.parse_args()  
  
# Clean up and validate IP to match IPv4 or IPv6 format
ip = args.ip.strip()  # Remove leading and trailing whitespaces  
if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip) and not re.match(r'^[a-fA-F0-9:]+$', ip): 
    print("Invalid IP address")  
    exit(1)  
  
# Load CIDR ranges from Github  
files = load_cidrs_from_github(user, repo)  
  
# Check if IP is in CIDRs  
with ThreadPoolExecutor() as executor:  
    futures = [executor.submit(is_ip_in_cidrs, ip, file) for file in files if file["name"].endswith(".txt")]  
  
for future in futures:  
    result = future.result()  
    if result:  
        print(f"{ip} found in {result[0]} [CIDR range: {result[1]}]")  
