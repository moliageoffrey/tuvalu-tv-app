# Use st.markdown with the unsafe_allow_html flag at the end
st.markdown(f"""
<div style="background: #111827; border-radius: 24px; padding: 30px; color: white; border: 1px solid #1f2937;">
    <p style="color: #9ca3af; margin:0; font-size: 0.8rem; letter-spacing: 1px; font-weight: 600; text-transform: uppercase;">Live Weather</p>
    <p style="color: #4b5563; margin:0; font-size: 0.75rem;">Funafuti, Tuvalu</p>
    
    <div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
        <h1 style="font-size: 3.5rem; margin:0; font-weight: 800; letter-spacing: -2px; color: white;">{w['temp']}°C</h1>
        <img src="http://openweathermap.org/img/wn/{w['icon']}@4x.png" width="100">
    </div>
    
    <p style="color: #38bdf8; font-weight: 600; margin-bottom: 25px; text-transform: capitalize; font-size: 1.1rem;">{w['cond']}</p>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
        <div style="background: #1f2937; padding: 15px; border-radius: 16px; text-align: center; border: 1px solid #374151;">
            <small style="color: #9ca3af; font-size: 0.65rem; text-transform: uppercase; display: block; margin-bottom: 4px;">Humidity</small>
            <span style="font-weight: 700; font-size: 1.2rem; color: white;">{w['hum']}%</span>
        </div>
        <div style="background: #1f2937; padding: 15px; border-radius: 16px; text-align: center; border: 1px solid #374151;">
            <small style="color: #9ca3af; font-size: 0.65rem; text-transform: uppercase; display: block; margin-bottom: 4px;">Wind Speed</small>
            <span style="font-weight: 700; font-size: 1.2rem; color: white;">{w['wind']} <small style="font-size: 0.7rem;">km/h</small></span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True) # <--- THIS LINE IS THE KEY
