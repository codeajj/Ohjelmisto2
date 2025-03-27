const leapyear = prompt("Give me a year and I will tell you if it is a leap year: ")

    if (leapyear % 4 === 0) {
            if (leapyear % 4 === 0 && leapyear % 100 === 0) {
                if (leapyear % 400 === 0) {
                    document.querySelector('#target').innerHTML = ("Tämä on karkausvuosi!")
                } else document.querySelector('#target').innerHTML = ("Tämä ei ole karkausvuosi!")
            } else document.querySelector('#target').innerHTML = ("Tämä on karkausvuosi!")
        } else document.querySelector('#target').innerHTML = ("Tämä ei ole karkausvuosi!")