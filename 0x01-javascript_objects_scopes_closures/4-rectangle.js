#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      if (i < this.height) {
        process.stdout.write('\n');
      }
    }
  }
  rotate () {
      this.width = this.width + this.height;
      this.height = this.width - this.height;
      this.width = this.width - this.height;
    }
  
    double () {
      this.width = this.width * 2;
      this.height = this.height * 2;
    }
};
module.exports = Rectangle;
