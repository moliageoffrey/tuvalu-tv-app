import streamlit as st
import requests

st.set_page_config(layout="wide")

# --- 1. WEATHER DATA ---
def get_weather():
    try:
        api_key = st.secrets["OPENWEATHER_API_KEY"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q=Funafuti,TV&appid={api_key}&units=metric"
        data = requests.get(url).json()
        return data
    except: return None

w_data = get_weather()

# --- 2. THE BALANCED LAYOUT ---
# We create two columns. [1, 2.5] means the right side is 2.5x wider than the left.
col1, col2 = st.columns([1, 2.5], gap="medium")

with col1:
    # --- WEATHER CARD ---
    if w_data:
        temp = round(w_data['main']['temp'])
        cond = w_data['weather'][0]['main']
        icon = w_data['weather'][0]['icon']
        
        st.html(f"""
        <div style="background: #101827; border-radius: 20px; padding: 25px; color: white; border: 1px solid #1f2937;">
            <p style="color: #9ca3af; margin:0; font-size: 0.9rem;">Funafuti, Tuvalu</p>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h1 style="font-size: 4rem; margin:0;">{temp}°C</h1>
                <img src="http://openweathermap.org/img/wn/{icon}@4x.png" width="80">
            </div>
            <p style="color: #38bdf8; font-weight: 600; margin-top: 10px;">{cond}</p>
            <hr style="border-color: #1f2937; margin: 20px 0;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; text-align: center;">
                <div><small style="color: #6b7280;">HUMIDITY</small><br><b>{w_data['main']['humidity']}%</b></div>
                <div><small style="color: #6b7280;">WIND</small><br><b>{round(w_data['wind']['speed']*3.6)} km/h</b></div>
            </div>
        </div>
        """)

with col2:
    # --- TV & EPG ---
    st.markdown("### 🇹🇻 Tuvalu TV Live")
    st.components.v1.iframe("https://www.facebook.com/plugins/video.php?href=https://www.facebook.com/watch/?v=1AfPd5mmTs", height=450)
    
    st.divider()
    
    st.markdown("### 📅 Program Guide")
    st.components.v1.iframe("https://pasifikatv.co.nz/schedule/", height=600, scrolling=True)
