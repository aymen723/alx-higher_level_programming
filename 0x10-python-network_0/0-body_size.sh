#!/bin/bash
# Get byte size of the HTTP res
curl -s "$1" | wc -c
