#!/usr/bin/node
/*
Script that prints a square
*/
if (isNaN(process.argv[2])) {
  console.log('Missing size');
}
let i = 0;
while (i < process.argv[2]) {
  console.log('X'.repeat(process.argv[2]));
  i++;
}
