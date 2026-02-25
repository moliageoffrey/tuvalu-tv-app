import requests

def get_weather():
    api_key = "YOUR_API_KEY_HERE"
    city = "Funafuti"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    data = requests.get(url).json()
    return {
        "temp": data['main']['temp'],
        "humidity": data['main']['humidity'],
        "wind": data['wind']['speed']
    }
