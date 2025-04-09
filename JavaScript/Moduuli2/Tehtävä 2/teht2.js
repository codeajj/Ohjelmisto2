vierasmäärä = +prompt("Kuinka monta vierasta?")
nimet = []
for (let i = 1; i-1 < vierasmäärä; i++) {
  nimi = prompt("Vieraan nimi")
  nimet += ("<ol>" + "Nimi: "+nimi+" Numero: " +i+"</ol>")
}

document.querySelector('#target').innerHTML = nimet