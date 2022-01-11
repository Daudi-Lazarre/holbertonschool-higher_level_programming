#!/usr/bin/node

const fs = require('fs');
const argv = process.argv;
const file = argv[2];
const string = argv[3];

fs.writeFile(filename, string, 'utf8', function (err) {
    if (err) {
        return console.log(err)
    }
});