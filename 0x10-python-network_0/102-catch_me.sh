#!/bin/bash
#Bash script that makes a request to 0.0.0.0:5000/catch_me You got me
curl -o /dev/null -sw "You find me!" 0.0.0.0:5000/catch_me
