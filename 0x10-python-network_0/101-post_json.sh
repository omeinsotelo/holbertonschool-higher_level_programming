#!/bin/bash
# Sends a JSON POST request to a URL passed, displays body of response.
curl -sX POST -H "Content-type: application/json" -d @"$2" "$1"
