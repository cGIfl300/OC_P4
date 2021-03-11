import argparse

import jsonpickle
from tinydb import TinyDB

from to_integer import convert_to_integer
from tournament import Tournament


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--create", help="create a new tournament", action="store_true"
    )

    parser.add_argument(
        "-l", "--list", help="list tournaments backups", action="store_true"
    )

    parser.add_argument("-b", "--backup", help="backup tournament",
                        action="store_true")

    parser.add_argument(
        "-r",
        "--restore",
        help="restore selected tournament number",
    )

    parser.add_argument(
        "-a", "--active", help="list active tournament", action="store_true"
    )

    parser.add_argument(
        "-res", "--results", help="enter matchs results", action="store_true"
    )

    parser.add_argument("-n", "--next", help="next tour", action="store_true")

    parser.add_argument(
        "-sc", "--scores", help="print actual players scores",
        action="store_true"
    )

    parser.add_argument(
        "-er", "--editranks", help="update players ranks", action="store_true"
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
        print(f"Ajout du joueur {_} sur {number_of_players}")
        add_player(tournament)
    tournament.save()


def tournament_backup():
    tournament = Tournament({})
    tournament.restore()
    tournament.backup_new()


def tournament_score():
    tournament = Tournament({})
    tournament.restore()
    for _ in tournament.players:
        print(
            f"Joueur: {_.surname} {_.forename} - {tournament.score_player(_)} point(s)."
        )


def update_players_ranks():
    tournament = Tournament({})
    tournament.restore()
    for _ in tournament.players:
        print(f"Joueur: {_.surname} {_.forename} - {_.rank} (actuel)")
        new_rank = input("Nouveau classement: ")
        new_rank = convert_to_integer(new_rank)
        if not new_rank:
            print(
                "Le nouveau classement dois être un entier, on passe au suivant.")
            continue
        else:
            _.rank = new_rank
    tournament.save()


def next_tour():
    tournament = Tournament({})
    tournament.restore()
    tournament.new_tour()


def tournaments_list():
    print(
        "Liste des tournois sauvegardés:\n" "-------------------------------\n")
    db = TinyDB("data/db.json")
    tournaments_table = db.table("tournaments")
    count = 0
    for _ in tournaments_table:
        count += 1
        tournament = Tournament(jsonpickle.decode(_["Tournaments"]).__dict__)
        print(f"{count} - {tournament.name}")


def number_of_tournaments():
    db = TinyDB("data/db.json")
    tournaments_table = db.table("tournaments")
    return len(tournaments_table)


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


def add_player(tournament):
    print(f"Adding a player to {tournament.name}")
    surname = input("Nom: ")
    forename = input("Prénom: ")
    birthday = input("Birthday: ")
    sex = input("Sexe: ")
    rank = input("Rang: ")
    rank = convert_to_integer(rank)
    if not rank:
        print("Le rang dois être un entier.")
        return
    tournament.add_player(
        {
            "surname": surname,
            "forename": forename,
            "birthday": birthday,
            "sex": sex,
            "rank": rank,
        }
    )


def enter_results():
    tournament = Tournament({})
    tournament.restore()

    for match in tournament.tours[tournament.active_tour].matchs:
        print(f"Round {tournament.active_tour}")
        print(
            f"Joueur (Joueur 1): {match.player1.surname} {match.player1.forename}")
        print(
            f"Contre (Joueur 2): {match.player2.surname} {match.player2.forename}")
        match_score = input(
            "1. Joueur 1 gagnant\n" "2. Joueur 2 gagnant\n" "3. Match Null\n"
        )
        match_score = convert_to_integer(match_score)

        if not match_score or match_score < 1 or match_score > 3:
            print("Le score dois être un entier compris entre 1 et 3.")
            return

        if match_score == 1:
            match.score1 = 1
            match.score2 = 0

        if match_score == 2:
            match.score1 = 0
            match.score2 = 1

        if match_score == 3:
            match.score1 = 0.5
            match.score2 = 0.5
    tournament.save()


def main():
    args = parse_arguments()
    if args.create:
        create_tournament()
    if args.list:
        tournaments_list()
    if args.backup:
        tournament_backup()
    if args.restore:
        restore_tournament(args.restore)
    if args.active:
        active_tournament_info()
    if args.results:
        enter_results()
    if args.next:
        next_tour()
    if args.scores:
        tournament_score()
    if args.editranks:
        update_players_ranks()


if __name__ == "__main__":
    main()
