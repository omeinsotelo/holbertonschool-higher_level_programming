#!/usr/bin/node
/*
Function that returns the reversed version of a list
*/
exports.esrever = function (list) {
  const newlist = [];
  for (let count = list.length - 1; count >= 0; count--) {
    newlist.push(list[count]);
  }
  return newlist;
};
