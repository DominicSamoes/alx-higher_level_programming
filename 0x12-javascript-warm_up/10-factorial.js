#!/usr/bin/node
function factorial (n) {
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
  if (n === 0 || isNaN(n))
       return 1;
  else
       return factorial(n - 1) * n;
      
}

console.log(factorial(Number(process.argv[2])));
