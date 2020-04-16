#!/usr/bin/python3
# script that takes in a URL, sends a request to the URL
import urllib.request
from sys import argv


if __name__ == '__main__':
    with urllib.request.urlopen(argv[1]) as reponse:
        header = reponse.info().__dict__["_headers"]
        header = [item[1] for item in header if item[0] == "X-Request-Id"]
        try:
            print(header[0])
        except Exception:
            print("None")
