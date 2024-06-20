#!/usr/bin/node
/*
    * process.argv is an array where:
    * - The first element is the path to Node.js executable
    * - The second is the path to script file.
    * - The rest are the command line arguments
    */
const args = process.argv.slice(2);
// ignores the first two elements in the process.argv array.

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
