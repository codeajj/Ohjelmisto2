const start_year = prompt('Give me a starting year');
startINT = parseInt(start_year);
const end_year = prompt('Give me a ending year');
endINT = parseInt(end_year);

years = [];

function leapyears(start, end) {
  for (i = start; i <= end; i++) {
    if (i % 4 === 0 && (i % 100 !== 0 || i % 400 === 0)) {
      years.push(i);
    }
  }
}

leapyears(startINT, endINT);

if (years.length > 0) {
  document.querySelector('#target').innerHTML = years.join('<br>');
} else {
  document.querySelector('#target').innerHTML = 'No leapyears.';
}