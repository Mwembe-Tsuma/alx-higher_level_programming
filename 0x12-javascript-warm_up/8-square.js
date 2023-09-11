#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const count = Number(process.argv[2]);

  let i = 0;
  while (i < count) {
    console.log('X'.repeat(x));
    i++;
  }
}
