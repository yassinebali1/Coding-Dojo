//Step 1: Review and Edit Variables

var height = 43; // Rider's height in inches
var age = 11;    // Rider's age

//Step 2: Create Conditional to Check if Rider is Taller than 42 Inches

if (height >= 42) {
    console.log("Get on that ride, kiddo!");
} else {
    console.log("Sorry kiddo. Maybe next year.");
}

//Stretch Feature 1: Adjust to Require Both Height and Age

if (height >= 42 && age >= 10) {
    console.log("Get on that ride, kiddo!");
} else {
    console.log("Sorry kiddo. Maybe next year.");
}
//Stretch Feature 2: Adjust to Require Either Height or Age

if (height >= 42 || age >= 10) {
    console.log("Get on that ride, kiddo!");
} else {
    console.log("Sorry kiddo. Maybe next year.");
}
