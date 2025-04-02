const prime = prompt("Prime number check.")
primeINT = parseInt(prime)

if (primeINT > 2) {
    document.querySelector("#target").innerText = ("Error")
}

if (primeINT % 1 === 0) {
    if (primeINT % 3 !== 0 && primeINT % 2 !== 0) {
        document.querySelector("#target").innerText = ("This is a prime number.")
    }
    else {
        document.querySelector("#target").innerText = ("This isn't a prime number.")
    }
}