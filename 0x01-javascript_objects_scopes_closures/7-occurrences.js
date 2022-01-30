#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let x = 0;

  for (const item of list) {
    if (item === searchElement) {
      x++;
    }
  }

  return x;
};
