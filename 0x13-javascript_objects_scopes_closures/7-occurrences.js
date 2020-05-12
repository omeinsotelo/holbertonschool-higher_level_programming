#!/usr/bin/node
/*
Function that returns the number of occurrences in a list:
*/
exports.nbOccurences = function (list, searchElement) {
  let nbO = 0;
  for (let cont = 0; cont < list.length; cont++) {
    if (list[cont] === searchElement) {
      nbO++;
    }
  }
  return (nbO);
};
