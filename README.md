#  Azure IP Ranges and Service Tags – Public Cloud

This repository obtains and stores (using Action) the current Azure's Datacenters public IP addresses. Results are available in [the ip folder](/ip).

## Why

By default, Microsoft doesn't provide a posibility to obtain Azure DC IP anonymously. Instead, it suggest to use [Azure CLI/Powershell/REST](https://docs.microsoft.com/en-us/azure/virtual-network/service-tags-overview#service-tags-on-premises) to query Azure using an authorized account. 

## How

[flow](/.github/workflows/main.yml)
[script](/ip/script.sh)