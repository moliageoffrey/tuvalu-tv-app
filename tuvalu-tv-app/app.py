{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
\
# 1. Page Layout (Makes it look good on wide screens)\
st.set_page_config(page_title="Tuvalu TV Live", layout="wide")\
\
# 2. The Title\
st.title("\uc0\u55356 \u56825 \u55356 \u56827  Tuvalu TV - Live Stream & Schedule")\
\
# 3. The Video Player\
# Note: Replace this URL with your actual .m3u8 stream link if you have one.\
# For now, we use a placeholder or a YouTube link.\
st.subheader("Now Playing")\
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Replace with Tuvalu TV link\
\
st.divider() # Adds a nice line between video and guide\
\
# 4. The EPG Section (The "Electronic Program Guide")\
st.subheader("Program Guide (Tuvalu & Pasifika)")\
\
# This is the URL for the Pasifika TV schedule\
epg_source = "https://pasifikatv.co.nz/schedule/"\
\
# We embed the schedule directly into your app\
st.components.v1.iframe(epg_source, height=800, scrolling=True)}