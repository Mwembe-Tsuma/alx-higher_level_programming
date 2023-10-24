#!/usr/bin/node

const fs = require('fs');

if (process.argv.length < 4) {
  console.error('Usage: node your-script.js <file-path> <string-to-write>');
  process.exit(1);
}

const path = process.argv[2];
const content = process.argv[3];

fs.writeFile(path, content, 'utf8', function (err) {
  if (err) {
    console.error(err);
  } else {
    console.log(`Successfully wrote to ${path}`);
  }
});
