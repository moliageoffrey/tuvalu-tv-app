import streamlit as st
import requests

st.set_page_config(page_title="Tuvalu Weather", layout="centered")

# --- 1. DATA FETCHING ---
def get_weather():
    # Placeholder data - replace with API logic later
    return {"temp": 28, "humidity": 78, "wind": 15, "vis": 10, "cond": "Cloudy", "icon": "03d"}

w = get_weather()

# --- 2. THE CLEAN WEATHER CARD ---
# We use st.html (new in Streamlit) which is safer for CSS/HTML blocks
st.html(f"""
<style>
    .weather-card {{
        background: linear-gradient(145deg, #1e293b, #0f172a);
        border-radius: 20px;
        padding: 30px;
        color: white;
        font-family: sans-serif;
        border: 1px solid #334155;
        max-width: 400px;
    }}
    .temp-big {{ font-size: 4rem; font-weight: bold; margin: 0; }}
    .stats-grid {{ 
        display: grid; 
        grid-template-columns: 1fr 1fr; 
        gap: 15px; 
        margin-top: 20px; 
    }}
    .stat-item {{ background: #1e293b; padding: 10px; border-radius: 10px; text-align: center; }}
</style>

<div class="weather-card">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <p style="color: #94a3b8; margin: 0;">Funafuti, Tuvalu</p>
            <h1 class="temp-big">{w['temp']}°C</h1>
            <p style="color: #38bdf8; margin: 0;">{w['cond']}</p>
        </div>
        <img src="http://openweathermap.org/img/wn/{w['icon']}@2x.png" width="80">
    </div>
    <div class="stats-grid">
        <div class="stat-item">
            <small style="color: #64748b;">HUMIDITY</small><br>
            <b>{w['humidity']}%</b>
        </div>
        <div class="stat-item">
            <small style="color: #64748b;">WIND</small><br>
            <b>{w['wind']} km/h</b>
        </div>
    </div>
</div>
""")
