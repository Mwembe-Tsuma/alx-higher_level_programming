#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length < 4) {
  console.error('Usage: node your-script.js <URL> <file-path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  try {
    fs.writeFile(filePath, body, 'utf8', function (err, result) { if (err) console.log(err); });
  } catch (err) {
    console.log(err);
  }
});
