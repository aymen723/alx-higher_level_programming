#!/bin/bash
# Sends a GET request to a URL
curl -s -o /dev/null -w "%{http_code}" "$1"
