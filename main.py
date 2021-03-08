import argparse

from tournament import Tournament


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--create", help="create a new tournament", action="store_true"
    )

    parser.add_argument(
        "-e",
        "--edit",
        help="edit tournament properties",
    )

    parser.add_argument(
        "-d",
        "--delete",
        help="delete tournament",
    )

    parser.add_argument(
        "-cp",
        "--create_players",
        help="create players",
    )

    parser.add_argument(
        "-ep",
        "--edit_players",
        help="edit players",
    )

    parser.add_argument(
        "-st",
        "--stop_tour",
        help="stop tour and ask for matchs results",
    )

    return parser.parse_args()


def create_tournament():
    """Création d'un tournois, instanciation de la class puis sauvegarde en tan que tournois actif.
    :return:
    """
    name = input("Nom du Tournois: ")
    place = input("Emplacement du Tournois: ")
    date = input("Date du Tournois: ")
    rounds = input("Nombre de tours: ")
    number_of_players = input("Nombre de joueurs: ")
    time_control = input("Contrôle du temps: ")
    comment = input("Commentaire: ")
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
    for _ in number_of_players:
        print(f"Ajout du joueur {_} sur {number_of_players}")
        add_player(tournament)

    tournament.save()


def add_player(tournament):
    print(f"Just to do something... {tournament.name}")
    pass


def main():
    args = parse_arguments()
    if args.create:
        create_tournament()


if __name__ == "__main__":
    main()
