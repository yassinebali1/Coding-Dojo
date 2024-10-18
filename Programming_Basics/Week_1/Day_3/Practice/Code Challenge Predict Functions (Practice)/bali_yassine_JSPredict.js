//predict 1 :When the function myBirthYearFunc() is called, the console.log following message: I was born in 1980

function myBirthYearFunc(){
    console.log("I was born in" + 1980);
}
myBirthYearFunc();

//predict 2 : When the function myBirthYearFunc() is called, the console.log following message: I was born in 1980

function myBirthYearFunc(birthYearInput){
    console.log("I was born in" + birthYearInput);
}
myBirthYearFunc(1980);

//predict 2 :
function add(num1, num2){
    console.log("Summing Numbers!");
    console.log("num1 is: " + num1); // 10
    console.log("num2 is: " + num2); //20
    var sum = num1 + num2; 
    console.log(sum);  // 30
}
add(10, 20);
