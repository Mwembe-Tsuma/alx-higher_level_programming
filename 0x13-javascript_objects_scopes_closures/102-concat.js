#!/usr/bin/node

const fs = require('fs');

const file1Path = fs.readFileSync(process.argv[2]).toString();
const file2Path = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], file1Path + file2Path);
