#!/bin/bash
# Sends a request to a URL, displays only status code of response.
curl -s "$1" -o /dev/null -w '%{http_code}'
