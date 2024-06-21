#!/usr/bin/node
const parentSqr = require('./5-square');
module.exports = class Square extends parentSqr {
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
