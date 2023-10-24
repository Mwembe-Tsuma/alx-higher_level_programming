#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: Status Code ${response.statusCode}`);
  } else {
    try {
      const movieData = JSON.parse(body);
      const characterUrls = movieData.characters;
      const fetchCharacterDetails = (index) => {
        if (index < characterUrls.length) {
          request(characterUrls[index], (charError, charResponse, charBody) => {
            if (charError) {
              console.error(charError);
            } else if (charResponse.statusCode !== 200) {
              console.error(`Error: Status Code ${charResponse.statusCode}`);
            } else {
              const characterData = JSON.parse(charBody);
              console.log(characterData.name);
              fetchCharacterDetails(index + 1);
            }
          });
        }
      };
      fetchCharacterDetails(0);
    } catch (parseError) {
      console.error('Error parsing API response:', parseError);
    }
  }
});
