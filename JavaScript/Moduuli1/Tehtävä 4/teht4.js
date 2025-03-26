function getHouse() {
  const minCeiled = Math.ceil(1);
  const maxFloored = Math.floor(4);
  return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled);
}

const username = prompt("Enter your name: ");

if (getHouse() === 1) {
    console.log("Hey " + username + " your house is Slytherin");
}
else if (getHouse() === 2) {
    console.log("Hey " + username + " your house is Hufflepuff");
}
else if (getHouse() === 3) {
    console.log("Hey " + username + " your house is Gryffindor");
}
else if (getHouse() === 4) {
    console.log("Hey " + username + " your house is Ravenclaw");
}