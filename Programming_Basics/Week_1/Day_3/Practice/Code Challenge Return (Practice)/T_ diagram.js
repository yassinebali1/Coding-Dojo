//Code Snippet 1:

function hello() {
    console.log('hello'); //afficher hello
}
hello(); // is called
console.log('Dojo'); // afficher dojo

//Code Snippet 2:

function hello() {
    console.log('hello');
    return 15;
}
var result = hello();
console.log('result is', result); // afficher "result is 15 "



//Code Snippet 3:

function numPlus(num) {
    console.log('num is', num); // numPlus(3) num=3
    return num+15;
}
var result = numPlus(3); 
console.log('result is', result); //afficher result is 18

//Code Snippet 4:
var num = 15;
console.log(num); //15
function logAndReturn(num){
   console.log(num);   
   return num;
}
var result = logAndReturn(10);
console.log(result);//10
console.log(num);//15

//Code Snippet 5
var num = 15;
console.log(num); //15
function timesTwo(num){
   console.log(num);   
   return num*2;
}
var result = timesTwo(10);
console.log(result); //afficher 20
console.log(num); //afficher 15

//Code Snippet 6

function timesTwoAgain(num) {
    console.log('num is', num); // afficher num is 3
    var y = num*2; // y = 3 * 2 (y becomes 6)
    return y; // (returns 6)
}
var result = timesTwoAgain(3) + timesTwoAgain(5);
console.log('result is', result); //result is 16

//Code Snippet 6

function timesTwoAgain(num) {
    console.log('num is', num);//num is 3
    var y = num*2;
    return y;
}
var result = timesTwoAgain(3) + timesTwoAgain(5);
console.log('result is', result);//result is 16


//Code Snippet 8

function printSumNums(num1, num2) {
    console.log(num1);  //afficher 2 
    return num1+num2;
 }
 console.log(printSumNums(2,3)) // afficher3
 console.log(printSumNums(3,5))// afficher 8
 
 