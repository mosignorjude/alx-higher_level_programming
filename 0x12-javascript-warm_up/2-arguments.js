#!/usr/bin/node
/*
    * process.argv is an array where:
    * - The first argument is the path to Node.js executable
    * - The 2nd is the path to script file.
    * - The rest are the command line arguments
    */
const args = process.argv.slice(2);
// ignores the first argument that runs the scripts

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
