#!/usr/bin/node

const args = process.argv.slice(2);
const x = args[0];
const xInt = parseInt(x);

if (isNaN(xInt)) {
  console.log('Missing number of occurrences');
} else if (xInt > 0) {
  for (let i = 0; i < xInt; i++) {
    console.log('C is fun');
  }
}
