#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const arr = [];

  for (let i = 0; i < args.length; i++) {
    arr.push(parseInt(args[i]));
  }
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
