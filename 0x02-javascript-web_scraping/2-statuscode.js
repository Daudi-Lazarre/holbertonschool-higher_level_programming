#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const URL = argv[2];

request(URL, function (err, response) {
    if (err) {
        console.error('error:', error)
    } else {
        console.log(`code: ${response.statusCode}`);
    }
});
