import streamlit as st

st.set_page_config(layout="wide")

# --- CUSTOM CSS FOR THE WEATHER CARD ---
st.markdown("""
<style>
    .weather-card {
        background-color: #101827;
        border-radius: 20px;
        padding: 30px;
        color: white;
        font-family: 'Inter', sans-serif;
        max-width: 450px;
        margin-bottom: 20px;
    }
    .weather-header { font-size: 1.2rem; display: flex; align-items: center; gap: 10px; color: #9ca3af; }
    .temp-big { font-size: 5rem; font-weight: bold; margin: 10px 0; }
    .location { font-size: 1.5rem; color: #9ca3af; margin-bottom: 20px; }
    .stat-label { color: #6b7280; font-size: 0.9rem; }
    .stat-value { font-size: 1.2rem; font-weight: bold; }
    .alert-text { color: #f59e0b; font-weight: bold; }
</style>
""", unsafe_html=True)

# --- THE WEATHER WIDGET UI ---
with st.container():
    st.markdown(f"""
    <div class="weather-card">
        <div class="weather-header">☁️ Weather Now</div>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <div class="temp-big">28°C</div>
                <div class="location">Funafuti</div>
            </div>
            <div style="font-size: 60px;">☁️</div>
        </div>
        <hr style="border-color: #1f2937;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
            <div>
                <p class="stat-label">💧 Humidity</p>
                <p class="stat-value">78%</p>
            </div>
            <div>
                <p class="stat-label">🌬️ Wind</p>
                <p class="stat-value">15 knots</p>
            </div>
            <div>
                <p class="stat-label">👁️ Visibility</p>
                <p class="stat-value">10 km</p>
            </div>
            <div>
                <p class="stat-label">🌊 Alerts</p>
                <p class="stat-value alert-text">2 Active</p>
            </div>
        </div>
    </div>
    """, unsafe_html=True)

# --- YOUR EXISTING TV & EPG CODE BELOW THIS ---
st.divider()
st.subheader("🇹🇻 Tuvalu TV Live")
st.components.v1.iframe("https://www.facebook.com/plugins/video.php?href=https://www.facebook.com/watch/?v=1AfPd5mmTs", height=500)
