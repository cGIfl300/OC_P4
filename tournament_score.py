from tournament import Tournament


def tournament_score():
    tournament = Tournament({})
    tournament.restore()
    for _ in tournament.players:
        print(
            f"Joueur: {_.surname} {_.forename} - "
            f"{tournament.score_player(_)} point(s)."
        )
