### problem statement 
Demonstrate through your app the different kinds of algorithms that a web-streaming app (like Netflix) or an audio-streaming app (like Spotify) may use for their Recommendation Engine.

### Movie Recommender  
A movie recommender that recommends movies using the K Nearest Neighbours algorithm from a list of ~5000 movies. Deployed Heroku Web App: https://my-movie-recommender-app.herokuapp.com/

### requirements
- Python version: 3.7.4
- Python modules: pandas, numpy, operator, json, streamlit

### dataset
IMDB 5000 Movie Dataset downloaded from [Kaggle](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)

### source code files
- ```data.py``` loads the data from the CSV files, cleans it, modifies it into the required format and stores it in JSON files
- ```Classifier.py``` is my implementation of the K-Nearest Neighbours algorithm
- ```recommender.py``` is the recommendation engine that runs the KNN algorithm on the data and displays the recommendations
- ```data.json``` and ```titles.json``` are JSON files containg the data created in ```data.py``` for faster loading when the recommendation engine is run
- ```test_movies.py``` is a file containing sample test data and steps to create new test data
- The movie we are fetching recommendations for is by default set to "Avengers: Infinity War" but it can easily be changed by following the steps in ```test_movies.py```
- The number of recommendations is by default set to 5. This can be changed by modifying the value of ```k``` in ```recommender.py``` 
- Added an implementation of the recommender in a [streamlit](for frontend)(https://docs.streamlit.io/en/latest/index.html) app. Can be found at ```st_app.py```
- Options to select multiple genres and IMDb score. Also option to select number of movies recommended. Range provided is 5 to 20 movies.

### features
- Recommendation's based on movie or genre 
- Simple responsive UI
- Movie's official page imdb link
- Movie Poster


### usage
- Clone my repository.
- Open CMD in working directory.
- Run following command.
- pip install -r requirements.txt
- st_app.py is the main Python file of Streamlit Web-Application.
- To run app, write following command in CMD. or use any IDE.
 streamlit run st_app.py
