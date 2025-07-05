import requests # type: ignore
from twilio.rest import Client

API_KEY = "ae469bfdf461a2f56d78d210ae620fd7"
LATITUDE = 47.024959
LONGITUDE = 28.793120
URL = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = 'AC69bd9af2af319a66940e6fea8215efe8'
auth_token = '4619bf99faced767c7a1774eefbb58f6'

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 5
}

response = requests.get(URL, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
min_temp = 1000
max_temp = -1000
content = ""

# Sigur că există indexul 2
middle_day_temp = data["list"][min(2, len(data["list"])-1)]["main"]["temp"]

for n in range(len(data["list"])):
    weather_id = data["list"][n]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
    if data["list"][n]["main"]["temp_min"] < min_temp:
        min_temp = data["list"][n]["main"]["temp_min"]
    if data["list"][n]["main"]["temp_max"] > max_temp:
        max_temp = data["list"][n]["main"]["temp_max"]

if will_rain:
    content += "It's going to rain today. Remember to take an umbrella with you.\n"
content += f"Middle day temperature: {middle_day_temp}°C\n"
content += f"Minimum temperature: {min_temp}°C\n"
content += f"Maximum temperature: {max_temp}°C\n"


client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='+15168425114',
    body=content,
    to='+37367617223'
)
print(message.status)
