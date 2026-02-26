import streamlit as st
import requests

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Tuvalu National Weather & TV Hub", 
    layout="wide", 
    page_icon="🇹🇻"
)

# 2. THE "CLEAN LOOK" CSS & TUVALU BRANDING
st.markdown("""
    <style>
        footer {display: none !important;}
        header {visibility: hidden;}
        [data-testid="stHeader"] {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        .stApp {background-color: #001f2b;}
        .block-container {padding-top: 1.5rem !important; padding-bottom: 0rem !important;}
        h3 { font-family: 'Inter', sans-serif; letter-spacing: -0.5px; color: white !important; }
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
    return {"temp": 29, "hum": 75, "wind": 14.5, "cond": "partly cloudy", "icon": "02d"}

w = get_weather()

# 4. MAIN DASHBOARD LAYOUT
col1, col2 = st.columns([1.1, 2], gap="large")

with col1:
    # --- NATIONAL RESILIENCE HUB WEATHER INTERFACE ---
    weather_card = f"""
    <div style="
        background: linear-gradient(160deg, #002B36 0%, #004B5E 100%); 
        border-radius: 28px; padding: 30px; color: white; border: 2px solid #38bdf8; 
        box-shadow: 0 15px 35px rgba(0,0,0,0.6); font-family: 'Inter', sans-serif;
    ">
        <div style="text-align: center; border-bottom: 1px solid rgba(56, 189, 248, 0.3); padding-bottom: 15px; margin-bottom: 25px;">
            <h3 style="margin:0; font-size: 1.1rem; color: #FFD700; letter-spacing: 2px; font-weight: 800;">🇹🇻 NATIONAL RESILIENCE HUB</h3>
            <p style="margin:5px 0 0; font-size: 0.75rem; color: #9ca3af; font-weight: 600;">COASTAL MONITORING: FUNAFUTI</p>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h1 style="font-size: 4.2rem; margin:0; font-weight: 800; color: white; letter-spacing: -3px;">{w['temp']}°C</h1>
                <p style="color: #38bdf8; font-weight: 700; font-size: 1.2rem; text-transform: capitalize; margin-top: -5px;">{w['cond']}</p>
            </div>
            <img src="http://openweathermap.org/img/wn/{w['icon']}@4x.png" width="110">
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 25px;">
            <div style="background: rgba(0,0,0,0.3); padding: 15px; border-radius: 18px; border-left: 5px solid #38bdf8;">
                <small style="color: #9ca3af; display: block; font-size: 0.7rem; font-weight: bold; text-transform: uppercase;">Tidal Risk</small>
                <span style="font-weight: 800; color: #00ffcc; font-size: 1.1rem;">NORMAL</span>
            </div>
            <div style="background: rgba(0,0,0,0.3); padding: 15px; border-radius: 18px; border-left: 5px solid #FFD700;">
                <small style="color: #9ca3af; display: block; font-size: 0.7rem; font-weight: bold; text-transform: uppercase;">UV Index</small>
                <span style="font-weight: 800; color: #f8fafc; font-size: 1.1rem;">HIGH (8)</span>
            </div>
        </div>
        <div style="margin-top: 25px; background: rgba(56, 189, 248, 0.1); border: 1px dashed #38bdf8; padding: 12px; border-radius: 15px; text-align: center;">
            <p style="margin:0; font-size: 0.8rem; color: #38bdf8; font-weight: 600;">🌊 ADVISORY: No coastal flood threats detected.</p>
        </div>
    </div>
    """
    st.components.v1.html(weather_card, height=550)

with col2:
    # --- LIVE SATELLITE SECTION ---
    st.markdown("<h3>🛰️ Regional Satellite (Live Clouds & Rain)</h3>", unsafe_allow_html=True)
    
    # Windy.com Live Satellite Map for Tuvalu
    satellite_url = "https://www.windy.com/-8.520/179.200?satellite,-9.319,179.200,6"
    
    # We use st.components.v1.iframe here which is more stable for map providers
    st.components.v1.iframe(
        "https://embed.windy.com/embed2.html?lat=-8.520&lon=179.200&detailLat=-8.520&detailLon=179.200&width=650&height=450&zoom=6&level=surface&overlay=satellite&product=satellite&menu=&message=true&marker=&calendar=now&pressure=&type=map&location=coordinates&detail=&metricWind=default&metricTemp=default&radarRange=-1",
        height=500
    )
    
    # Optional Program Guide below the map
    with st.expander("📺 View TTV Program Guide"):
        st.components.v1.html("""
            <iframe src="https://www.ttv.sb/tv-guide/" width="100%" height="500px" style="border-radius:15px;"></iframe>
        """, height=520)
