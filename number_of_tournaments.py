from tinydb import TinyDB


def number_of_tournaments():
    db = TinyDB("data/db.json")
    tournaments_table = db.table("tournaments")
    return len(tournaments_table)
