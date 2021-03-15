from to_integer import convert_to_integer
from tournament import Tournament


def update_players_ranks():
    tournament = Tournament({})
    tournament.restore()
    for _ in tournament.players:
        print(f"Joueur: {_.surname} {_.forename} - {_.rank} (actuel)")
        new_rank = input("Nouveau classement: ")
        new_rank = convert_to_integer(new_rank)
        if not new_rank:
            print(
                "Le nouveau classement dois être un entier, on passe au "
                "suivant.")
            continue
        else:
            _.rank = new_rank
    tournament.save()
