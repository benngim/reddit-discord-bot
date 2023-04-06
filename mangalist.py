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
        mangas.add(manga_title)
        with open('mangalist', 'a') as file:
            print(f"Adding {manga_title} to mangalist!")
            file.write(manga_title + "\n")
            return 1
    else:
        print(f"{manga_title} is already in mangalist!")
        return 0

# Delete manga from mangalist text file and mangas set
def delete_manga(manga):
    manga_title = manga.upper()
    if manga_title in mangas:
        mangas.remove(manga_title)

        with open('mangalist', 'r') as file:
            lines = file.readlines()

        with open('mangalist', 'w') as file:
            for line in lines:
                if line.strip("\n") != manga_title:
                    file.write(line)

        print(f"{manga_title} has been deleted from the mangalist!")
        return 1

    else:
        print(f"{manga_title} is already not in mangalist!")
        return 0

def get_mangalist():
    mangalist = ""

    with open('mangalist', 'r') as file:
        for line in file:
            mangalist += line

    return mangalist