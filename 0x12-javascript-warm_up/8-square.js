#!/usr/bin/node
const squaresize = Math.floor(Number(process.argv[2]));
if (isNaN(squaresize)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < squaresize; r++) {
    let squarerow = '';
    for (let i = 0; i < squaresize; i++) 
      squarerow += 'X';
    console.log(squarerow);
  }
}
