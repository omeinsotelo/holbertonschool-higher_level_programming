#!/usr/bin/node
/*
Script that computes and prints a factorial
*/
function factorial (numF) {
  if (isNaN(parseInt(numF))) {
    return 1;
  } else if (parseInt(numF) === 0) {
    return 1;
  } else {
    return parseInt(numF) * factorial(parseInt(numF) - 1);
  }
}
console.log(factorial(process.argv[2]));
