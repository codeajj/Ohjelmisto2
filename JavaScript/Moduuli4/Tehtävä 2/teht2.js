const form = document.getElementById("form")

form.addEventListener("submit", evt=> {
  evt.preventDefault()
  const query = document.getElementById('query').value
  fetch("https://api.tvmaze.com/search/shows?q=" + query)
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.log(error))
})