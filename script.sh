#/bin/bash
LIST=$(az network list-service-tags --location westeurope)

for item in $(echo $LIST | jq -c '.values[]'); do
	name=$(echo $item | jq -r '.id')
	echo $item | jq -r '.properties.addressPrefixes[]' >> ip/$name.txt
done