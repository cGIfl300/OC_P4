from to_integer import convert_to_integer


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
