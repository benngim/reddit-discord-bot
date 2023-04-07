"""Setup for mongo database"""

import pymongo
from dotenv import load_dotenv
import os

def get_database():
    load_dotenv()

    # Create a connection using MongoClient
    client = pymongo.MongoClient(os.getenv("CONNECTION_STRING"))

    # Create the manga database
    return client['manga_db']
  

if __name__ == "__main__":     
   # Get the database
   manga_db = get_database()