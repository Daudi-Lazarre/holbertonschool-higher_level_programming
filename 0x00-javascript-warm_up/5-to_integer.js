#!/usr/bin/node

const value = process.argv[2];
const num = isNaN(Number(value));

console.log(num ? 'Not a number' : `My number: ${Number(value)}`);