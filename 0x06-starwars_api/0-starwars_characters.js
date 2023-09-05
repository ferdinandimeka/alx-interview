#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/';

if (process.argv.length > 2) {
  request(`${url}films/${process.argv[2]}/`, (err, res, body) => {
    if (err) {
      console.log(err);
    }

    const characters = JSON.parse(body).characters;
    const characterName = characters.map((character) => {
      return new Promise((resolve, reject) => {
        request(character, (err, res, body) => {
          if (err) {
            reject(err);
          }
          resolve(JSON.parse(body).name);
        });
      });
    });

    Promise.all(characterName)
      .then(names => console.log(names.join('\n')))
      .catch(err => console.log(err));
  });
}
