#!/usr/bin/node
/*
Empty class Rectangle that defines a rectangle:
*/
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let wXh = 0; wXh < this.height; wXh++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
