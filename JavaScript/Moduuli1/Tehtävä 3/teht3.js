const number1 = prompt("Give me a number: ");
const number2 = prompt("Give me another number:");
const number3 = prompt("Give me a third number: ");

sum = parseInt(number1) + parseInt(number2) + parseInt(number3);
average = sum / 3;
product = number1 * number2 * number3;

document.querySelector('#target').innerHTML = ("The sum of your numbers is " + sum + ", the average is " + average + " and the product is " + product)