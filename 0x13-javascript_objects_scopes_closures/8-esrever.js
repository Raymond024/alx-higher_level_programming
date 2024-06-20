#!/usr/bin/node
exports.esrever = function (list) {
  let leng = list.length - 1;
  let x = 0;
  while ((len - x) > 0) {
    const auxi = list[leng];
    list[leng] = list[x];
    list[x] = auxi;
    x++;
    leng--;
  }
  return list;
};
