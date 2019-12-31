from typing import List, Dict
import scrython
import sqlite3
import os
import wget
import re


db_filename = "cards.db"


def create_conn(db_file: str):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return conn


def execute_query(conn, sql_cmd: str) -> None:
    try:
        c = conn.cursor()
        c.execute(sql_cmd)
    except Error as e:
        print(e)


def download_card_image(card, dest_folder: str) -> str:
    image_url = card.image_uris()["png"]  # TODO configure
    pattern = re.compile('\W')
    name_str = re.sub(pattern, '', card.name())
    file_name = "{}.png".format(name_str)
    dest_path = os.path.join(dest_folder, file_name)
    if not os.path.isfile(dest_path):
        wget.download(image_url, dest_path)
    return dest_path

def download_card_data(card_name: str):
    return scrython.cards.Named(fuzzy=card_name)


def init_table(conn) -> None:
    cmd_str = """CREATE TABLE IF NOT EXISTS cards (
                    id integer PRIMARY KEY,
                    card_name text NOT NULL,
                    card_text text NOT NULL,
                    image_path text NOT NULL);"""
    execute_query(conn, cmd_str)


def dump_tables(conn) -> List[str]:
    c = conn.cursor()
    cmd_str = "SELECT name FROM sqlite_master WHERE type='table';"
    c.execute(cmd_str)
    result = c.fetchall()
    c.close()
    return [x[0] for x in result]


def add_card(conn, card_name: str, card_text: str, image_path: str) -> None:
    c = conn.cursor()
    cmd_str = """INSERT INTO cards (card_name, card_text, image_path)
                 VALUES("{}", "{}", "{}");""".format(card_name, card_text, image_path)
    c.execute(cmd_str)
    c.close()
    conn.commit()


def download_cards(conn, dl_list: List[str], image_dir: str) -> None:
    # For each uncached entry, download card text and image 
    for card_name in dl_list:
        card = download_card_data(card_name)
        # Download image. Would eventually want to batch process this - TODO
        im_path = download_card_image(card, image_dir)
        add_card(conn, card.name(), card.oracle_text(), im_path)


def load_list(cfg: Dict[str, str], list_file: str) -> None:
    # Load requests from file
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
        remaining_cards = list(set(card_list) - set(cached_cards))
        c.close()
    
    download_cards(conn, remaining_cards, cfg["images_dir"])
    conn.close()


def get_card_record(card_name: str):
    # Return Scrython record if exists, else return None
    pass


if __name__ == "__main__":
    imgs_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
    load_list("card_list.txt", imgs_path)
