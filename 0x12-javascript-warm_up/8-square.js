#!/usr/bin/node

const args = process.argv.slice(2);
const size = args[0];
const sizeInt = parseInt(size);
let square = '';

if (isNaN(sizeInt)) {
  console.log('Missing size');
} else if (sizeInt > 0) {
  for (let i = 0; i < sizeInt; i++) {
    square += 'X';
  }
  for (let j = 0; j < sizeInt; j++) {
    console.log(square);
  }
}
