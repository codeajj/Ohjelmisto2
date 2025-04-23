const img = document.querySelector("#target")
const over = document.getElementById("trigger")

over.addEventListener("mouseover", () => {
  img.src = "img/picB.jpg"
});

over.addEventListener("mouseleave", () => {
  img.src = "img/picA.jpg"
});
