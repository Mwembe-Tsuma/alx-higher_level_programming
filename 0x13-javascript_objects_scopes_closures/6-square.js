#!/usr/bin/node

const SquarePrint = require('./5-square');

class Square extends SquarePrint {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let rows = 0; rows < this.height; rows++) {
      let x = '';
      for (let cols = 0; cols < this.width; cols++) {
        x += c;
      }
      console.log(x);
    }
  }
}

module.exports = Square;
