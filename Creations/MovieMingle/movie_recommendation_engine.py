import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movie_dataset.csv")  # Load your dataset here

features = ["keywords", "cast", "genres", "director"]

def combine_features(row):
    return (
        row["keywords"]
        + " "
        + row["cast"]
        + " "
        + row["genres"]
        + " "
        + row["director"]
    )

for feature in features:
    df[feature] = df[feature].fillna("")  # Fill all NaNs with blank string
df["combined_features"] = df.apply(combine_features, axis=1)

cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
cosine_sim = cosine_similarity(count_matrix)

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]

def recommend_similar_movies(movie_title):
    if movie_title not in df["title"].values:
        print("Movie not found in the dataset.")
        return
    
    movie_index = get_index_from_title(movie_title)
    similar_movies = list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]
    
    print(f"\nRecommended movies similar to '{movie_title}':")
    for i, element in enumerate(sorted_similar_movies):
        if i >= 5:  # Print the top 5 recommended movies
            print("Type 'more' for more recommended movies.")
            more = input()
            if more.lower() != "more":
                break
            i = 0
        similar_movie_title = get_title_from_index(element[0])
        print(f"{i+1}. {similar_movie_title}")
        i += 1
    print("\n")

# Ask the user for input
user_input = input("Enter 'search' to search for a specific movie title or enter a genre: ")

if user_input.lower() == "search":
    user_movie_title = input("Enter the movie title: ")
    recommend_similar_movies(user_movie_title)
else:
    user_genre = user_input
    filtered_movies = df[df["genres"].str.contains(user_genre, case=False)]

    if filtered_movies.empty:
        print("No movies found for the given input.")
    else:
        print(f"\nTop recommended movies in the '{user_genre}' genre are:\n")
        
        for index, row in filtered_movies.iterrows():
            print(f"Recommended movies similar to '{row['title']}':")
            recommend_similar_movies(row["title"])
