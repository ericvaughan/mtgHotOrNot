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


def execute_query(conn, sql_cmd: str):
    try:
        c = conn.cursor()
        c.execute(sql_cmd)
    except Error as e:
        print(e)


def download_card_image(card_name: str):
    card = scrython.cards.Named(fuzzy=card_name)


def init_table(conn):
    import pdb;pdb.set_trace()
    cmd_str = """CREATE TABLE IF NOT EXISTS cards (
                    id integer PRIMARY KEY,
                    card_name text NOT NULL,
                    card_text text NOT NULL,
                    image_path text NOT NULL);"""
    execute_query(conn, cmd_str)


def dump_tables(conn):
    c = conn.cursor()
    cmd_str = "SELECT name FROM sqlite_master WHERE type='table';"
    c.execute(cmd_str)
    result = c.fetchall()
    c.close()
    return [x[0] for x in result]


def load_list(list_file: str):
    # Load requests from file
    import pdb;pdb.set_trace()
    card_list = open(list_file, "r").readlines()
    card_list = [x.strip("\n") for x in card_list]
    conn = create_conn(db_filename)

    if "cards" not in dump_tables(conn):
        init_table(conn)
        remaining_cards = card_list
    else: 
        # Load cached data
        c = conn.cursor()
        cmd_str = "SELECT card_name FROM cards;"
        c.execute(cmd_str)
        cached_cards = [x[0] for x in c.fetchall()]
        import pdb;pdb.set_trace()
        c.close()
    
    download_cards(remaining_cards)
    conn.close()

    # For each uncached entry, download card text and image 
    #if !get_card_record:
        

def get_card_record(card_name: str):
    # Return Scrython record if exists, else return None
    pass


if __name__ == "__main__":
    load_list("card_list.txt")
