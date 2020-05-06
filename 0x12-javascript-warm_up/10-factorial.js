#!/usr/bin/node
/*
Script that computes and prints a factorial
*/
function factorial (factorial) {
  if (isNaN(parseInt(factorial))) {
    return 1;
  } else if (parseInt(factorial) === 0) {
    return 1;
  } else {
    return parseInt(factorial) * factorial(parseInt(factorial) - 1);
  }
}
console.log(factorial(process.argv[2]));
