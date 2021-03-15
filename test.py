from simulate_matchs import simulate_match
from tournament import Tournament


def test():
    print("Création d'un tournois de 4 rounds avec 8 joueurs.")
    rounds_to_test = 4
    tournois = Tournament({"rounds": rounds_to_test})
    properties = [
        {
            "surname": "DUPUIS",
            "forename": "Mélanie",
            "birthday": 22,
            "sex": False,
            "rank": 1092,
        },
        {
            "surname": "DUBOIS",
            "forename": "Natasha",
            "birthday": 20,
            "sex": False,
            "rank": 1083,
        },
        {
            "surname": "MARK",
            "forename": "Henry",
            "birthday": 42,
            "sex": True,
            "rank": 2093,
        },
        {
            "surname": "MALORY",
            "forename": "Lucie",
            "birthday": 45,
            "sex": False,
            "rank": 2099,
        },
        {
            "surname": "DUCHATEAU",
            "forename": "Edouard",
            "birthday": 57,
            "sex": True,
            "rank": 1021,
        },
        {
            "surname": "ARMAND",
            "forename": "Jacques",
            "birthday": 37,
            "sex": True,
            "rank": 2097,
        },
        {
            "surname": "LOPEZ",
            "forename": "Julia",
            "birthday": 19,
            "sex": False,
            "rank": 2000,
        },
        {
            "surname": "LYNCH",
            "forename": "David",
            "birthday": 99,
            "sex": True,
            "rank": 1999,
        },
    ]
    for _ in properties:
        tournois.add_player(_)

    # Testing object properties (player's name)
    # for player in tournois.players:
    #     print(player.surname)

    print("Jouer les tournois et simuler les résultats.")

    for _ in range(tournois.rounds + 1):
        print(f"Tour numéro {_ + 1}")
        if not tournois.new_tour():
            return
        tournois.stop_tour()
        simulate_match(tournois)
        print("\nAffichage des résultats des joueurs:"
              "\n------------------------------------")
        for player in tournois.players:
            print(
                f"Affichage du score de {player.surname}"
                f" {player.forename}: {tournois.score_player(player)}"
            )


if __name__ == "__main__":
    test()
