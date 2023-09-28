#!/bin/bash
#takes URL as an argument, sends a GET request, and displays the body of the response
curl -s -X GET $1 -H "X-School-User-Id: 98" -L
