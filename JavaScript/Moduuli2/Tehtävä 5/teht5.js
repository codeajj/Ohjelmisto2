let numero = 0
numerot = []
let onko = true;

while (onko === true) {
  numero = +prompt("Kysyn numeroita kunnes annat aikasemman numeron");
  if (numerot.includes(numero)) {
    onko = false;
  }
  else numerot.push(numero);
}

numerot.sort((a,b) => a-b);
console.log(numerot);
document.querySelector("#target").innerHTML = "Vastaus konsolissa."