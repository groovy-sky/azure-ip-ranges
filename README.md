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