const form = document.getElementById("form")

form.addEventListener("submit", evt=> {
  evt.preventDefault()
  const query = document.getElementById('query').value
  fetch("https://api.chucknorris.io/jokes/search?query=" + query).
      then(response => response.json()).
      then(data => {
        document.querySelector("p").innerHTML = data.result[0].value
      })
      .catch(error => console.log(error))
})