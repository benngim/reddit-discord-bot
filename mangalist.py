"""Implements functions related to the mangalist"""
import database

mangas = set()

# Loads mangas from mangalist text file into the mangas set
def load_manga():
    print("Loading Manga List:\n")
    mangalist = database.get_database()["Mangas"].find()
    for manga in mangalist:
        mangas.add(manga['Title'])
        print(f"{manga['Title']}\n")

    
# Adds new manga to both the mangalist text file and mangas set
def add_manga(manga):
    manga_title = manga.upper()
    if manga_title not in mangas:
        mangas.add(manga_title)
        database.get_database()["Mangas"].insert_one({"Title": manga_title})
        return 1
    else:
        return 0

# Delete manga from mangalist text file and mangas set
def delete_manga(manga):
    manga_title = manga.upper()
    if manga_title in mangas:
        mangas.remove(manga_title)        
        database.get_database()["Mangas"].delete_one({"Title": manga_title})
        return 1
    else:
        return 0

def get_mangalist():
    mangalist = ""

    for manga in sorted(mangas):
        mangalist += f"{manga}\n"

    return mangalist