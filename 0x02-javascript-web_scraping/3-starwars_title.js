#!/usr/bin/node

const request = require('request');
const whatMovie = argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/:id' + whatMovie;

request(URL, function (err, response, body) {
    if (err) {
        console.log(err)
    } else {
        const json = JSON.parse(body);
        console.log(json.title);
    }
});