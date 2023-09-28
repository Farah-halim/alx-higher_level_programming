#!/bin/bash
# This script takes in a URL, sends a request to that URL using curl, and displays the size of the body of the response in bytes
curl -sI "$1" | grep "Content-Length:" | cut -c 17- 
