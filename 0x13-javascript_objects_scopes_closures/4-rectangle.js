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

  rotate () {
    const newW = this.width;
    this.width = this.height;
    this.height = newW;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
