import streamlit as st
import requests

# 1. PAGE CONFIGURATION
# Must be the very first Streamlit command
st.set_page_config(
    page_title="Tuvalu TV & Weather Hub", 
    layout="wide", 
    page_icon="🇹🇻"
)

# 2. THE "CLEAN LOOK" CSS
# This hides Streamlit bars and styles the background
st.markdown("""
    <style>
        /* Hide Streamlit Branding */
        footer {display: none !important;}
        header {visibility: hidden;}
        [data-testid="stHeader"] {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        
        /* App Background */
        .stApp {background-color: #0f172a;}
        
        /* Space management */
        .block-container {padding-top: 2rem !important; padding-bottom: 0rem !important;}
        
        /* Custom Iframe Styling */
        iframe {border-radius: 15px; border: 1px solid #1f2937; background: white;}
        
        /* Mobile adjustment */
        @media (max-width: 768px) {
            .stColumn {margin-bottom: 20px;}
        }
    </style>
""", unsafe_allow_html=True)

# 3. WEATHER FETCHING FUNCTION
def get_weather():
    try:
        # Check if the secret exists in Streamlit Cloud Settings
        if "OPENWEATHER_API_KEY" in st.secrets:
            api_key = st.secrets["OPENWEATHER_API_KEY"]
            # Fetching for Funafuti, Tuvalu
            url = f"http://api.openweathermap.org/data/2.5/weather?q=Funafuti,TV&appid={api_key}&units=metric"
            response = requests.get(url, timeout=5)
            data = response.json()
            
            return {
                "temp": round(data['main']['temp']),
                "hum": data['main']['humidity'],
                "wind": round(data['wind']['speed'] * 3.6, 1), # Convert m/s to km/h
                "cond": data['weather'][0]['description'],
                "icon": data['weather'][0]['icon']
            }
    except Exception as e:
        # If API fails, show this log in 'Manage App' but don't crash the site
        print(f"Weather Data Error: {e}")
    
    # Fallback Data (Default display if API is offline)
    return {"temp": 29, "hum": 78, "wind": 12.4, "cond": "Partly Cloudy", "icon": "02d"}

# Get the data
w = get_weather()

# 4. MAIN DASHBOARD LAYOUT
# col1 is for Weather (narrower), col2 is for TV Guide (wider)
col1, col2 = st.columns([1.2, 2], gap="large")

with col1:
    # --- WEATHER CARD ---
    # We use an f-string to inject the weather variables into the HTML
    weather_card = f"""
    <div style="background: #111827; border-radius: 24px; padding: 30px; color: white; border: 1px solid #1f2937; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);">
        <p style="color: #9ca3af; margin:0; font-size: 0.8rem; letter-spacing: 1px; font-weight: 600; text-transform: uppercase;">Live Weather</p>
        <p style="color: #4b5563; margin:0; font-size: 0.75rem;">Funafuti, Tuvalu</p>
        
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 25px 0;">
            <h1 style="font-size: 3.8rem; margin:0; font-weight: 800; letter-spacing: -2px; color: white;">{w['temp']}°C</h1>
            <img src="http://openweathermap.org/img/wn/{w['icon']}@4x.png" width="90">
        </div>
        
        <p style="color: #38bdf8; font-weight: 600; margin-bottom: 25px; text-transform: capitalize; font-size: 1.1rem;">{w['cond']}</p>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
            <div style="background: #1f2937; padding: 15px; border-radius: 16px; text-align: center; border: 1px solid #374151;">
                <small style="color: #9ca3af; font-size: 0.65rem; text-transform: uppercase; display: block; margin-bottom: 4px;">Humidity</small>
                <span style="font-weight: 700; font-size: 1.2rem; color: white;">{w['hum']}%</span>
            </div>
            <div style="background: #1f2937; padding: 15px; border-radius: 16px; text-align: center; border: 1px solid #374151;">
                <small style="color: #9ca3af; font-size: 0.65rem; text-transform: uppercase; display: block; margin-bottom: 4px;">Wind Speed</small>
                <span style="font-weight: 700; font-size: 1.2rem; color: white;">{w['wind']} <small style="font-size: 0.7rem;">km/h</small></span>
            </div>
        </div>
        
        <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid #1f2937; text-align: center;">
             <a href="https://www.ttv.sb/live-stream/" target="_blank" style="text-decoration: none; background: #ef4444; color: white; padding: 10px 20px; border-radius: 10px; font-weight: bold; font-size: 0.9rem;">🔴 WATCH TTV LIVE</a>
        </div>
    </div>
    """
with col1:
    # ... (all your weather_card HTML code is here) ...
    
    # THE FIX IS RIGHT HERE:
    st.markdown(weather_card, unsafe_allow_html=True)

with col2:
    # --- TV GUIDE SECTION ---
    st.markdown("<h3 style='color: white; margin-top: 0; font-family: sans-serif;'>📅 Solomon TTV Program Guide</h3>", unsafe_allow_html=True)
    
    # Embedding the external TV guide from TTV
    st.components.v1.iframe("https://www.ttv.sb/tv-guide/", height=750, scrolling=True)
