import streamlit as st
import json
from PIL import Image
from Classifier import KNearestNeighbours
from operator import itemgetter
from bs4 import BeautifulSoup
import requests,io
import PIL.Image
from urllib.request import urlopen


# Load data and movies list from corresponding JSON files
with open(r'data.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
with open(r'titles.json', 'r+', encoding='utf-8') as f:
    movie_titles = json.load(f)

def movie_poster_fetcher(imdb_link):
    ## Display Movie Poster
    url_data = requests.get(imdb_link).text
    s_data = BeautifulSoup(url_data, 'html.parser')
    imdb_dp = s_data.find("meta", property="og:image")
    movie_poster_link = imdb_dp.attrs['content']
    u = urlopen(movie_poster_link)
    raw_data = u.read()
    image = PIL.Image.open(io.BytesIO(raw_data))
    image = image.resize((250, 300) )
    st.image(image, use_column_width=False)

def knn(test_point, k):
    # Create dummy target variable for the KNN Classifier
    target = [0 for item in movie_titles]
    # Instantiate object for the Classifier
    model = KNearestNeighbours(data, target, test_point, k=k)
    # Run the algorithm
    model.fit()
    # Distances to most distant movie
    max_dist = sorted(model.distances, key=itemgetter(0))[-1]
    # Print list of 10 recommendations < Change value of k for a different number >
    table = list()
    for i in model.indices:
        # Returns back movie title and imdb link
        table.append([movie_titles[i][0], movie_titles[i][2]])
    return table



if __name__ == '__main__':
    genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
              'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News',
              'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'War', 'Western']
    movies = [title[0] for title in movie_titles]
    st.header('MOVIE RECOMMENDER APPLICATION')
    apps = ['--Select--', 'Movie based', 'Criteria based']
    app_options = st.selectbox('Select Recommendation Type:', apps)
    if app_options == 'Movie based':
        movie_select = st.selectbox('Select movie:', ['--Select--'] + movies)
        if movie_select == '--Select--':
            st.write('Select any movie')
        else:
            n = st.number_input('Number of movies:', min_value=5, max_value=20, step=1)
            genres = data[movies.index(movie_select)]
            test_point = genres
            table = knn(test_point, n+1)
            table.pop(0)
            x=0
            st.markdown(
                '''<h4 style='text-align: left; color: #d73b5c;'>* Fetching movie posters will take few seconds.*</h4>''',
                unsafe_allow_html=True)
            for movie, link in table:
                x+=1
                # Displays movie title with link to imdb
                st.markdown(f"({x})[{movie}]({link})")
                movie_poster_fetcher(link)
    elif app_options == apps[2]:
        options = st.multiselect('Select genres:', genres)
        if options:
            imdb_score = st.slider('IMDb score:', 1, 10, 7)
            n = st.number_input('Number of movies:', min_value=5, max_value=20, step=1)
            test_point = [1 if genre in options else 0 for genre in genres]
            test_point.append(imdb_score)
            table = knn(test_point, n)
            x=0
            st.markdown(
                '''<h4 style='text-align: left; color: #d73b5c;'>* Fetching movie posters will take few seconds.*</h4>''',
                unsafe_allow_html=True)
            for movie, link in table:
                x+=1
                # Displays movie title with link to imdb
                st.markdown(f"({x})[{movie}]({link})")
                value = imdb_score
                formatted_string = "{:.2f}".format(imdb_score)
                # format to two decimal places
                float_value = float(formatted_string)
                #st.write(imdb_score)
                st.markdown('IMDB Rating: ' + str(float_value) + '⭐')
                movie_poster_fetcher(link)
        else:
            st.write("This is a simple Movie. || You can select the genres and change the IMDb score.")
    else:
        st.write('Select option')