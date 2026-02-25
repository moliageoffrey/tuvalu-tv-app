import streamlit as st
import requests

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Tuvalu TV Hub", layout="wide")

# 2. THE "CLEAN LOOK" CSS (No Footer, No Header, Balanced Spacing)
st.html("""
    <style>
        /* Hide all Streamlit branding and UI elements */
        footer {display: none !important;}
        [data-testid="stHeader"] {display: none !important;}
        [data-testid="stStatusWidget"] {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        
        /* Set background and tighten the top spacing to match your screenshot */
        .stApp {background-color: #0f172a;}
        .block-container {padding-top: 2rem !important; padding-bottom: 0rem !important;}
        
        /* Smooth styling for frames */
        iframe {border-radius: 15px;}
        
        /* Custom scrollbar for a more premium feel */
        ::-webkit-scrollbar {width: 8px;}
        ::-webkit-scrollbar-track {background: #0f172a;}
        ::-webkit-scrollbar-thumb {background: #1f2937; border-radius: 10px;}
    </style>
""")

# 3. WEATHER FETCHING FUNCTION (Standard 2.5 API)
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
        # Static Fallback for stability
        return {"temp": 28, "hum": 80, "wind": 12, "cond": "Cloudy", "icon": "03d"}

w = get_weather()

# --- MAIN DASHBOARD LAYOUT ---
# Changing [1, 2.3] to [1.5, 2] makes the weather widget (col1) significantly wider
col1, col2 = st.columns([1.5, 2], gap="large")

with col1:
    # --- WEATHER CARD ---
    # The width of this card will now automatically expand to fill the wider column
    st.html(f"""
    <div style="background: #111827; border-radius: 24px; padding: 30px; color: white; border: 1px solid #1f2937; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3); width: 100%;">
        <p style="color: #9ca3af; margin:0; font-size: 0.8rem; letter-spacing: 1px; font-weight: 600;">LIVE WEATHER</p>
        ...
    </div>
    """)

with col2:
    # --- TV & PROGRAM GUIDE SECTION ---
    st.markdown("### 📅 Program Guide")
    
    # Pasifika TV Schedule
    st.components.v1.iframe("https://pasifikatv.co.nz/schedule/", height=600, scrolling=True)
    
    st.divider()
    
    # TV Player Header
    st.markdown("### 🇹🇻 Tuvalu TV Live")
    # Facebook Video Player
    st.components.v1.iframe("https://www.facebook.com/plugins/video.php?href=https://www.facebook.com/watch/?v=1AfPd5mmTs", height=450)
