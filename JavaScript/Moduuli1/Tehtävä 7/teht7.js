const dice_amount = prompt('How many dice will I throw?');
diceInt = parseInt(dice_amount);
dicesum = 0;

function Random(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;

}

for (let i = 0; i < diceInt; i++) {
  dicesum = dicesum + Random(1, 6);
  document.querySelector('#target').innerHTML = (dicesum);
}