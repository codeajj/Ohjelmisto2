const number_list = [1, 2 ,3 , 4, 5, 6, 7, 8, 9, 10]
const even_list = []

even(number_list)
function even(number_list) {
  for (let i = 0; i < number_list.length; i++) {
    if (number_list[i] % 2 === 0) {
      even_list.push(number_list[i])
    }
  }
}

document.querySelector('#target').innerHTML = even_list.join('\n');