#!/usr/bin/node

const request = require('request');
const whatMovie = argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/:id' + whatMovie;

request(url, function (errorId, response, body) {
    if (errorId) {
      console.log(errorId);
    } else {
      const json = JSON.parse(body);
      console.log(json.title);
    }
  });