import jsonpickle
from tinydb import TinyDB


class Basic:
    # Define a basic class for heritage
    def __init__(self, dic):
        for attr_name, attr_value in dic.items():
            setattr(self, attr_name, attr_value)


class Tournament(Basic):
    def __init__(self, dic):
        super().__init__(dic)
        self.players = []
        self.tours = []
        self.rounds = 4
        self.active_tour = -1

    def add_player(self, dic):
        self.players.append(Player(dic))

    def new_tour(self):
        if self.active_tour == self.rounds - 1:
            print("Le tournois est terminé.")
            return
        self.active_tour += 1
        self.tours.append(Tour(self))

    def score_player(self, player):
        score_total = 0
        for _ in self.tours:
            for match in _.matchs:
                if (match.player1.surname == player.surname) and (
                    match.player1.forename == player.forename
                ):
                    score_total += match.score1
                if (match.player2.surname == player.surname) and (
                    match.player2.forename == player.forename
                ):
                    score_total += match.score2
        return score_total

    def save(self):
        db = TinyDB("data/db.json")
        at_table = db.table("active_tournament")
        at_table.truncate()
        dic = {"Actual": jsonpickle.encode(self)}
        at_table.insert(dic)


def restore():
    db = TinyDB("data/db.json")
    at_table = db.table("active_tournament")
    return jsonpickle.decode(at_table.all()[0]["Actual"])


class Tour:
    def __init__(self, tournament):
        self.matchs = []
        self.tournament = tournament
        self.title = f"Round {self.tournament.active_tour + 1}"
        players_unordered = self.tournament.players
        self.ranked_players = sorted(
            players_unordered, key=lambda ordering_value: ordering_value.rank
        )
        self.ranked_players.reverse()

        print("Création des matchs")
        len_players_list = len(self.ranked_players)
        median = int(len_players_list / 2)
        for _ in range(median):
            print(
                f"Match {_} : {self.ranked_players[_].surname} {self.ranked_players[_ + median].surname}"
            )
            self.matchs.append(
                Match(
                    {
                        "player1": self.ranked_players[_],
                        "player2": self.ranked_players[_ + median],
                        "score1": 0,
                        "score2": 0,
                    }
                )
            )


class Match(Basic):
    def __init__(self, dic):
        super().__init__(dic)


class Player(Basic):
    def __init__(self, dic):
        super().__init__(dic)


def test():
    tournois = Tournament({"colibri": "pamplemousse"})
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
            "surname": "MALFOY",
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
    for player in tournois.players:
        print(player.surname)
    for _ in range(tournois.rounds + 1):
        print(f"Tour numéro {_ + 1}")
        tournois.new_tour()

    # Serialize
    print("Sérialisation\n")
    tournois_serialize = jsonpickle.encode(tournois)
    print(tournois_serialize)

    # Unserialize
    print("Desérialisation\n")
    new_tournois = jsonpickle.decode(tournois_serialize)
    for _ in new_tournois.tours:
        print(_.title)

    new_tournois.save()
    new_tournois = restore()

    print("Après unserialization")
    for _ in new_tournois.tours:
        print(_.title)


if __name__ == "__main__":
    test()
