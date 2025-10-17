## Instructions
## You're building a movie recommendation system and need to process movie data using lambda functions.

movies = [
    {"title": "The Matrix", "year": 1999, "rating": 8.7, "genre": "Sci-Fi"},
    {"title": "Inception", "year": 2010, "rating": 8.8, "genre": "Thriller"},
    {"title": "Pulp Fiction", "year": 1994, "rating": 8.9, "genre": "Crime"},
    {"title": "The Godfather", "year": 1972, "rating": 9.2, "genre": "Crime"},
    {"title": "Avatar", "year": 2009, "rating": 7.8, "genre": "Sci-Fi"},
    {"title": "Titanic", "year": 1997, "rating": 7.8, "genre": "Romance"},
]


# TODO: Sort movies by rating (highest first)
by_rating = sorted(movies, key=lambda movie: movie["rating"], reverse=True)

# TODO: Sort movies by year (newest first)
by_year = sorted(movies, key=lambda movie: movie["year"], reverse=True)

# Test your sorting
print("Highest rated:", by_rating[0]["title"])
print("Newest movie:", by_year[0]["title"])
