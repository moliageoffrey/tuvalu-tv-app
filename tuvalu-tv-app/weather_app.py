import streamlit as st
import requests

st.set_page_config(page_title="Tuvalu Weather", layout="centered")

# --- 1. REAL-TIME DATA FETCHING ---
def get_weather():
    # Replace "YOUR_API_KEY" with your actual OpenWeatherMap key
    api_key = "YOUR_API_KEY" 
    city = "Funafuti,TV"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        data = requests.get(url).json()
        return {
            "temp": round(data['main']['temp']),
            "humidity": data['main']['humidity'],
            "wind": data['wind']['speed'],
            "cond": data['weather'][0]['main'],
            "icon": data['weather'][0]['icon']
        }
    except:
        # Fallback if API fails
        return {"temp": 28, "humidity": 80, "wind": 12, "cond": "Partly Cloudy", "icon": "03d"}

w = get_weather()

# --- 2. THE PREMIUM WEATHER CARD ---
st.html(f"""
<style>
    .weather-card {{
        background: linear-gradient(145deg, #1e293b, #0f172a);
        border-radius: 24px;
        padding: 40px;
        color: white;
        font-family: 'Segoe UI', sans-serif;
        border: 1px solid #334155;
        max-width: 450px;
    }}
    .temp-val {{ font-size: 5rem; font-weight: 800; margin: 0; line-height: 1; }}
    .loc-name {{ font-size: 1.5rem; color: #94a3b8; margin-bottom: 5px; }}
    .stat-grid {{ 
        display: grid; 
        grid-template-columns: 1fr 1fr; 
        gap: 20px; 
        margin-top: 30px; 
    }}
    .stat-box {{ 
        background: rgba(255, 255, 255, 0.05); 
        padding: 15px; 
        border-radius: 15px; 
        text-align: center; 
    }}
</style>

<div class="weather-card">
    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
            <p class="loc-name">Funafuti, Tuvalu</p>
            <h1 class="temp-val">{w['temp']}°C</h1>
            <p style="color: #38bdf8; font-weight: 600; margin-top: 10px;">{w['cond']}</p>
        </div>
        <img src="http://openweathermap.org/img/wn/{w['icon']}@4x.png" width="100">
    </div>
    
    <div class="stat-grid">
        <div class="stat-box">
            <small style="color: #64748b; text-transform: uppercase;">Humidity</small><br>
            <span style="font-size: 1.2rem; font-weight: 600;">{w['humidity']}%</span>
        </div>
        <div class="stat-box">
            <small style="color: #64748b; text-transform: uppercase;">Wind</small><br>
            <span style="font-size: 1.2rem; font-weight: 600;">{w['wind']} km/h</span>
        </div>
    </div>
</div>
""")
