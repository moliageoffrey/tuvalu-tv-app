import requests

def get_weather():
    api_key = "e57728a01bb0517612bda589671f886c"
    city = "Funafuti"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    data = requests.get(url).json()
    return {
        "temp": data['main']['temp'],
        "humidity": data['main']['humidity'],
        "wind": data['wind']['speed']
    }
