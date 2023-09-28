#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -o /dev/null -sw "You got me!" -L 0.0.0.0:5000/catch_me
