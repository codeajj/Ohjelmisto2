let numero = 0
numerot = []

do {
  numero = +prompt("Kysyn numeroita kunnes annat nollan!");
  if (numero > 0) {
    numerot.push(numero);
  }
} while (numero !== 0);

numerot.sort((a,b) => a-b);
numerot.reverse();
console.log(numerot);
document.querySelector("#target").innerHTML = "Vastaus konsolissa."