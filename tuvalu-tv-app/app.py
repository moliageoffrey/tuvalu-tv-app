import streamlit as st

# Setup the page
st.set_page_config(page_title="Tuvalu TV Live", layout="wide")

st.title("🇹🇻 Tuvalu TV - Live Stream & Schedule")

# Video Player
st.subheader("Now Playing: Tuvalu TV")

# This link is a beautiful 4K drone view of Tuvalu to use as a live background
# until you have a specific broadcast link.
st.subheader("Facebook Live Feed")
st.components.v1.iframe("https://www.facebook.com/plugins/video.php?href=https://www.facebook.com/TuvaluBroadcastingCorporation/live", height=500)

st.divider()

# EPG Section
st.subheader("Program Guide")
epg_source = "https://pasifikatv.co.nz/schedule/"
st.components.v1.iframe(epg_source, height=800, scrolling=True)
