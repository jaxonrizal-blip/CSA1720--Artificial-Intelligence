import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample user ratings
ratings = {
    'Movie1': [5, 5, 1, 0],
    'Movie2': [4, 4, 2, 0],
    'Movie3': [0, 3, 5, 4],
    'Movie4': [0, 2, 4, 5]
}

df = pd.DataFrame(
    ratings,
    index=['User1', 'User2', 'User3', 'User4']
)

print("User Ratings:")
print(df)

# Calculate similarity
similarity = cosine_similarity(df)

similarity_df = pd.DataFrame(
    similarity,
    index=df.index,
    columns=df.index
)

# Select target user
target_user = 'User1'

# Get similarities with other users
similar_users = similarity_df.loc[target_user].drop(target_user)

# Align rating data with similar users
user_ratings = df.loc[similar_users.index]

# Calculate predicted ratings
predicted = similar_users @ user_ratings
predicted = predicted / similar_users.sum()

# Find unrated movies
unrated = df.loc[target_user] == 0

# Display recommendations
recommendations = predicted[unrated].sort_values(
    ascending=False
)

print("\nRecommended Movies for", target_user)
print(recommendations)
