import streamlit as st
import requests

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Tuvalu TV & Weather Hub", 
    layout="wide", 
    page_icon="🇹🇻"
)

# 2. THE "CLEAN LOOK" CSS
st.markdown("""
    <style>
        footer {display: none !important;}
        header {visibility: hidden;}
        [data-testid="stHeader"] {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        .stApp {background-color: #0f172a;}
        .block-container {padding-top: 2rem !important; padding-bottom: 0rem !important;}
        iframe {border-radius: 15px; border: 1px solid #1f2937; background: white;}
    </style>
""", unsafe_allow_html=True)

# 3. WEATHER FETCHING FUNCTION
def get_weather():
    try:
        if "OPENWEATHER_API_KEY" in st.secrets:
            api_key = st.secrets["OPENWEATHER_API_KEY"]
            url = f"http://api.openweathermap.org/data/2.5/weather?q=Funafuti,TV&appid={api_key}&units=metric"
            response = requests.get(url, timeout=5)
            data = response.json()
            return {
                "temp": round(data['main']['temp']),
                "hum": data['main']['humidity'],
                "wind": round(data['wind']['speed'] * 3.6, 1),
                "cond": data['weather'][0]['description'],
                "icon": data['weather'][0]['icon']
            }
    except:
        pass
    return {"temp": 29, "hum": 78, "wind": 12.4, "cond": "Partly Cloudy", "icon": "02d"}

w = get_weather()

# 4. MAIN DASHBOARD LAYOUT
col1, col2 = st.columns([1.2, 2], gap="large")

with col1:
    # --- WEATHER CARD ---
    weather_display = f"""
    <div style="background: #111827; border-radius: 24px; padding: 30px; color: white; border: 1px solid #1f2937; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);">
        <p style="color: #9ca3af; margin:0; font-size: 0.8rem; font-weight: 600; text-transform: uppercase;">Live Weather</p>
        <p style="color: #4b5563; margin:0; font-size: 0.75rem;">Funafuti, Tuvalu</p>
        
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 25px 0;">
            <h1 style="font-size: 3.5rem; margin:0; font-weight: 800; color: white;">{w['temp']}°C</h1>
            <img src="http://openweathermap.org/img/wn/{w['icon']}@4x.png" width="80">
        </div>
        
        <p style="color: #38bdf8; font-weight: 600; text-transform: capitalize; font-size: 1.1rem;">{w['cond']}</p>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
            <div style="background: #1f2937; padding: 15px; border-radius: 16px; text-align: center;">
                <small style="color: #9ca3af; font-size: 0.65rem; display: block;">HUMIDITY</small>
                <span style="font-weight: 700; font-size: 1.2rem;">{w['hum']}%</span>
            </div>
            <div style="background: #1f2937; padding: 15px; border-radius: 16px; text-align: center;">
                <small style="color: #9ca3af; font-size: 0.65rem; display: block;">WIND</small>
                <span style="font-weight: 700; font-size: 1.2rem;">{w['wind']} <small style="font-size: 0.7rem;">km/h</small></span>
            </div>
        </div>
        
        <div style="margin-top: 30px; padding-top: 20px; border-top: 1px solid #1f2937; text-align: center;">
             <a href="https://www.ttv.sb/live-stream/" target="_blank" style="text-decoration: none; background: #ef4444; color: white; padding: 12px 24px; border-radius: 12px; font-weight: bold; display: inline-block;">🔴 WATCH TTV LIVE</a>
        </div>
    </div>
    """
    
    # Ensure this line is NOT indented further than the 'weather_display' variable above
    st.markdown(weather_display, unsafe_allow_html=True)

with col2:
    # --- TV GUIDE SECTION ---
    st.markdown("<h3 style='color: white; margin-top: 0; font-family: sans-serif;'>📅 Solomon TTV Program Guide</h3>", unsafe_allow_html=True)
    
    # Safari-safe iframe method
    st.components.v1.html(f"""
        <iframe 
            src="https://www.ttv.sb/tv-guide/" 
            width="100%" 
            height="700px" 
            style="border: 1px solid #1f2937; border-radius: 15px; background: white;"
            sandbox="allow-scripts allow-same-origin allow-forms"
            loading="lazy">
        </iframe>
    """, height=720)
