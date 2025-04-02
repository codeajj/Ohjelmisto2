const dice = parseInt(prompt ("How many dice will I throw?"))
const sum = parseInt(prompt ("What sum do you want?"))

let how_many = 0, wanted_sum = 0

function dice_throw() {
    return Math.floor(Math.random() * (6 - 1 + 1)) + 1;
}

for (let i = 0; i < 10000; i++) {
    wanted_sum = 0
    for (let j = 0; j < dice; j++) {
        wanted_sum += dice_throw();
    }
    if (wanted_sum === sum) {
        how_many += 1
    }
}

let procentage = how_many / 10000 * 100
document.querySelector("#target").innerHTML = (procentage.toFixed(2) + "%")