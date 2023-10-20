import requests
from datetime import datetime


parameters = {
    "lat":40.982383 ,
    "lng":28.893372,
    "formatted":0
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])

print(sunset.split("T")[1].split(":")[0])


time_now = datetime.now()

print(time_now)
