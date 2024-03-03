from flask import Flask, render_template, request
from core.fetch_movie import fetch_movie_data
from core.recommendation import create_recommendation_system, get_recommendations

app = Flask(__name__)

# Set up TMDb API key
API_KEY = 'Please paste your API Key'
BASE_URL = 'https://api.themoviedb.org/3'

# Fetch movie data
movies = fetch_movie_data(API_KEY, BASE_URL)

# Create recommendation system
movies_df, cosine_sim = create_recommendation_system(movies)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    if request.method == 'POST':
        movie_title = request.form['movie_title']
        recommended_movies = get_recommendations(movie_title, movies_df, cosine_sim)
        return render_template('recommendations.html', movie_title=movie_title, recommended_movies=recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
