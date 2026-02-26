import streamlit as st
import requests

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Tuvalu TV Hub", layout="wide", page_icon="🇹🇻")

# 2. THE "CLEAN LOOK" CSS
st.markdown("""
    <style>
        /* Hide all Streamlit branding */
        footer {display: none !important;}
        header {visibility: hidden;}
        [data-testid="stHeader"] {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        
        /* Set background and tighten top spacing */
        .stApp {background-color: #0f172a;}
        .block-container {padding-top: 2rem !important; padding-bottom: 0rem !important;}
        
        /* Custom Font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
        html, body, [class*="css"]  {
            font-family: 'Inter', sans-serif;
        }

        /* Make the frames look modern */
        iframe {border-radius: 15px; border: 1px solid #1f2937;}
    </style>
""", unsafe_allow_html=True)

# 3. WEATHER FETCHING FUNCTION
def get_weather():
    try:
        # Checking if secret exists to prevent crash
        if "OPENWEATHER_API_KEY" in st.secrets:
            api_key = st.secrets["OPENWEATHER_API_KEY"]
            url = f"http://api.openweathermap.org/data/2.5/weather?q=Funafuti,TV&appid={api_key}&units=metric"
            data = requests.get(url).json()
            return {
                "temp": round(data['main']['temp']),
                "hum": data['main']['humidity'],
                "wind": round(data['wind']['speed'] * 3.6, 1),
                "cond": data['weather'][0]['description'],
                "icon": data['weather'][0]['icon']
            }
    except Exception as e:
        print(f"Weather Error: {e}")
    
    # Fallback Data if API fails
    return {"temp": 29, "hum": 78, "wind": 10.5, "cond": "Partly Cloudy", "icon": "02d"}

w = get_weather()

# 4. MAIN DASHBOARD LAYOUT
col1, col2 = st.columns([1.2, 2], gap="large")

with col1:
    # --- WEATHER CARD ---
    st.markdown(f"""
    <div style="background: #111827; border-radius: 24px; padding: 30px; color: white; border: 1px solid #1f2937; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);">
        <p style="color: #9ca3af; margin:0; font-size: 0.8rem; letter-spacing: 1px; font-weight: 600; text-transform: uppercase;">Live Weather</p>
        <p style="color: #4b5563; margin:0; font-size: 0.75rem;">Funafuti, Tuvalu</p>
        
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
            <h1 style="font-size: 3.5rem; margin:0; font-weight: 800; letter-spacing: -2px; color: white;">{w['temp']}°C</h1>
            <img src="http://openweathermap.org/img/wn/{w['icon']}@4x.png" width="100">
        </div>
        
        <p style="color: #38bdf8; font-weight: 600; margin-bottom: 25px; text-transform: capitalize; font-size: 1.1rem;">{w['cond']}</p>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
            <div style="background: #1f2937; padding: 15px; border-radius: 16px; text-align: center; border: 1px solid #374151;">
                <small style="color: #9ca3af; font-size: 0.65rem; text-transform: uppercase; display: block; margin-bottom: 4px;">Humidity</small>
                <span style="font-weight: 700; font-size: 1.2rem;">{w['hum']}%</span>
            </div>
            <div style="background: #1f2937; padding: 15px; border-radius: 16px; text-align: center; border: 1px solid #374151;">
                <small style="color: #9ca3af; font-size: 0.65rem; text-transform: uppercase; display: block; margin-bottom: 4px;">Wind Speed</small>
                <span style="font-weight: 700; font-size: 1.2rem;">{w['wind']} <small style="font-size: 0.7rem;">km/h</small></span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # --- TV & PROGRAM GUIDE SECTION ---
    st.markdown("<h3 style='color: white; margin-top: 0;'>📅 Solomon TTV Guide</h3>", unsafe_allow_html=True)
    
    # Using st.components.v1.iframe for better loading
    st.components.v1.iframe("https://www.ttv.sb/tv-guide/", height=700, scrolling=True)
