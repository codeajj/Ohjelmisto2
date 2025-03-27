import requests

hakusana = input("Give me a city: ")

pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={hakusana}&appid={"d01e8c6c9527213014a1cbff4c710e10"}&units=metric"

vastaus = requests.get(pyyntö).json()
print(f"Weather in {hakusana} is {vastaus["weather"][0]["description"]} and tempature is {vastaus["main"]["temp"]} C")