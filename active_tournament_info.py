from tournament import Tournament


def active_tournament_info():
    tournament = Tournament({})
    tournament.restore()
    print(
        "Tournois actif:\n"
        "---------------\n"
        f"Nom: {tournament.name}\n"
        f"Date: {tournament.date}\n"
        f"Tour actif: {tournament.active_tour + 1}"
    )
