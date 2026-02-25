import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="Tuvalu Weather Station", layout="centered")

# 2. Weather Fetching Logic
def get_tuvalu_weather():
    api_key = "YOUR_API_KEY" # <--- PASTE YOUR KEY HERE
    city = "Funafuti,TV"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        return {
            "temp": round(data['main']['temp']),
            "humidity": data['main']['humidity'],
            "wind": data['wind']['speed'],
            "visibility": data.get('visibility', 0) // 1000,
            "condition": data['weather'][0]['main'],
            "icon": data['weather'][0]['icon']
        }
    except:
        # Fallback data if API fails
        return {"temp": 28, "humidity": 80, "wind": 12, "visibility": 10, "condition": "Cloudy", "icon": "03d"}

w = get_tuvalu_weather()

# 3. Custom CSS for the "Premium Dark" Look
st.markdown("""
<style>
    .stApp { background-color: #000000; } /* Dark background for the whole app */
    .weather-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        border-radius: 24px;
        padding: 40px;
        color: white;
        font-family: 'Inter', sans-serif;
        border: 1px solid #334155;
    }
    .temp-val { font-size: 5rem; font-weight: 800; margin: 0; line-height: 1; }
    .loc-name { font-size: 1.8rem; color: #94a3b8; }
    .stat-box { background: #1e293b; padding: 15px; border-radius: 15px; text-align: center; }
    .stat-label { color: #64748b; font-size: 0.8rem; text-transform: uppercase; }
    .stat-num { font-size: 1.1rem; font-weight: 600; }
</style>
""", unsafe_html=True)

# 4. Display the Card
st.markdown(f"""
<div class="weather-card">
    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
            <p class="loc-name">Funafuti, Tuvalu</p>
            <h1 class="temp-val">{w['temp']}°C</h1>
            <p style="color: #38bdf8; font-weight: 600;">{w['condition']}</p>
        </div>
        <img src="http://openweathermap.org/img/wn/{w['icon']}@4x.png" width="100">
    </div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 30px;">
        <div class="stat-box">
            <p class="stat-label">Humidity</p>
            <p class="stat-num">{w['humidity']}%</p>
        </div>
        <div class="stat-box">
            <p class="stat-label">Wind Speed</p>
            <p class="stat-num">{w['wind']} km/h</p>
        </div>
        <div class="stat-box">
            <p class="stat-label">Visibility</p>
            <p class="stat-num">{w['visibility']} km</p>
        </div>
        <div class="stat-box">
            <p class="stat-label">Region</p>
            <p class="stat-num">Oceania</p>
        </div>
    </div>
</div>
""", unsafe_html=True)
