import streamlit as st

st.set_page_config(page_title="Tuvalu TV Live", layout="wide")

st.title("🇹🇻 Tuvalu TV - Live Stream & Schedule")

st.subheader("Featured Broadcast")

# This is the most stable version of the Facebook Embed URL
# It points directly to the video ID 1AfPd5mmTs
st.subheader("Latest from Tuvalu TV")
# This shows the actual Facebook Page Feed
st.components.v1.iframe("https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2FTuvaluBroadcastingCorporation&tabs=timeline&width=500&height=500", height=500)

st.subheader("Program Guide")
st.components.v1.iframe("https://pasifikatv.co.nz/schedule/", height=800, scrolling=True)
