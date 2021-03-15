from add_player import add_player
from to_integer import convert_to_integer
from tournament import Tournament


def create_tournament():
    """Création d'un tournois, instanciation de la class puis sauvegarde en tan
    que tournois actif.
    :return:
    """
    name = input("Nom du Tournois: ")
    place = input("Emplacement du Tournois: ")
    date = input("Date du Tournois: ")
    rounds = input("Nombre de tours: ")
    number_of_players = input("Nombre de joueurs: ")
    time_control = input("Contrôle du temps: ")
    comment = input("Commentaire: ")
    rounds = convert_to_integer(rounds)
    number_of_players = convert_to_integer(number_of_players)
    if not rounds or rounds < 1:
        print("Le nombre de tours dois être un entier positif.")
        return
    if not number_of_players or number_of_players < 2:
        print("Il faut que le nombre de joueurs soit égal ou supérieur à 2")
        return
    tournament = Tournament(
        {
            "name": name,
            "place": place,
            "date": date,
            "rounds": rounds,
            "time_control": time_control,
            "comment": comment,
        }
    )
    # Add players...
    for _ in range(number_of_players):
        print(f"Ajout du joueur {_ + 1} sur {number_of_players}")
        add_player(tournament)
    tournament.save()
