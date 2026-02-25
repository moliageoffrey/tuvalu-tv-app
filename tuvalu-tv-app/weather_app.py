import streamlit as st
import requests

st.set_page_config(page_title="Tuvalu Weather Station", layout="centered")

def get_weather():
    api_key = st.secrets["OPENWEATHER_API_KEY"]
    # We use Funafuti's coordinates for better accuracy with Alerts
    lat, lon = -8.5211, 179.1962 
    
    # Using the One Call 3.0 URL (Requires subscription on OWM site)
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Visibility is in meters, we convert to KM
        vis_km = data['current'].get('visibility', 0) / 1000
        
        # Alerts is a list; we grab the first one if it exists
        alert_msg = "No Active Alerts"
        alert_style = "color: #10b981;" # Green
        
        if 'alerts' in data:
            alert_msg = data['alerts'][0]['event']
            alert_style = "color: #ef4444; font-weight: bold; animation: blinker 1.5s linear infinite;" # Red + Blinking

        return {
            "temp": round(data['current']['temp']),
            "humidity": data['current']['humidity'],
            "wind": round(data['current']['wind_speed'] * 3.6, 1),
            "vis": vis_km,
            "cond": data['current']['weather'][0]['main'],
            "icon": data['current']['weather'][0]['icon'],
            "alert": alert_msg,
            "alert_style": alert_style
        }
    except:
        return None

w = get_weather()

if w:
    st.html(f"""
    <style>
        @keyframes blinker {{ 50% {{ opacity: 0; }} }}
        .weather-card {{
            background: linear-gradient(145deg, #1e293b, #0f172a);
            border-radius: 24px;
            padding: 30px;
            color: white;
            font-family: 'Inter', sans-serif;
            border: 1px solid #334155;
            max-width: 450px;
        }}
        .temp-val {{ font-size: 5rem; font-weight: 800; margin: 0; }}
        .stat-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 25px; }}
        .stat-box {{ background: rgba(255,255,255,0.05); padding: 12px; border-radius: 12px; text-align: center; }}
        .alert-box {{ 
            margin-top: 20px; 
            padding: 10px; 
            background: rgba(0,0,0,0.3); 
            border-radius: 10px; 
            text-align: center; 
            border: 1px solid #334155;
        }}
    </style>

    <div class="weather-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <p style="color: #94a3b8; margin:0;">Funafuti, Tuvalu</p>
                <h1 class="temp-val">{w['temp']}°C</h1>
                <p style="color: #38bdf8; font-weight: 600;">{w['cond']}</p>
            </div>
            <img src="http://openweathermap.org/img/wn/{w['icon']}@4x.png" width="100">
        </div>
        
        <div class="stat-grid">
            <div class="stat-box">
                <small style="color: #64748b;">HUMIDITY</small><br>
                <span>{w['humidity']}%</span>
            </div>
            <div class="stat-box">
                <small style="color: #64748b;">WIND</small><br>
                <span>{w['wind']} km/h</span>
            </div>
            <div class="stat-box">
                <small style="color: #64748b;">VISIBILITY</small><br>
                <span>{w['vis']} km</span>
            </div>
            <div class="stat-box">
                <small style="color: #64748b;">UV INDEX</small><br>
                <span>High</span>
            </div>
        </div>

        <div class="alert-box">
            <small style="color: #64748b;">OFFICIAL ALERTS</small><br>
            <span style="{w['alert_style']}">{w['alert']}</span>
        </div>
    </div>
    """)
