# app.py

import streamlit as st
from lyricsgenius import Genius
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# Configuration
st.set_page_config(
    page_title="Taylor Swift Lyrics Visualizer",
    page_icon="🎵",
    layout="wide"
)

# Genius API token - can be set via environment variable or directly
GENIUS_ACCESS_TOKEN = os.getenv("GENIUS_ACCESS_TOKEN", "R26e_IIphluKwuxNzVURUOxnr5pT10L-iC12uHCftzS2S5ecYsMmB5XMc_Sj4hgu")

# Initialize Genius client
if GENIUS_ACCESS_TOKEN != "WdJgb1rMGkQqEM1rO3BrHcmi820cHkhG5cX4eQZXI_xxrdzEeCDuDGjSRHoaEHgH":
    genius = Genius(GENIUS_ACCESS_TOKEN)
    genius.verbose = False  # Turn off status messages
    genius.remove_section_headers = True  # Clean up lyrics
else:
    genius = None

# App header
st.title("🎵 Taylor Swift Lyrics Visualizer")
st.markdown("Enter a Taylor Swift song title to fetch lyrics and generate a beautiful word cloud!")

# API key status
if genius is None:
    st.warning("⚠️ Genius API key not configured. Please set your API token to use this app.")
    st.info("To get started: Go to https://genius.com/developers, create an API client, and get your access token.")

# Input section
song_title = st.text_input("Enter Taylor Swift Song Title:", placeholder="e.g., Shake It Off, Love Story, Anti-Hero")

if song_title and genius:
    with st.spinner(f"Searching for '{song_title}' by Taylor Swift..."):
        try:
            # Search for the song
            song = genius.search_song(song_title, artist="Taylor Swift")
            
            if song:
                # Display song info
                st.success(f"Found: **{song.title}** by {song.artist}")
                
                # Create two columns for layout
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.subheader("📝 Lyrics")
                    # Display lyrics in a scrollable text area
                    st.text_area(
                        "Song Lyrics",
                        song.lyrics,
                        height=400,
                        label_visibility="collapsed"
                    )
                
                with col2:
                    st.subheader("☁️ Word Cloud")
                    # Generate and display word cloud
                    try:
                        # Clean lyrics for word cloud (remove common words)
                        lyrics_text = song.lyrics.lower()
                        
                        # Create word cloud
                        wordcloud = WordCloud(
                            width=800, 
                            height=400, 
                            background_color="white",
                            colormap="viridis",
                            max_words=100,
                            relative_scaling=0.5,
                            stopwords=set(['verse', 'chorus', 'bridge', 'outro', 'intro'])
                        ).generate(lyrics_text)
                        
                        # Display word cloud
                        fig, ax = plt.subplots(figsize=(10, 5))
                        ax.imshow(wordcloud, interpolation="bilinear")
                        ax.axis("off")
                        st.pyplot(fig)
                        plt.close(fig)
                        
                    except Exception as e:
                        st.error(f"Error generating word cloud: {e}")
                
            else:
                st.warning(f"Song '{song_title}' by Taylor Swift not found. Please check the spelling and try again.")
                
        except Exception as e:
            st.error(f"An error occurred while searching: {e}")
            st.info("This might be due to API rate limits or network issues. Please try again in a moment.")

elif song_title and not genius:
    st.error("Cannot search for lyrics without a valid Genius API token.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and the Genius API")
