#!/usr/bin/node
/*
Script that prints the first argument can be converted to an integer
*/
if (!parseInt(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + process.argv[2]);
}
