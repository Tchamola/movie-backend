
#%%
from database import SessionLocal
from models import Movie, Rating, Tag, Link


db = SessionLocal()
#%%
## Tester la récupération de quelques films

movies = db.query(Movie).limit(5).all()

for movie in movies:
    print(f"ID: {movie.movieId}, Title: {movie.title}, Genres: {movie.genres}")

else:
    print("No movies found !")

## Récupérer les films du genre "Action"

action_movies = db.query(Movie).filter(Movie.genres.contains("Action")).limit(5).all()

for movie in action_movies:
    print(f"ID: {movie.movieId}, Title: {movie.title}, Genres: {movie.genres}")

else:
    print("No action movies found !")

## Tester la récupération des évaluations (ratings)

Ratings = db.query(Rating).limit(5).all()

for rating in Ratings:
    print(f"UserID: {rating.userId}, MoviesID: {rating.movieId}, Rating: {rating.rating}, Timestamp: {rating.timestamp}")

else:
    print("No ratings found !")
#%%
## Films avec une note supérieure ou égale à 4

high_rated_movies = db.query(Movie).join(Rating).filter(Rating.rating >= 4).limit(5).all()

for title, rating in high_rated_movies:
    print(title, rating)

hight_rated_movies = (
    db.query(Movie.title, Rating.rating)
    .join(Rating)
    .filter(Rating.rating >= 4, Movie.movieId == Rating.movieId)
    .limit(5)
    .all() 
)

for title, rating in hight_rated_movies:
    print(title, rating)
#%%
## Récupération des tags associés aux films

tags = db.query(Tag).limit(5).all()

for tag in tags:
    print(f"UserID: {tag.userId}, MovieID: {tag.movieId}, Tag: {tag.tag}, Timestamp: {tag.timestamp}")

else:
    print("No tags found !")

## Tester la classe Link

links = db.query(Link).limit(5).all()

for link in links:
    print(f"MovieID: {link.movieId}, IMDB ID: {link.imdbId}, TMDB ID: {link.tmdbId}")

else:
    print("No links found !")

## Fermer la session de la base de données
db.close()
# %%
