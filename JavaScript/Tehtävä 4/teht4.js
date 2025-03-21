function getHouse() {
  return Math.random() * (4 - 1) + 1;
}

const username = prompt("Enter your name: ");

if (getHouse() >= 1 || getHouse() > 2) {
    console.log("Hey " + username + " your house is Slytherin");
}
else if (getHouse() >= 2 || getHouse() > 3) {
    console.log("Hey " + username + " your house is Hufflepuff");
}
else if (getHouse() >= 3 || getHouse() > 4) {
    console.log("Hey " + username + " your house is Gryffindor");
}
else if (getHouse() === 4 || getHouse() < 3) {
    console.log("Hey " + username + " your house is Ravenclaw");
}