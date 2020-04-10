#!/bin/bash
# script takes URL displays HTTP methods the server will accept.
curl -sI "$1" | grep Allow: | cut -d" " -f2-
