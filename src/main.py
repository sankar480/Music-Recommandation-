import streamlit as st
from recommand import df, recommand_song  # assuming recommmand_song is the correct function name

# Page configuration
st.set_page_config(
    page_title="Music Recommender",
    page_icon="🎵",
    layout="centered"
)

# App title
st.title("Instant Music Recommender")

# Dropdown to select a song
song_list = sorted(df['song'].dropna().unique())
selected_song = st.selectbox("Select a song:", song_list)

# Button to trigger recommendation
if st.button("Recommend Songs"):
    with st.spinner("Finding similar songs..."):
        recommendation = recommand_song(selected_song)
        if isinstance(recommendation, str):
            st.warning(recommendation)
        else:
            st.success("Top Similar Songs:")
            st.table(recommendation)
