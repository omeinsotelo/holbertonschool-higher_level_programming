#!/usr/bin/node
/*
Script that prints the number of movies where the character “Wedge Antilles” is present.
*/
const request = require('request');
request
  .get(process.argv[2], (err, response, body) => {
    if (!err) {
      let cnt = 0;
      const results = JSON.parse(body).results;
      results.forEach(people => {
        if (people.characters.find(function (character) { return character.endsWith('/18/'); })) cnt++;
      });
      console.log(cnt);
    }
  });
