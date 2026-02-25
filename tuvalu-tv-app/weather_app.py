import streamlit as st
import requests

st.set_page_config(page_title="Tuvalu Weather Station", layout="centered")

def get_weather():
    # Safely get your key from Streamlit Secrets
    try:
        api_key = st.secrets["OPENWEATHER_API_KEY"]
    except:
        st.error("API Key not found in Secrets!")
        return None
        
    # Using the standard FREE 2.5 API (Most reliable for new accounts)
    city = "Funafuti,TV"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            # Visibility is in meters, convert to KM
            vis_km = data.get('visibility', 0) / 1000
            wind_speed = round(data['wind']['speed'] * 3.6, 1) # km/h
            
            # --- SMART ALERT LOGIC ---
            # Since the free API doesn't give text alerts, we create them based on conditions
            alert_msg = "Conditions: Normal"
            alert_style = "color: #10b981;" # Green
            
            if wind_speed > 40:
                alert_msg = "⚠️ High Wind Warning"
                alert_style = "color: #ef4444; font-weight: bold; animation: blinker 1.5s linear infinite;"
            elif vis_km < 2:
                alert_msg = "⚠️ Low Visibility / Heavy Rain"
                alert_style = "color: #f59e0b; font-weight: bold;"

            return {
                "temp": round(data['main']['temp']),
                "humidity": data['main']['humidity'],
                "wind": wind_speed,
                "vis": vis_km,
                "cond": data['weather'][0]['main'],
                "icon": data['weather'][0]['icon'],
                "alert": alert_msg,
                "alert_style": alert_style
            }
    except Exception as e:
        st.write(f"Connection Error: {e}")
        return None
    return None

w = get_weather()

# If the data exists, show the card. If not, show a helpful message.
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
            margin: auto;
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
                <p style="color: #38bdf8; font-weight:
