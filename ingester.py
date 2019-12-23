import scrython
import sqlite3


def download_card_image(card_name: str):
    card = scrython.cards.Named(fuzzy=card_name)


def load_list(list_file: str):
    # Load requests from file
    card_list = open(list_file, "r").readlines()
    
    # Load cached data
    card_conn = sqlite3.connect("cards.db")
    card_cursor = card_conn.cursor()

    # For each uncached entry, download card text and image 
    


if __name__ == "__main__":
    import pdb;pdb.set_trace()
    download_card_image("Black Lotus")
