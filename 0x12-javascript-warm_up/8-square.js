#!/usr/bin/node
const s = Math.floor(Number(process.argv[2]));
if (isNaN(s)) {
  console.log('Missing size');
} else {
  for (let v = 0; v < s; v++) {
    let r = '';
    for (let y = 0; y < s; y++) r += 'X';
    console.log(row);
  }
}
