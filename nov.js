function fib(n){
if(n<2)return n;
return fib(n-1)+fib(n-2);
}

let results = fib(10);

console.log(results)
