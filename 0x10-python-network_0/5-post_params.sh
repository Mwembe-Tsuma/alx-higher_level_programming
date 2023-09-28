#!/bin/bash
#takes URL, sends a POST request, and displays the body of the response
curl -s -X POST $1 -d "email=test@gmail.com&subject=I will always be here for PLD" -L
