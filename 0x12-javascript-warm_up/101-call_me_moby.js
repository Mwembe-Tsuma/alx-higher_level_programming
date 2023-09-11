#!/usr/bin/node

exports.callMeMoby = function (n, theFunction) {
  let i = 0;
  while (i < n) {
    theFunction();
    i++;
  }
};

