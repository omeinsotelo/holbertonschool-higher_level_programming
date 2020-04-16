#!/usr/bin/python3
# Sends a POST request to the passed URL with the email as a parameter
import requests
from sys import argv


if __name__ == "__main__":
    values = {'email': argv[2]}
    r = requests.post(argv[1], data=values)
    print(r.text)
