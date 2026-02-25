import streamlit as st
import requests

st.set_page_config(page_title="Tuvalu Weather Station", layout="centered")

def get_weather():
    try:
        api_key = st.secrets["OPENWEATHER_API_KEY"]
        city = "Funafuti,TV"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            return {
                "temp": round(data['main']['temp']),
                "hum": data['main']['humidity'],
                "wind": round(data['wind']['speed'] * 3.6, 1),
                "vis": data.get('visibility', 0) / 1000,
                "cond": data['weather'][0]['main'],
                "icon": data['weather'][0]['icon']
            }
    except:
        return None
    return None

w = get_weather()

if w:
    # 1. Define the Styles
    style = """
    <style>
        .weather-card {
            background: linear-gradient(145deg, #1e293b, #0f172a);
            border-radius: 24px;
            padding: 30px;
            color: white;
            font-family: sans-serif;
            border: 1px solid #334155;
            max-width: 450px;
            margin: auto;
        }
        .temp-val { font-size: 5rem; font-weight: 800; margin: 0; }
        .stat-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 25px; }
        .stat-box { background: rgba(255,255,255,0.05); padding: 12px; border-radius: 12px; text-align: center; }
    </style>
    """

    # 2. Define the Card Content (Using .format for safety)
    card_html = """
    <div class="weather-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <p style="color: #94a3b8; margin:0;">Funafuti, Tuvalu</p>
                <h1 class="temp-val">{temp}°C</h1>
                <p style="color: #38bdf8; font-weight: 600; margin:0;">{cond}</p>
            </div>
            <img src="http://openweathermap.org/img/wn/{icon}@4x.png" width="100">
        </div>
        <div class="stat-grid">
            <div class="stat-box"><small style="color: #64748b;">HUMIDITY</small><br><b>{hum}%</b></div>
            <div class="stat-box"><small style="color: #64748b;">WIND</small><br><b>{wind} km/h</b></div>
            <div class="stat-box"><small style="color: #64748b;">VISIBILITY</small><br><b>{vis} km</b></div>
            <div class="stat-box"><small style="color: #64748b;">REGION</small><br><b>Oceania</b></div>
        </div>
    </div>
    """.format(temp=w['temp'], cond=w['cond'], icon=w['icon'], hum=w['hum'], wind=w['wind'], vis=w['vis'])

    # 3. Render
    st.html(style + card_html)
else:
    st.warning("Cloud is connecting to OpenWeatherMap... Please ensure your API Key is active.")
