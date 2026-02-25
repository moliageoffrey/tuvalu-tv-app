import streamlit as st

# Setup the page
st.set_page_config(page_title="Tuvalu TV Live", layout="wide")

st.title("🇹🇻 Tuvalu TV - Live Stream & Schedule")

# Video Player Section
st.subheader("Featured Broadcast")

# This is the "Magic" link format for Facebook embeds
fb_video_url = "https://www.facebook.com/plugins/video.php?href=https://www.facebook.com/watch/?v=1AfPd5mmTs&show_text=0&width=560"

# We use an iframe to ensure the Facebook player loads correctly
st.components.v1.iframe(fb_video_url, height=500, scrolling=False)

st.divider()

# EPG Section
st.subheader("Program Guide")
epg_source = "https://pasifikatv.co.nz/schedule/"
st.components.v1.iframe(epg_source, height=800, scrolling=True)
