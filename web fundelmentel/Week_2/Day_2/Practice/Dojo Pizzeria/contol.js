function pizzaOven(crustTypeValue, sauceTypeValue, cheesesValue, toppingsValue) {
    var pizza = {};
    pizza.crustType = crustTypeValue;
    pizza.sauceType = sauceTypeValue;
    pizza.cheeses = cheesesValue;
    pizza.toppings = toppingsValue;
    return pizza;
}
var pizza1 = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
var pizza2 = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
var pizza3 = pizzaOven("thin crust", "pesto", ["provolone"], ["spinach", "tomatoes", "artichokes"]);
var pizza4 = pizzaOven("stuffed crust", "alfredo", ["cheddar", "mozzarella"], ["bacon", "chicken", "garlic"]);

console.log(pizza1.crustType);
console.log(pizza2);
console.log(pizza3);
console.log(pizza4);

function Random index(arr) {
    var index = Math.floor(Math.random() * arr.length);
    return arr[index];
}