# KNN Movie Recommender
A movie recommender that recommends movies using the K Nearest Neighbours algorithm from a list of ~5000 movies

### Requirements
- Python version: 3.7.4
- Python modules: pandas, numpy, operator, json, streamlit

### Dataset
IMDB 5000 Movie Dataset downloaded from [Kaggle](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)

### Files
- ```Classifier.py``` is my implementation of the K-Nearest Neighbours algorithm
- ```data.py``` loads the data from the CSV files, cleans it, modifies it into the required format and stores it in JSON files
- ```recommender.py``` is the recommendation engine that runs the KNN algorithm on the data and displays the recommendations
- ```data.json``` and ```titles.json``` are JSON files containg the data created in ```data.py``` for faster loading when the recommendation engine is run
- ```test_movies.py``` is a file containing sample test data and steps to create new test data

### Steps
- Just run ```recommender.py``` to get the recommendations
- The movie we are fetching recommendations for is by default set to "Avengers: Infinity War" but it can easily be changed by following the steps in ```test_movies.py```
- The number of recommendations is by default set to 10. This can be changed by modifying the value of ```k``` in ```recommender.py```

### Streamlit App
- Added an implementation of the recommender in a [streamlit](https://docs.streamlit.io/en/latest/index.html) app. Can be found at ```st_app.py```
- Options to select multiple genres and IMDb score. Also option to select number of movies recommended. Range provided is 5 to 30 movies.

