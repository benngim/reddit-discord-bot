"""Implements functions related to the animelist"""
import database

animes = set()

# Loads mangas from mangalist text file into the mangas set
def load_anime():
    print("Loading Anime List:\n")
    animelist = database.get_database()["Animes"].find()
    for anime in animelist:
        animes.add(anime['Title'])
        print(f"{anime['Title']}\n")

    
# Adds new manga to both the mangalist text file and mangas set
def add_anime(anime):
    anime_title = anime.upper()
    if anime_title not in animes:
        animes.add(anime_title)
        database.get_database()["Animes"].insert_one({"Title": anime_title})
        return 1
    else:
        return 0

# Delete manga from mangalist text file and mangas set
def delete_anime(anime):
    anime_title = anime.upper()
    if anime_title in animes:
        animes.remove(anime_title)        
        database.get_database()["Animes"].delete_one({"Title": anime_title})
        return 1
    else:
        return 0

def get_animelist():
    animelist = ""

    for anime in sorted(animes):
        animelist += f"{anime}\n"

    return animelist