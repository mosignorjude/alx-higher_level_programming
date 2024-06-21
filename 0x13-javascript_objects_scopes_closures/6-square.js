#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof (c) === 'undefined') {
      this.print();
    } else {
      let sqr = '';
      for (let i = 0; i < this.width; i++) {
        sqr += 'C';
      }
      for (let j = 0; j < this.height; j++) {
        console.log(sqr);
      }
    }
  }
};
