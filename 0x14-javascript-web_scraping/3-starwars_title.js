#!/usr/bin/node
/*
Script that prints the title of a Star Wars movie
*/
const request = require('request');
request
  .get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (error, response, body) {
    console.log(error || JSON.parse(body).title);
  });
