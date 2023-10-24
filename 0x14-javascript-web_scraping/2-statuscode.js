#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node your-script.js <URL>');
  process.exit(1);
}

request.get(process.argv[2], (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
