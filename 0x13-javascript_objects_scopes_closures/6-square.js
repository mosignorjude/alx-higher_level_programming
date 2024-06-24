#!/usr/bin/node
const parentSqr = require('./5-square');
module.exports = class Square extends parentSqr {
  charPrint (c) {
    let sqr = '';
    for (let i = 0; i < this.width; i++) {
      if (typeof (c) === 'undefined') {
        sqr += 'X';
      } else {
        sqr += c;
      }
    }
    for (let j = 0; j < this.height; j++) {
      console.log(sqr);
    }
  }
};
