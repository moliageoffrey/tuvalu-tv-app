import streamlit as st

# Setup the page
st.set_page_config(page_title="Tuvalu TV Live", layout="wide")

st.title("🇹🇻 Tuvalu TV - Live Stream & Schedule")

# Video Player
st.subheader("Now Playing")
# Replace this URL with your actual stream link later
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") 

st.divider()

# EPG Section
st.subheader("Program Guide")
epg_source = "https://pasifikatv.co.nz/schedule/"
st.components.v1.iframe(epg_source, height=800, scrolling=True)
