import jsonpickle
from tinydb import TinyDB

from tournament import Tournament


def tournaments_list():
    print(
        "Liste des tournois sauvegardés:\n"
        "-------------------------------\n")
    db = TinyDB("data/db.json")
    tournaments_table = db.table("tournaments")
    count = 0
    for _ in tournaments_table:
        count += 1
        tournament = Tournament(jsonpickle.decode(_["Tournaments"]).__dict__)
        print(f"{count} - {tournament.name}")
