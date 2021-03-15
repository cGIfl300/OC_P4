from random import randint


def simulate_match(tournament):
    for match in tournament.tours[tournament.active_tour].matchs:
        print(f"Simulating Round {tournament.active_tour +1}")
        print(
            f"Joueur (Joueur 1): {match.player1.surname} "
            f"{match.player1.forename}")
        print(
            f"Contre (Joueur 2): {match.player2.surname} "
            f"{match.player2.forename}")
        # match_score = input("1. Joueur 1 gagnant\n"
        #                     "2. Joueur 2 gagnant\n"
        #                     "3. Match Null\n")
        match_score = randint(1, 3)
        if match_score == 1:
            match.score1 = 1
            match.score2 = 0

        if match_score == 2:
            match.score1 = 0
            match.score2 = 1

        if match_score == 3:
            match.score1 = 0.5
            match.score2 = 0.5
