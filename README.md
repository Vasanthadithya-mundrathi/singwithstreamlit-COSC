# 🎤 Sing With Streamlit: Taylor Swift Lyrics Visualizer

A Streamlit web app that lets you enter a Taylor Swift song title, fetches the lyrics from the Genius API, displays them in a clean textbox, and generates a beautiful word cloud.

## Features

- Enter any Taylor Swift song title
- Fetches lyrics using the Genius API
- Displays lyrics in a scrollable textbox
- Generates a word cloud from the lyrics
- Interactive and visually appealing UI
- Handles missing API key and errors gracefully

## Requirements

- Python 3.7+
- streamlit
- lyricsgenius
- wordcloud
- matplotlib

## Setup

1. Install dependencies:
   ```
   pip install streamlit lyricsgenius wordcloud matplotlib
   ```

2. Set your Genius API token as an environment variable:
   ```
   export GENIUS_ACCESS_TOKEN=your_genius_api_token
   ```

3. Run the app:
   ```
   streamlit run app.py
   ```

## Deployment

- Push this folder to GitHub.
- On Streamlit Cloud, set the `GENIUS_ACCESS_TOKEN` as a secret.
- Deploy the app.

## Credits

- Built with [Streamlit](https://streamlit.io/)
- Lyrics from [Genius API](https://genius.com/developers)
- Word cloud by [wordcloud](https://github.com/amueller/word_cloud)

---
Made for the COSC Swiftie + Pythonista challenge!
