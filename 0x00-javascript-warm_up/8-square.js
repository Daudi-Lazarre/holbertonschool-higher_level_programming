#!/usr/bin/node

const val = Number(process.argv[2]);

if (isNaN(val)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < value; i++) {
    let v = '';
    for (let j = 0; j < value; j++) {
      v += 'X';
    }
    console.log(v);
  }
}