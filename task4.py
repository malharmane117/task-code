import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample movie dataset
data = {
    'movie_id': [1, 2, 3, 4, 5],
    'title': ['Avengers', 'Iron Man', 'Captain America', 'Thor', 'Hulk'],
    'description': [
        'Superheroes save the world',
        'A man builds a powerful suit of armor',
        'A soldier becomes a superhuman warrior',
        'A god fights with his magical hammer',
        'A scientist turns into a green monster'
    ]
}

df = pd.DataFrame(data)

# TF-IDF Vectorization on descriptions
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

# Compute cosine similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Movie title to index mapping
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

# Recommendation function
def recommend(title, num_recommendations=2):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]  # exclude the input movie

    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

# Example: Get recommendations for "Iron Man"
print("Recommended movies for 'Iron Man':")
print(recommend("Iron Man"))
