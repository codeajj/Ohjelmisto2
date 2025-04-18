function Random(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;

}
let dices = []
let dice = 0;

number = +prompt("I will throw a d20 untill I get your required number");

while (dice !== number) {
  dice = Random(1, 20);
  dices.push("<ul>" + dice + "</ul>");
}

if (dice === number) {
  document.querySelector('#target').innerHTML = dices.join("\n");
}