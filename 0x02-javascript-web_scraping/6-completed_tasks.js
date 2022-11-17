#!/usr/bin/node
const argv = process.argv;
const URL = argv[2];
const request = require('request');

request(URL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const rbody = JSON.parse(body);
    const dictionary = {};
    for (const x of rbody) {
      if (x.completed === true) {
        if (dictionary[x.userId] === undefined) {
          dictionary[x.userId] = 0;
        }
        dictionary[x.userId] += 1;
      }
    }
    console.log(dictionary);
  }
});
