number = Math.floor(Math.random() * 4)

const username = prompt("Enter your name: ");

if (number === 0) {
    document.querySelector('#target').innerHTML = ("Hey " + username + " your house is Slytherin");
}
else if (number === 1) {
    document.querySelector('#target').innerHTML = ("Hey " + username + " your house is Hufflepuff");
}
else if (number === 2) {
    document.querySelector('#target').innerHTML = ("Hey " + username + " your house is Gryffindor");
}
else if (number === 3) {
    document.querySelector('#target').innerHTML = ("Hey " + username + " your house is Ravenclaw");
}
else {
    document.querySelector('#target').innerHTML = 'VÄÄÄÄÄÄÄÄÄÄÄÄÄRIN!!!!!!!!!';
}