#!/usr/bin/node

const args = process.argv.slice(2);

/*
    * convert arguments to integer
    * By using map method to apply the parseInt function
    * To the each element of the original array
    * creates a new array.
    * */

const intArg = parseInt(args[0]);

if (isNaN(intArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + intArg);
}
