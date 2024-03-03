import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def create_recommendation_system(movies):
    # Convert data to DataFrame
    movies_df = pd.DataFrame(movies)

    # Concatenate genres into a single string
    movies_df['genres_str'] = movies_df['genre_ids'].apply(lambda x: ' '.join(map(str, x)))

    # Initialize TF-IDF Vectorizer
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')

    # Fit and transform the TF-IDF vectorizer
    tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['genres_str'])

    # Compute cosine similarity matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    return movies_df, cosine_sim

def get_recommendations(title, movies_df, cosine_sim):
    # Get the index of the movie that matches the title
    idx = movies_df.loc[movies_df['title'].str.lower() == title.lower()].index[0]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the titles of the top 10 most similar movies
    # Return the titles and poster paths of the top 10 most similar movies
    #recommendations = [{'title': movies_df['title'].iloc[idx], 'poster_path': movies_df['poster_path'].iloc[idx]} for idx in movie_indices]
     # Return the titles and poster paths of the top 10 most similar movies
    recommendations = [{'title': movies_df['title'].iloc[idx],
                        'overview': movies_df['overview'].iloc[idx],
                        'poster_path': 'https://image.tmdb.org/t/p/w500' + movies_df['poster_path'].iloc[idx]} 
                       for idx in movie_indices]
    #return movies_df['title'].iloc[movie_indices]
    return recommendations
