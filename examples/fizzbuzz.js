let i = 0;

while(true){
if(i>=100)break;

if(i%3===0&&i%5===0)console.log(`Fizzbuzz`);
 else if(i%3===0)console.log(`Fizz`);
 else if(i%5===0)console.log(`Buzz`);
else console.log(i);

i = i+1;
}