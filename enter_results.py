from to_integer import convert_to_integer
from tournament import Tournament


def enter_results():
    tournament = Tournament({})
    tournament.restore()

    for match in tournament.tours[tournament.active_tour].matchs:
        print(f"Round {tournament.active_tour}")
        print(
            f"Joueur (Joueur 1): {match.player1.surname} "
            f"{match.player1.forename}")
        print(
            f"Contre (Joueur 2): {match.player2.surname} "
            f"{match.player2.forename}")
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
