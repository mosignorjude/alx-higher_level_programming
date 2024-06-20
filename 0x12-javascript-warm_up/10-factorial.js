#!/usr/bin/node

function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

const args = process.argv.slice(2);
let n = parseInt(args[0]);
if (isNaN(n)) {
  n = 0;
}
console.log(factorial(n));
