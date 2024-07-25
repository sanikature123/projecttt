import streamlit as st
import requests

# OMDb API key
API_KEY = '94a257a1'

# Function to fetch movie data from OMDb API
def fetch_movie_data(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"
    response = requests.get(url)
    return response.json()

# Streamlit app
st.title("Movie Information App")

# Input for movie title
movie_title = st.text_input("Enter movie title:")

# Button to fetch movie data
if st.button("Get Movie Info"):
    if movie_title:
        # Fetch movie data
        movie_data = fetch_movie_data(movie_title)
        
        # Display movie data
        if movie_data.get("Response") == "True":
            st.write("Title:", movie_data.get("Title"))
            st.write("Year:", movie_data.get("Year"))
            st.write("Rated:", movie_data.get("Rated"))
            st.write("Released:", movie_data.get("Released"))
            st.write("Runtime:", movie_data.get("Runtime"))
            st.write("Genre:", movie_data.get("Genre"))
            st.write("Director:", movie_data.get("Director"))
            st.write("Writer:", movie_data.get("Writer"))
            st.write("Actors:", movie_data.get("Actors"))
            st.write("Plot:", movie_data.get("Plot"))
            st.write("Language:", movie_data.get("Language"))
            st.write("Country:", movie_data.get("Country"))
            st.write("Awards:", movie_data.get("Awards"))
            st.write("Poster:", movie_data.get("Poster"))
            st.image(movie_data.get("Poster"))
        else:
            st.write("Movie not found.")
    else:
        st.write("Please enter a movie title.")
