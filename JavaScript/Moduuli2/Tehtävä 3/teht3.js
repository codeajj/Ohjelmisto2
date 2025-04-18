koirat = []
for (let i = 6; i > 0; i--) {
  nimi = prompt("Anna minulle " +i+ " koiran nimet")
  koirat.push("<ul>" + "Koira: "+nimi+ "</ul>")
}
koirat.sort((a,b) => a-b);
koirat.reverse();

document.querySelector('#target').innerHTML = koirat.join("\n")