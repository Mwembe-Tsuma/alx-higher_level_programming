#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node your-script.js <API-URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const dict = JSON.parse(body).reduce((acc, elem) => {
    if (!acc[elem.userId]) {
      if (elem.completed) {
        acc[elem.userId] = 1;
      }
    } else {
      if (elem.completed) {
        acc[elem.userId] += 1;
      }
    }
    return acc;
  }, {});
  console.log(dict);
});
