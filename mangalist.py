"""Implements functions related to the mangalist"""

mangas = set()

def load_manga():
    print("Manga List: ")
    with open('mangalist', 'r') as file:
        for line in file:
            print(line)
            manga = line.rstrip()
            mangas.add(manga)

