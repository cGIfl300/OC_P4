from tournament import Tournament


def sorted_by_rank():
    tournament = Tournament({})
    tournament.restore()
    print("\nAffichage des joueurs par rang:\n"
          "-------------------------------\n")
    ranked_players = tournament.list_players_by_rank()
    rank = 0
    for _ in ranked_players:
        rank += 1
        print(
            f"{rank} - {_.rank} {_.surname}"
            f" {_.forename}")
