// Team Blue Duck: Zhao Yu Lin, Sean Ging, Patrick Ging
// SoftDev
// K27; Basic functions in JavaScript
// 2022-02-04



function fact(n){
  if(n <= 1)
  return 1;
  return n * fact(n - 1);
}

function fib(n){
  if(n<=  1)
  return n;
  return fib(n - 1) + fib(n - 2);
}
