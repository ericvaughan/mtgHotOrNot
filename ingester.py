import scrython
import sqlite3
import os


db_filename = "cards.db"


def create_conn(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return conn


def create_table(conn, create_table_sql: str):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def download_card_image(card_name: str):
    card = scrython.cards.Named(fuzzy=card_name)


def init_table(conn):
    cmd_str = """CREATE TABLE IF NOT EXISTS cards (
                    id integer PRIMARY KEY,
                    card_name text NOT NULL,
                    card_text text NOT NULL,
                    image_path text NOT NULL
                 );"""
    create_table(conn, cmd_str)


def dump_tables(conn):
    import pdb;pdb.set_trace()
    c = conn.cursor()
    cmd_str = "SELECT name FROM sqlite_master WHERE type='table';"
    c.execute(cmd_str)
    result = c.fetchall()
    c.close()


def load_list(list_file: str):
    # Load requests from file
    card_list = open(list_file, "r").readlines()
    # TODO split the string into proper list
    conn = create_conn(db_filename)

    f "cards" not in dump_tables(conn:
        init_table(db_filename)
        remaining_cards = card_list
    else: 
        # Load cached data
        pass
    
    download_cards(remaining_cards)
    conn.close()

    # For each uncached entry, download card text and image 
    #if !get_card_record:
        

def get_card_record(card_name: str):
    # Return Scrython record if exists, else return None
    pass


if __name__ == "__main__":
    load_list("card_list.txt")
