#!/usr/bin/node
/*
Class Square that defines a square and inherits from Rectangle of 4-rectangle.js
*/
class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let wXh = 0; wXh < this.height; wXh++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
