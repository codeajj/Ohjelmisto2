const answer = confirm('Should I calculate root?');

if (answer === true) {
  const number = prompt('Give me a number: ');
  numberINT = parseInt(number);
  square = Math.sqrt(numberINT);
  document.querySelector('#target').innerHTML = ('Square root of ' + numberINT +
      ' is ' + square);
} else if (answer === false) {
  document.querySelector(
      '#target').innerHTML = ('The square root is not calculated');
}

if (numberINT <= 0) {
  document.querySelector(
      '#target').innerHTML = ('Cannot calculate a negative number or zero');
}