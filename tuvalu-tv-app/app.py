import streamlit as st
import requests

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Tuvalu TV Hub", layout="wide")

# 2. NUCLEAR CSS (Hides footer, balloon, and cleans up padding)
st.html("""
    <style>
        footer {display: none !important;}
        [data-testid="stHeader"] {display: none !important;}
        [data-testid="stStatusWidget"] {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        .stApp {background-color: #0f172a;}
        .block-container {padding-top: 0rem !important; padding-bottom: 0rem !important;}
        
        /* Ticker Styling */
        .ticker-wrap {
            width: 100%;
            overflow: hidden;
            background-color: #1e293b; 
            padding: 10px 0;
            border-bottom: 2px solid #334155;
            margin-bottom: 20px;
        }
        .ticker {
            display: inline-block;
            white-space: nowrap;
            animation: marquee 40s linear infinite;
            color: #f8fafc;
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
        }
        @keyframes marquee {
            0% { transform: translate(0, 0); }
            100% { transform: translate(-100%, 0); }
        }
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
            "vis": data.get('visibility', 0) / 1000,
            "cond": data['weather'][0]['main'],
            "icon": data['weather'][0]['icon']
        }
    except:
        return {"temp": 28, "hum": 80, "wind": 12, "vis": 10, "cond": "Clear", "icon": "01d"}

w = get_weather()

# 4. NEWS & WEATHER TICKER CONTENT
headlines = [
    f"🌡️ FUNAFUTI: {w['temp']}°C",
    f"☁️ {w['cond']}",
    "Tuvalu Harbours Infrastructure Project Update",
    "Climate Resilience: New Water Systems for Outer Islands",
    "Pacific Leaders Summit Highlights Regional Connectivity",
    "Tuvalu Fisheries Management Council New Regulations",
    "Sea Wall Construction Progresses in Funafuti"
]
ticker_text = " • ".join(headlines)

# Display Ticker
st.html(f"""
    <div class="ticker-wrap">
        <div class="ticker">
            <span>{ticker_text} &nbsp;&nbsp;&nbsp; • &nbsp;&nbsp;&nbsp; {ticker_text}</span>
        </div>
    </div>
""")

# 5. MAIN DASHBOARD LAYOUT (Balanced Columns)
col1, col2 = st.columns([1, 2.5], gap="large")

with col1:
    # --- WEATHER SIDEBAR ---
    st.html(f"""
    <div style="background: #111827; border-radius: 20px; padding: 25px; color: white; border: 1px solid #1f2937;">
        <p style="color: #9ca3af; margin:0; font-size: 0.9rem;">Funafuti, Tuvalu</p>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h1 style="font-size: 3.5rem; margin:0; font-weight: 800;">{w['temp']}°C</h1>
            <img src="http://openweathermap.org/img/wn/{w['icon']}@4x.png" width="70">
        </div>
        <p style="color: #38bdf8; font-weight: 600; margin: 10px 0;">{w['cond']}</p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 20px;">
            <div style="background: #1f2937; padding: 10px; border-radius: 10px; text-align: center;">
                <small style="color: #6b7280;">HUMIDITY</small><br><b>{w['hum']}%</b>
            </div>
            <div style="background: #1f2937; padding: 10px; border-radius: 10px; text-align: center;">
                <small style="color: #6b7280;">WIND</small><br><b>{w['wind']} km/h</b>
            </div>
        </div>
    </div>
    """)

with col2:
    # --- TV PLAYER & PROGRAM GUIDE ---
    st.markdown("### 🇹🇻 Tuvalu TV Live")
    st.components.v1.iframe("https://www.facebook.com/plugins/video.php?href=https://www.facebook.com/watch/?v=1AfPd5mmTs", height=450)
    
    st.divider()
    
    st.markdown("### 📅 Program Guide")
    st.components.v1.iframe("https://pasifikatv.co.nz/schedule/", height=600, scrolling=True)
