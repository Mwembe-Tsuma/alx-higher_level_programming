#!/bin/bash
#Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -sd "user_id=98" -X PUT -H "You got me!" -L 0.0.0.0:5000/catch_me
