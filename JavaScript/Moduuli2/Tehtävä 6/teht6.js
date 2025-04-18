function Random() {
  return Math.floor(Math.random() * (6 - 1 + 1)) + 1;

}
let dices = []
let dice = 0;

while (dice !== 6) {
  dice = Random();
  dices.push("<ul>" + dice + "</ul>");
}

if (dice === 6) {
  document.querySelector('#target').innerHTML = dices.join("\n");
}