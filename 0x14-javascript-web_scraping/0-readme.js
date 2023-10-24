#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 3) {
  console.error('Usage: node your-script.js <file-path>');
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', function (err, result) {
  if (err) {
    console.error(err);
  } else {
    console.log(result);
  }
});
