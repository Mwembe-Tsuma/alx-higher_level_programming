#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let rows = 0; rows < this.height; rows++) {
      let x = '';
      for (let cols = 0; cols < this.width; cols++) {
        x += 'X';
      }
      console.log(x);
    }
  }
}

module.exports = Rectangle;
