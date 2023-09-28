#!/bin/bash
# script that sends a DELETE request to the URL passed as the 1st arg
curl -s -X DELETE $1 -L
