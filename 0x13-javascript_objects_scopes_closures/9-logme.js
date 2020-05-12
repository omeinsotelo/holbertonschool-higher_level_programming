#!/usr/bin/node
/*
Function prints number of arguments already printed and the new argument value
*/
let count = 0;
exports.logMe = function (item) {
  console.log('%d: %s', count, item);
  count++;
};
