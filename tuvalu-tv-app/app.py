import streamlit as st
import requests

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Tuvalu TV Hub", layout="wide")

# 2. NUCLEAR CSS (Hides footer, balloon, and cleans up padding)
st.html("""
    <style>
        /* Hide all Streamlit branding and UI elements */
        footer {display: none !important;}
        [data-testid="stHeader"] {display: none !important;}
        [data-testid="stStatusWidget"] {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        
        /* Set background and remove top spacing */
        .stApp {background-color: #0f172a;}
        .block-container {padding-top: 1rem !important; padding-bottom: 0rem !important;}
        
        /* Ensure the app is responsive */
        iframe {border-radius: 12px;}
    </style>
""")

# 3. WEATHER FETCHING FUNCTION
def get_weather():
    try:
        api_key = st.secrets["OPENWEATHER_API_KEY"]
        # Standard API 2.5 for stability
        url = f"http://api.openweathermap.org/data/2.5/weather?q=Funafuti,TV&appid={api_key}&units=metric"
        data = requests.get(url).json()
        return {
            "temp": round(data['main']['temp']),
            "hum": data['main']['humidity'],
            "wind": round(data['wind']['speed'] * 3.6, 1),
            "vis": data.get('visibility', 0) / 1000,
            "cond": data['weather'][0]['main'],
            "icon": data['weather'][0]['icon']
        }
    except:
        # Fallback values if API is down or key is still activating
        return {"temp": 28, "hum": 80, "wind": 12, "vis": 10, "cond": "Cloudy", "icon": "03d"}

w = get_weather()

# 4. MAIN DASHBOARD LAYOUT (Balanced Columns)
# col1 is narrower for the weather card, col2 is wider for the video
col1, col2 = st.columns([1, 2.5], gap="large")

with col1:
    # --- WEATHER SIDEBAR ---
    st.html(f"""
    <div style="background: #111827; border-radius: 20px; padding: 25px; color: white; border: 1px solid #1f2937; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
        <p style="color: #9ca3af; margin:0; font-size: 0.9rem; letter-spacing: 0.05em;">LIVE WEATHER</p>
        <p style="color: #64748b; margin:0; font-size: 0.8rem;">Funafuti, Tuvalu</p>
        
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 15px 0;">
            <h1 style="font-size: 3.5rem; margin:0; font-weight: 800;">{w['temp']}°C</h1>
            <img src="http://openweathermap.org/img/wn/{w['icon']}@4x.png" width="70">
        </div>
        
        <p style="color: #38bdf8; font-weight: 600; margin-bottom: 20px; text-transform: capitalize;">{w['cond']}</p>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
            <div style="background: #1f2937; padding: 12px; border-radius: 12px; text-align: center;">
                <small style="color: #6b7280; font-size: 0.65rem; text-transform: uppercase;">Humidity</small><br>
                <span style="font-weight: 700;">{w['hum']}%</span>
            </div>
            <div style="background: #1f2937; padding: 12px; border-radius: 12px; text-align: center;">
                <small style="color: #6b7280; font-size: 0.65rem; text-transform: uppercase;">Wind</small><br>
                <span style="font-weight: 700;">{w['wind']} km/h</span>
            </div>
        </div>
    </div>
    """)

with col2:
    # --- TV PLAYER ---
    st.markdown("### 🇹🇻 Tuvalu TV Live")
    st.components.v1.iframe("https://www.facebook.com/plugins/video.php?href=https://www.facebook.com/watch/?v=1AfPd5mmTs", height=450)
    
    st.divider()
    
    # --- PROGRAM GUIDE ---
    st.markdown("### 📅 Program Guide")
    st.components.v1.iframe("https://pasifikatv.co.nz/schedule/", height=600, scrolling=True)
