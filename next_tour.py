from tournament import Tournament


def next_tour():
    tournament = Tournament({})
    tournament.restore()
    tournament.new_tour()
