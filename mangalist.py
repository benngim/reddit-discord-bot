"""Implements functions related to the mangalist"""

mangas = set()

# Loads mangas from mangalist text file into the mangas set
def load_manga():
    print("Loading Manga List:\n")
    with open('mangalist', 'r') as file:
        for line in file:
            manga = line.rstrip()
            print(manga)
            mangas.add(manga)

# Adds new manga to both the mangalist text file and mangas set
def add_manga(manga):
    manga_title = manga.upper()
    if manga_title not in mangas:
        with open('mangalist', 'a') as file:
            print(f"Adding {manga_title} to mangalist!")
            file.write(manga_title + "\n")
            return 1
    else:
        print(f"{manga_title} is already in mangalist!")
        return 0