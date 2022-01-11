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
  };
  module.exports = Rectangle;