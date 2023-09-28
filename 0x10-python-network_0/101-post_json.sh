#!/bin/bash
#JSON POST request to a URL passed as the 1st arg, and displays the body of the response
curl -s -X POST $1 -H "Content-Type: application/json" -d @$2 -L
