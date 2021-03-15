from tournament import Tournament


def tournament_backup():
    tournament = Tournament({})
    tournament.restore()
    tournament.backup_new()
