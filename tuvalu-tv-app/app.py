import streamlit as st
import requests

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Tuvalu TV Hub", layout="wide")

# 2. THE "CLEAN LOOK" CSS
st.html("""
    <style>
        /* Hide all Streamlit branding */
        footer {display: none !important;}
        [data-testid="stHeader"] {display: none !important;}
        [data-testid="stStatusWidget"] {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        
        /* Set background and tighten top spacing */
        .stApp {background-color: #0f172a;}
        .block-container {padding-top: 1rem !important; padding-bottom: 0rem !important;}
        
        /* Make the frames look modern */
        iframe {border-radius: 15px;}
    </style>
""")

# 3. WEATHER FETCHING FUNCTION
def get_weather():
    try:
        api_key = st.secrets["OPENWEATHER_API_KEY"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q=Funafuti,TV&appid={api_key}&units=metric"
        data = requests.get(url).json()
        return {
            "temp": round(data['main']['temp']),
            "hum": data['main']['humidity'],
            "wind": round(data['wind']['speed'] * 3.6, 1),
            "cond": data['weather'][0]['main'],
            "icon": data['weather'][0]['icon']
        }
    except:
        return {"temp": 28, "hum": 80, "wind": 12, "cond": "Clear", "icon": "01d"}

w = get_weather()

# 4. MAIN DASHBOARD LAYOUT
# I increased the first number (1.5) to make the weather column wider
col1, col2 = st.columns([1.5, 2], gap="large")

with col1:
    # --- WEATHER CARD ---
    st.html(f"""
    <div style="background: #111827; border-radius: 24px; padding: 30px; color: white; border: 1px solid #1f2937; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);">
        <p style="color: #9ca3af; margin:0; font-size: 0.8rem; letter-spacing: 1px; font-weight: 600;">LIVE WEATHER</p>
        <p style="color: #4b5563; margin:0; font-size: 0.75rem;">Funafuti, Tuvalu</p>
        
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
            <h1 style="font-size: 4rem; margin:0; font-weight: 800; letter-spacing: -2px;">{w['temp']}°C</h1>
            <img src="http://openweathermap.org/img/wn/{w['icon']}@4x.png" width="80">
        </div>
        
        <p style="color: #38bdf8; font-weight: 600; margin-bottom: 25px; text-transform: uppercase; font-size: 0.9rem;">{w['cond']}</p>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
            <div style="background: #1f2937; padding: 15px; border-radius: 16px; text-align: center;">
                <small style="color: #6b7280; font-size: 0.6rem; text-transform: uppercase; display: block; margin-bottom: 4px;">Humidity</small>
                <span style="font-weight: 700; font-size: 1.1rem;">{w['hum']}%</span>
            </div>
            <div style="background: #1f2937; padding: 15px; border-radius: 16px; text-align: center;">
                <small style="color: #6b7280; font-size: 0.6rem; text-transform: uppercase; display: block; margin-bottom: 4px;">Wind</small>
                <span style="font-weight: 700; font-size: 1.1rem;">{w['wind']} <small style="font-size: 0.7rem;">km/h</small></span>
            </div>
        </div>
    </div>
    """)

with col2:
    # --- TV & PROGRAM GUIDE SECTION ---
    st.markdown("### 📅 Program Guide")
    st.components.v1.iframe("https://pasifikatv.co.nz/schedule/", height=600, scrolling=True)
    
    st.divider()
    
   # st.markdown("### 🇹🇻 Tuvalu TV Live")
   # st.components.v1.iframe("https://www.facebook.com/plugins/video.php?href=https://www.facebook.com/watch/?v=1AfPd5mmTs", height=450)
