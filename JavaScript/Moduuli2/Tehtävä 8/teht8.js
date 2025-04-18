const name_list = ["Johnny", "DeeDee", "Joey", "Marky"]

concat(name_list)
function concat() {
  for (let i = 0; i < name_list.length; i++) {
    name += name_list[i]
  }
}

document.querySelector('#target').innerHTML = name