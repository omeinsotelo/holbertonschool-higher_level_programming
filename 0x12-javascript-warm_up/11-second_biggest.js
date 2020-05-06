#!/usr/bin/node
/*
Script that searches the second biggest integer in the list of arguments.
*/
function secondMax (a) {
  if (process.argv.length <= 3) {
    return 0;
  } else {
    a.sort((x, y) => x - y);
    a.pop();
    return (a.pop());
  }
}
console.log(secondMax(process.argv));
