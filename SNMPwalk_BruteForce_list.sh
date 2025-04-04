#!/bin/bash

echo "Enter Target IP address: "
read TARGET_IP

echo "Enter the name of the wordlist (make sure it's in the same directory): "
read WORDLIST

# Loop through each community string in the wordlist
while IFS= read -r COMMUNITY; do
    echo "Trying community string: $COMMUNITY"
    snmpwalk -v2c -c "$COMMUNITY" "$TARGET_IP"
    if [ $? -eq 0 ]; then
        echo "Success with community string: $COMMUNITY"
        break
    fi
done < "$WORDLIST"
