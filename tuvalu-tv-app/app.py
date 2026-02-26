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
    # Enhanced Tuvalu Weather Dashboard
    weather_card = f"""
    <div style="
        background: linear-gradient(145deg, #111827, #1e293b); 
        border-radius: 15px; 
        padding: 30px; 
        color: white; 
        border: 1px solid #334155; 
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.4);
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    ">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
            <p style="color: #38bdf8; margin:0; font-size: 0.85rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase;">Island Forecast</p>
            <span style="font-size: 1.5rem;">🇹🇻</span>
        </div>
        <h2 style="margin:0; font-size: 1.6rem; font-weight: 300; color: #f8fafc;">Funafuti, Tuvalu</h2>
        
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 30px 0;">
            <div>
                <h1 style="font-size: 4.5rem; margin:0; font-weight: 800; letter-spacing: -3px; color: white;">{w['temp']}°C</h1>
                <p style="color: #38bdf8; font-weight: 600; text-transform: capitalize; font-size: 1.2rem; margin-top: -5px;">{w['cond']}</p>
            </div>
            <img src="http://openweathermap.org/img/wn/{w['icon']}@4x.png" style="width: 120px; filter: drop-shadow(0 0 10px #38bdf8);">
        </div>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
            <div style="background: rgba(30, 41, 59, 0.5); padding: 20px; border-radius: 20px; text-align: center; border: 1px solid #334151;">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 8px;"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>
                <small style="color: #9ca3af; font-size: 0.7rem; display: block; text-transform: uppercase; letter-spacing: 1px;">Humidity</small>
                <span style="font-weight: 700; font-size: 1.4rem;">{w['hum']}%</span>
            </div>
            <div style="background: rgba(30, 41, 59, 0.5); padding: 20px; border-radius: 20px; text-align: center; border: 1px solid #334151;">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom: 8px;"><path d="M9.59 4.59A2 2 0 1 1 11 8H2m10.59 11.41A2 2 0 1 0 14 16H2m15.73-8.27A2.5 2.5 0 1 1 19.5 12H2"/></svg>
                <small style="color: #9ca3af; font-size: 0.7rem; display: block; text-transform: uppercase; letter-spacing: 1px;">Wind Speed</small>
                <span style="font-weight: 700; font-size: 1.4rem;">{w['wind']} <small style="font-size: 0.8rem; font-weight: 400;">km/h</small></span>
            </div>
        </div>

        <div style="margin-top: 25px; text-align: center;">
            <p style="color: #475569; font-size: 0.7rem; font-style: italic;">Data updated via OpenWeather API</p>
        </div>
    </div>
    """
    
    # We increased the height slightly to fit the icons and padding
    st.components.v1.html(weather_card, height=520)

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
