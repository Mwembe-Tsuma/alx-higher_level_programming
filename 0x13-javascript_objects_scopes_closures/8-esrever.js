#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length - 1;
  let x = 0;
  while ((len - x) > 0) {
    const temp = list[len];
    list[len] = list[x];
    list[x] = temp;
    x++;
    len--;
  }
  return list;
};
