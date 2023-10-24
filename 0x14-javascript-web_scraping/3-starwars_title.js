#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node your-script.js <movie-id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request(apiUrl + movieId, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
