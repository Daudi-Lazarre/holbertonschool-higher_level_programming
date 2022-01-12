#!/usr/bin/node

const request = require('request');
const whatMovie = argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/:id' + whatMovie;

request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      const json = JSON.parse(body);
      console.log(json.title);
    }
  });