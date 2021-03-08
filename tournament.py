from random import randint

import jsonpickle
from tinydb import TinyDB


class Basic:
    # Define a basic class for heritage, convert a dictionary to class attributes
    def __init__(self, dic):
        for attr_name, attr_value in dic.items():
            setattr(self, attr_name, attr_value)


class Tournament(Basic):
    def __init__(self, dic):
        self.players = []
        self.tours = []
        self.rounds = 4
        self.active_tour = -1
        super().__init__(dic)

    def add_player(self, dic):
        """
        Add a player from a dictionary
        :param dic: player's properties
        :return: Nothing
        """
        self.players.append(Player(dic))

    def new_tour(self):
        '''
        Start a new tour
        :return: Nothing
        '''
        if self.active_tour == self.rounds - 1:
            print("Le tournois est terminé.")
            return
        self.active_tour += 1
        self.tours.append(Tour(self))

    def stop_tour(self):
        '''
        Stop actual tour. Record time and ask for player's scores.
        :return:
        '''
        if self.active_tour == self.rounds - 1:
            print("Le tournois est terminé.")
            return
        for match in self.tours[self.active_tour].matchs:
            print(f"Round {self.active_tour}")
            print(
                f"Joueur (Joueur 1): {match.player1.surname} {match.player1.forename}"
            )
            print(
                f"Contre (Joueur 2): {match.player2.surname} {match.player2.forename}"
            )
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

    def score_player(self, player):
        '''
        Return player score
        :param player:
        :return: player's score (float)
        '''
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

    def played_togethers(self, player1, player2):
        '''
        Return True if players ever played together False if not
        :param player1:
        :param player2:
        :return: True / False
        '''
        for _ in self.tours:
            for match in _.matchs:
                score_total = 0
                # Match for player1
                if (match.player1.surname == player1.surname) and (
                        match.player1.forename == player1.forename
                ) or (match.player2.surname == player1.surname) and (match.player2.forename == player1.forename):
                    score_total += 1

                # Match for player2
                if (match.player1.surname == player2.surname) and (
                        match.player1.forename == player2.forename) or (match.player2.surname == player2.surname) and (
                        match.player2.forename == player2.forename
                ):
                    score_total += 1
                if score_total == 2:
                    return True
        return False

    def save(self):
        '''
        Save tournament state (actual one)
        :return: Nothing
        '''
        db = TinyDB("data/db.json")
        at_table = db.table("active_tournament")
        at_table.truncate()
        dic = {"Actual": jsonpickle.encode(self)}
        at_table.insert(dic)

    def restore(self):
        '''
        Restore actual tournament from the database
        :return: Nothing
        '''
        db = TinyDB("data/db.json")
        at_table = db.table("active_tournament")
        self.__dict__.update(jsonpickle.decode(at_table.all()[0]["Actual"]).__dict__)


class Tour:
    def __init__(self, tournament):
        self.matchs = []
        self.tournament = tournament
        self.title = f"Round {self.tournament.active_tour + 1}"

        players_unordered = self.tournament.players
        self.ranked_players = sorted(
            players_unordered,
            key=lambda ordering_value: (ordering_value.rank,
                                        tournament.score_player(ordering_value))
        )
        self.ranked_players.reverse()

        print("Création des matchs")
        self.matchs_list()

    def matchs_list(self):
        """
        Generate the matchs list for the round
        :return:
        """
        out_of_players = False
        players_cursor = 0

        len_players_list = len(self.ranked_players)
        median = int(len_players_list / 2)

        # Prevent from playing the same match
        for _ in range(median):

            player1 = self.ranked_players[_]
            player2 = self.ranked_players[_ + median]

            while self.tournament.played_togethers(player1, player2) or out_of_players:

                if (_ + median + players_cursor) < (len_players_list - 1):
                    players_cursor += 1
                    # If players played together, then we swap players in the list
                    (self.ranked_players[_ + median],
                     self.ranked_players[_ + median + players_cursor]) = (
                        self.ranked_players[_ + median + players_cursor],
                        self.ranked_players[_ + median])
                    player2 = self.ranked_players[_ + median]
                else:
                    out_of_players = True

            # Don't forget to re-initialize the players cursor for next match...
            players_cursor = 0

            print(
                f"Match {_ + 1} : {player1.surname} "
                f"{player2.surname}"
            )
            self.matchs.append(
                Match(
                    {
                        "player1": player1,
                        "player2": player2,
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
        tournois.stop_tour()
        print(
            f"Affichage du score {tournois.players[0].surname} {tournois.players[0].forename}"
        )
        print(f"Score: {tournois.score_player(tournois.players[0])}")


#     test002(tournois)
#
#
# def test002(tournois):
#     # Serialize
#     print("Sérialisation\n")
#     tournois_serialize = jsonpickle.encode(tournois)
#     print(tournois_serialize)
#     # Unserialize
#     print("Desérialisation\n")
#     new_tournois = jsonpickle.decode(tournois_serialize)
#     for _ in new_tournois.tours:
#         print(_.title)
#     new_tournois.save()
#     new_tournois.restore()
#     # Après sérialization et déserialization
#     for _ in new_tournois.tours:
#         print(_.title)
#     print(
#         f"Affichage du score {tournois.players[0].surname} {tournois.players[0].forename}"
#     )
#     print(f"Score: {tournois.score_player(tournois.players[0])}")


if __name__ == "__main__":
    test()
