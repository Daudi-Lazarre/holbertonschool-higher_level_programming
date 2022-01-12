#!/usr/bin/node

const request = require('request');
const whatMovie = argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/' + whatMovie[2] + '/';

request(URL, function (err, response, body) {
    if (errorId) {
        console.log(errorId)
    } else {
        const json = JSON.parse(body);
        console.log(json.title);
    }
});