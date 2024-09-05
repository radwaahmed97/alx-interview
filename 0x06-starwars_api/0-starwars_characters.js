#!/usr/bin/node
/**
 * script that prints all characters of a Star Wars movie
 * @param {String} url - site url
 * @returns {Promise}  - promise resolved with json response and reject with error
 */
function createRequest (url) {
  const request = require('request');
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body));
    });
  });
}

/**
 * Entry point - pushes requests to Star Wars API
 */
async function main () {
  const args = process.argv;

  if (args.length < 3) return;

  const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
  const movie = await createRequest(movieUrl);

  if (movie.characters === undefined) return;
  for (const characterUrl of movie.characters) {
    const character = await createRequest(characterUrl);
    console.log(character.name);
  }
}

main();
