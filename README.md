#  Azure IP Ranges and Service Tags – Public Cloud

This repository obtains and stores (using Action) the current Azure's Datacenters public IP addresses. Results you can check [here](/ip).

![](/img/logo.png)

## Why?

By default, Microsoft doesn't provide a posibility to obtain Azure DC IP anonymously. Instead, it suggest to use [Azure CLI/Powershell/REST](https://docs.microsoft.com/en-us/azure/virtual-network/service-tags-overview#service-tags-on-premises) to query Azure using an authorized account. **The main aim of this repository is** to show how with a minimum effort you can obtain and store all necessary configs/data in one place.

## How?

There is only [one workflow](/.github/workflows/main.yml) which do a few things:
1. Converts and stores SPN_KEY_BASE64 secret as a certificate (which is used for authentication).
2. Using the certificate logins to Azure CLI.
3. Executes [script.sh](/ip/script.sh), which get IPs and stores them in separate files locally.
4. Pushes changes to this repository.

## What?

The result of the workflow is a bunch of files with IP addresses. For easier search I also wrote a small Python script which can be used to search for a specific IP in all of these files. The script is located [here](/search.py). You can install it using the following command(you'll need to have Python and Linux OS/WSL installed):

```
curl -s https://raw.githubusercontent.com/groovy-sky/azure-ip-ranges/main/requirements.txt | xargs -n 1 pip install --user
alias azsearch='curl -s https://raw.githubusercontent.com/groovy-sky/azure-ip-ranges/main/search.py | python -'  # Add this to your .bashrc or .zshrc
```

After that you can use it like this:

```
azsearch [IP_ADDRESS]
```

As a result you will get a list of files where the IP is located (or none if it's not found). Also works in Azure CLI:
![](/img/ipsearch_example.png)