from database import SessionLocal
from query_helpers import *

db = SessionLocal()

# rating = get_ratings(db, limit = 10, min_rating=3.5, user_id=1)
# for film in rating:
#     print(f"ID : {film.movieId}, Note : {film.rating}")

rating = get_rating(db, user_id=1, movie_id=1)
print(f"UserID: {rating.userId}, MovieID: {rating.movieId}, Rating: {rating.rating}, Timestamp: {rating.timestamp}")


# tag = get_tag(db, user_id=2, movie_id=60756, tag_text="funny")
# print(tag)
# print(f"UserID: {tag.userId}, MovieID: {tag.movieId}, Tag: {tag.tag}, Timestamp: {tag.timestamp}")

# n_movies = get_link_count(db)
# print(f"Nombre de films avec des liens : {n_movies}")
# db.close()