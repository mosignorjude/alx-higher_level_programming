#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rect = '';
    for (let i = 0; i < this.width; i++) {
      rect += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(rect);
    }
  }

  rotate () {
    const h = this.height;
    const w = this.width;
    this.height = w;
    this.width = h;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
