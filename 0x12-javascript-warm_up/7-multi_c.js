#!/usr/bin/node
const y = Math.floor(Number(process.argv[2]));
if (isNaN(y)) {
  console.log('Missing number of occurrences');
} else {
  for (let z = 0; z < y; z++) {
    console.log('C is fun');
  }
}
