🎬 **MovieMingle: Movie Recommendation System** 🍿 <br>

MovieMingle is a web application designed to provide personalized movie recommendations to users based on their input movie titles. The system utilizes Flask, HTML, CSS, and the TMDB API to fetch movie data, process it, and generate recommendations using a content-based filtering approach. This report provides an overview of the project, including its objectives, implementation details, features, recommendation technique, and future enhancements. <br>


## Table of Contents
1. [Objectives](#objectives)
2. [Implementation Details](#implementation-details)
3. [Recommendation Technique](#recommendation-technique)
4. [Features](#features)
5. [Future Enhancements](#future-enhancements)
6. [Output][#output]
7. [How to use][how-to-use]
   
## Objectives 
The primary objectives of the Movie Recommendation System project are as follows: <br>
🌟 Develop a web application for movie recommendations to enhance user experience in discovering new movies. <br>
🌟 Utilize the TMDB API to fetch movie data, including titles, genres, overviews, and poster images. <br>
🌟 Implement a content-based filtering algorithm to generate personalized movie recommendations based on user input. <br>
🌟 Create an intuitive user interface for interacting with the recommendation system. <br>
🌟 Deploy the application to a web server to make it accessible to users. <br>

## Implementation Details
The implementation of the Movie Recommendation System involves the following key components and technologies: <br>
🛠️ Flask: Flask is used as the web application framework to handle HTTP requests and responses. It provides routes for serving web pages and processing user input. <br>
🛠️ HTML/CSS: HTML is used for creating the structure of web pages, while CSS is used for styling the user interface to improve aesthetics and usability. <br>
🛠️ TMDB API: The TMDB (The Movie Database) API is utilized to fetch movie data, including titles, genres, overviews, and poster images. This data is essential for generating movie recommendations. <br>
🛠️ Content-Based Filtering: The recommendation algorithm is based on content-based filtering, which analyzes the intrinsic characteristics of movies, such as genres and plot descriptions, to generate recommendations. <br>
🛠️ Python Libraries: Various Python libraries such as requests, pandas, scikit-learn, and Flask are used for data retrieval, processing, recommendation system implementation, and web development. <br>

## Recommendation Technique 
The Movie Recommendation System employs a content-based filtering approach to generate personalized movie recommendations. Here's how the recommendation technique works: <br>
🔍 Data Retrieval: Movie data is fetched from the TMDB API, including titles, genres, and overviews. <br>
🔍 Data Preprocessing: The fetched movie data is processed and organized into a DataFrame. Genres are concatenated into a single string for each movie to represent its genre profile. <br>
🔍 TF-IDF Vectorization: TF-IDF (Term Frequency-Inverse Document Frequency) vectorization is applied to the genre profiles. This step converts textual data into numerical form, capturing the importance of each genre across all movies. <br>
🔍 Similarity Calculation: Cosine similarity is calculated between each pair of movies based on their TF-IDF vectors. This measures the similarity between movies' genre profiles, indicating how closely related they are in terms of genre. <br>
🔍 Recommendation Generation: When a user inputs a movie title, the system finds the index of the input movie in the DataFrame. Then, it retrieves the similarity scores between the input movie and all other movies. The top N (e.g., 10) most similar movies are selected based on these scores and presented as recommendations. <br>

## Features
The Movie Recommendation System offers the following features: <br>
🔎 Movie Search: Users can search for movie recommendations by entering the title of a movie they like. <br>
🔎 Personalized Recommendations: The system generates personalized movie recommendations based on the input movie title and the content of the movies. <br>
🔎 Interactive User Interface: The web interface provides an intuitive and user-friendly experience for interacting with the recommendation system. <br>
🔎 Movie Details: Each recommended movie is accompanied by its title, overview, and poster image for easy exploration. <br>
🔎 Responsive Design: The user interface is designed to be responsive, ensuring optimal viewing and interaction across different devices and screen sizes. <br>

## Future Enhancements [for v2]
While the Movie Recommendation System provides valuable functionality, there are several opportunities for future enhancements: <br>
🚀 Collaborative Filtering: Explore collaborative filtering techniques to incorporate user ratings and interactions for more accurate recommendations. <br>
🚀 Advanced Algorithms: We can use more advanced recommendation algorithms such as matrix factorization and deep learning models to improve recommendation quality. <br>
🚀 Performance Optimization: Optimize the recommendation algorithm and data retrieval process to handle larger datasets and scale the application for increased traffic. <br>

## Output

<img src='https://github.com/codeasarjun/MovieMingle/blob/main/img/search.png'> 
<hr>

<img src='https://github.com/codeasarjun/MovieMingle/blob/main/img/result.png'> 
<hr>

<img src='https://github.com/codeasarjun/MovieMingle/blob/main/img/sample_ouput.gif'> 
<hr>


## How to use
Clone the Repository: 📥 <br>
To access the code and deploy the application locally, follow these steps: 🛠️ <br>

Clone the GitHub repository to your local machine using Git or download the repository as a ZIP file. 📦 <br>
Navigate to the project directory. 📂 <br>
Install any necessary dependencies. ⚙️ <br>
Run the application using the provided instructions. ▶️ <br>
Access the application through your web browser and start using MovieMingle! 🎬🍿 <br>
