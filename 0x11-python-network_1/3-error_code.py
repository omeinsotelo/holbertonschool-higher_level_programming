#!/usr/bin/python3
# Sends a request to the URL and displays the body of the response
import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    try:
        request = urllib.request.Request(argv[1])
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
