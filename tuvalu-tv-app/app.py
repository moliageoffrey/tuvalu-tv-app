import streamlit as st

st.set_page_config(layout="wide")

# This hides the internal elements so they don't peek through while loading
st.html("""
    <style>
        #MainMenu {visibility: hidden !important;}
        footer {display: none !important;}
        header {visibility: hidden !important;}
        [data-testid="stStatusWidget"] {display: none !important;}
        .block-container {padding-top: 0rem !important; padding-bottom: 0rem !important;}
        .stApp {background-color: #0f172a;}
    </style>
""")

# 2. Weather Fetching Logic (Keep this in the main app for speed)
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
        return {"temp": 28, "hum": 83, "wind": 9.3, "vis": 10.0, "cond": "Clouds", "icon": "03d"}

w = get_weather()

# 3. Create Columns for Balance
# col1 is for Weather, col2 is for the TV/EPG
col1, col2 = st.columns([1, 1.8], gap="large")

with col1:
    st.markdown("### ☁️ Local Weather")
    st.html(f"""
    <style>
        .weather-card {{
            background: #111827;
            border-radius: 20px;
            padding: 25px;
            color: white;
            font-family: sans-serif;
            border: 1px solid #1f2937;
        }}
        .temp-val {{ font-size: 4.5rem; font-weight: 800; margin: 0; }}
        .stat-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 20px; }}
        .stat-box {{ background: #1f2937; padding: 12px; border-radius: 12px; text-align: center; }}
        .stat-label {{ color: #6b7280; font-size: 0.7rem; text-transform: uppercase; }}
    </style>
    <div class="weather-card">
        <p style="color: #9ca3af; margin:0;">Funafuti, Tuvalu</p>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h1 class="temp-val">{w['temp']}°C</h1>
            <img src="http://openweathermap.org/img/wn/{w['icon']}@4x.png" width="80">
        </div>
        <p style="color: #38bdf8; font-weight: 600; margin-bottom: 20px;">{w['cond']}</p>
        <div class="stat-grid">
            <div class="stat-box"><p class="stat-label">Humidity</p><b>{w['hum']}%</b></div>
            <div class="stat-box"><p class="stat-label">Wind</p><b>{w['wind']} km/h</b></div>
            <div class="stat-box"><p class="stat-label">Visibility</p><b>{w['vis']} km</b></div>
            <div class="stat-box"><p class="stat-label">Region</p><b>Oceania</b></div>
        </div>
    </div>
    """)

with col2:
    st.markdown("### 🇹🇻 Tuvalu TV Live")
    # THE TV PLAYER
    #st.components.v1.iframe("https://www.facebook.com/plugins/video.php?href=https://www.facebook.com/watch/?v=1AfPd5mmTs", height=400)
    
    st.markdown("### 📅 Program Guide")
    # THE EPG
    st.components.v1.iframe("https://pasifikatv.co.nz/schedule/", height=600, scrolling=True)
