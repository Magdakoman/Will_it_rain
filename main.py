import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


account_sid = "AC6ef99dbbc26c26c5c9ec7a7ca63eb978"
auth_token = "b10edc9a48e77a2b1326ed3955c64628"


API_KEY = "6641e64dfd422b338cfaf649593fee23"
MY_LAT = 54.352024
MY_LNG = 18.646639
parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
# hourly = weather_data['hourly'][0]['weather'][0]['id']
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an umbrella",
        from_="+17572319415",
        to="+48504931650"
    )
    print(message.status)