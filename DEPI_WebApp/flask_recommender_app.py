
from flask import Flask, request, render_template
import pandas as pd
from genre_mapping import genre_mapping

app = Flask(__name__)

# Dummy data to replace actual data (you can load real datasets in these variables)
sampled_df = pd.read_csv('data/sampled_df.csv')

similarity_df = pd.read_csv('data/similarity_df.csv')

def recommend_books_by_genre(genre, sampled_df, similarity_df, genre_mapping, top_n=10):
    if genre not in genre_mapping:
        return "Genre not found."

    # Get the encoded genre value
    encoded_genre = genre_mapping[genre]

    # Filter books of the selected genre
    genre_books = sampled_df[sampled_df['Genre_Encoded'] == encoded_genre]

    if genre_books.empty:
        return "No books found for this genre."

    # Get recommendations based on the first book in the genre
    first_book = genre_books['Title'].iloc[0]

    # Handle cases where the book is not found in similarity_df
    if first_book not in similarity_df.index:
        return f"No similarity data found for the book '{first_book}' in this genre."

    recommendations = similarity_df.loc[first_book].sort_values(ascending=False)

    # Exclude books already in the genre
    recommendations = recommendations[~recommendations.index.isin(genre_books['Title'])]

    return recommendations.head(top_n).index.tolist()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        genre = request.form["genre"]
        recommended_books = recommend_books_by_genre(genre, sampled_df, similarity_df, genre_mapping)

        if isinstance(recommended_books, list):
            return render_template("index.html", recommendations=recommended_books, genre=genre)
        else:
            return render_template("index.html", error=recommended_books)
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
