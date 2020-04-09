#!/bin/bash
# Takes in a URL, sends a GET request, displays the body of the response 
curl "$1" -sLX GET
