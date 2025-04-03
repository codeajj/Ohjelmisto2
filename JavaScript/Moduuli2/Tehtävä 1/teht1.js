let kerrat=0, numerot=[];

while(kerrat<5) {
  numerot.push(parseInt(prompt("Anna viisi numeroa ja tulostan ne vastakkaisessa järjestyksessä")));kerrat++;
}

for(let i=0; i<numerot.length; i++) {
  document.querySelector("#target").innerHTML=(numerot[4]+", "+numerot[3]+", "+numerot[2]+", "+numerot[1]+", "+numerot[0]);
}