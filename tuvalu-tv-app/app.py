import streamlit as st

st.set_page_config(page_title="Tuvalu TV Live", layout="wide")

st.title("🇹🇻 Tuvalu TV - Live Stream & Schedule")

st.subheader("Featured Broadcast")

# This is the most stable version of the Facebook Embed URL
# It points directly to the video ID 1AfPd5mmTs
fb_embed_link = "https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2Ffacebook%2Fvideos%2F10153231339965444%2F&show_text=0&width=560" 

# Alternative: If the specific video is being stubborn, 
# it is better to embed the whole Page Feed so it always shows the LATEST video.
page_plugin = "https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2FTuvaluBroadcastingCorporation&tabs=timeline&width=500&height=500&small_header=false&adapt_container_width=true&hide_cover=false&show_facepile=true"

# Try the video first:
st.components.v1.iframe(f"https://www.facebook.com/plugins/video.php?href=https://www.facebook.com/watch/?v=1AfPd5mmTs", height=500)

st.divider()

st.subheader("Program Guide")
st.components.v1.iframe("https://pasifikatv.co.nz/schedule/", height=800, scrolling=True)
