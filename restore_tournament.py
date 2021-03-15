import jsonpickle
from tinydb import TinyDB

from number_of_tournaments import number_of_tournaments
from to_integer import convert_to_integer
from tournament import Tournament


def restore_tournament(selected_tournament):
    total_tournaments = number_of_tournaments()
    selected_tournament = convert_to_integer(selected_tournament)
    if not selected_tournament:
        print("Must be integer")
        return
    if selected_tournament > total_tournaments or selected_tournament < 1:
        print("Numéro de tournois invalide.")
        return
    print(
        f"Restauration du tournois numéro {selected_tournament}:\n"
        "-------------------------------------------------------\n"
    )
    db = TinyDB("data/db.json")
    tournaments_table = db.table("tournaments")
    count = 0
    for _ in tournaments_table:
        count += 1
        if count == selected_tournament:
            tournament = Tournament(
                jsonpickle.decode(_["Tournaments"]).__dict__)
            print(f"{count} - {tournament.name}")
            # Is now the activated tournament
            tournament.save()
