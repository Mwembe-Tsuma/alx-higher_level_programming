#!/usr/bin/node

const dict = require('./101-data').dict;

const listAll = Object.entries(dict);
const val = Object.values(dict);
const Uniq = [...new Set(val)];
const newDict = {};
for (const x in Uniq) {
  const list = [];
  for (const y in listAll) {
    if (listAll[y][1] === Uniq[x]) {
      list.unshift(listAll[y][0]);
    }
  }
  newDict[Uniq[x]] = list;
}
console.log(newDict);
