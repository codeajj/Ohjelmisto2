const leapyear = prompt("Give me a year and I will tell you if it is a leap year: ")

    if (leapyear % 4 === 0) {
            if (leapyear % 4 === 0 && leapyear % 100 === 0) {
                if (leapyear % 400 === 0) {
                    console.log("Tämä on karkausvuosi!")
                } else console.log("Tämä ei ole karkausvuosi!")
            } else console.log("Tämä on karkausvuosi!")
        } else console.log("Tämä ei ole karkausvuosi!")