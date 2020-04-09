#!/bin/bash
# URL as an argument, sends a GET request, and displays the body of the response
curl "$1" -sH "X-HolbertonSchool-User-Id: 98"
