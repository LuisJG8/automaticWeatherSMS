import requests
from twilio.rest import Client
import datetime

ACCOUNT_SID = "YOUR ACCOUNT ID"
AUTH_TOKEN = "YOUR AUTH_TOKEN"
TWILIO_PHONE_NUMBER = "YOUR TWILIO PHONE NUMBER"
MY_LINK = "https://api.openweathermap.org/data/2.5/forecast?"
API_KEY = "YOUR WEATHER API KEY"


PARAMETERS = {
    "lat": 89.785080,
    "lon": -23.294712,
    "appid": API_KEY,
    "cnt": 4
}

connection = requests.get(url=MY_LINK, params=PARAMETERS)
print(connection.raise_for_status())
weather_data = connection.json()

print(weather_data["list"])

# weather_number1 = weather_data["list"]["weather"][0]["id"]
# weather_number2 = weather_data["list"]["weather"][0]["id"]
# weather_number3 = weather_data["list"]["weather"][0]["id"]
# weather_number4 = weather_data["list"]["weather"][0]["id"]
# all_weather_numbers = [weather_number1,weather_number2,weather_number3,weather_number4]

will_rain = False
for number in weather_data["list"]:
    new_numbers = number["weather"][0]["id"]
    if new_numbers < 700:
        print("Bring an umbrella")
        will_rain = True
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It is going to rain",
        from_="whatsapp:TWILIO WHATSAPP NUMBER",
        to="whatsapp:WHATSAPP NUMBER"
        )
    print(message.status)