from tournament import Tournament


def sorted_by_names():
    tournament = Tournament({})
    tournament.restore()
    print("\nAffichage des joueurs par ordre alphabétique:\n"
          "---------------------------------------------\n")
    ranked_players = tournament.list_players_by_names()
    rank = 0
    for _ in ranked_players:
        rank += 1
        print(
            f"{rank} - {_.surname} {_.forename}")
