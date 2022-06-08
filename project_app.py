from unittest import result
from fastapi import FastAPI
import recommender
import atexit

#global variables
uri = "neo4j+s://5f4265ee.databases.neo4j.io"
user = "neo4j"
password = "w1iFkPByrJMyPIhl4S102q16Llw-KI-oxDGJxvLSF1U" # modify this accordingly based on your own password
    
neo_db = recommender.Recommender(uri, user, password)

# exit handler
def exit_application():
    neo_db.close()

atexit.register(exit_application)

app = FastAPI()


@app.get('/getRecommendation')
async def get_recommendation_by_knn(username):
    result = neo_db.find_recommendation_knn(username)
    return result

@app.delete('/deleteRating')
async def delete_rating(userId, movieId):
    result = neo_db.deleteRating(userId, movieId)
    return result

@app.get('/getMovie')
async def find_movie_by_name(movie_name):
    result = neo_db.find_movie(movie_name)
    return result

@app.post('/createNewUser')
async def create_a_new_user(name, custom_id):
    result = neo_db.createUser(name, custom_id)
    return result

@app.post('/ratingMovie')
async def rating_a_movie(userId, movieId, rating):
    result = neo_db.ratedMovie(userId, movieId, rating)
    return result

@app.get('/get_recommend_content')
async def find_recommendation_content_based(title, by_another_user):
    result = neo_db.find_recommendation_content(title, by_another_user)
    return result

@app.get('/get_recommend_user')
async def find_recommendation_by_user(user_name):
    result = neo_db.find_recommendation_user(user_name)
    return result