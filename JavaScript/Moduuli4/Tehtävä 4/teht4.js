const form = document.getElementById("form")

const article = document.querySelector("#element")

const div = document.createElement("div"); div.classList.add("results") // Div
const h2 = document.createElement("h2"); div.appendChild(h2) // Name
const a = document.createElement("a"); div.appendChild(a); a.target="_blank" // URL
const figure = document.createElement("figure"); div.appendChild(figure) // Luon figure kuvaa varten
const img = document.createElement("img"); div.appendChild(img) // Image and alt
const sumDiv = document.createElement("div"); div.appendChild(sumDiv) // Jotta div toimii normaalisti
figure.appendChild(img)
article.appendChild(div)

form.addEventListener("submit", evt=> {
  evt.preventDefault()
  const query = document.getElementById('query').value
  fetch("https://api.tvmaze.com/search/shows?q=" + query)
      .then(response => response.json())
      .then(data => {
        sumDiv.innerHTML = data[0].show.summary
        img.alt = "No image found"
        img.src = data[0].show.image?.medium
            ? data[0].show.image?.medium
            : "https://via.placeholder.com/210x295?text=Not%20Found"
        a.textContent = data[0].show.url
        h2.textContent = data[0].show.name
  })
      .catch(error => console.log(error))
})