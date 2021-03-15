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
        self.name = "Untilted"
        super().__init__(dic)

    def add_player(self, dic):
        """
        Add a player from a dictionary
        :param dic: player's properties
        :return: Nothing
        """
        self.players.append(Player(dic))

    def new_tour(self):
        """
        Start a new tour
        :return: Nothing
        """
        if self.active_tour == self.rounds - 1:
            print("Le tournois est terminé.")
            return False
        self.active_tour += 1
        self.tours.append(Tour(self))
        self.save()
        return True

    def stop_tour(self):
        """
        Stop actual tour. Record time and ask for player's scores.
        :return:
        """
        if self.active_tour == self.rounds - 1:
            print("Le tournois est terminé.")
            return

    def score_player(self, player):
        """
        Return player score
        :param player:
        :return: player's score (float)
        """
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
        """
        Return True if players ever played together False if not
        :param player1:
        :param player2:
        :return: True / False
        """
        for _ in self.tours:
            for match in _.matchs:
                score_total = 0
                # Match for player1
                if (
                        (match.player1.surname == player1.surname)
                        and (match.player1.forename == player1.forename)
                        or (match.player2.surname == player1.surname)
                        and (match.player2.forename == player1.forename)
                ):
                    score_total += 1

                # Match for player2
                if (
                        (match.player1.surname == player2.surname)
                        and (match.player1.forename == player2.forename)
                        or (match.player2.surname == player2.surname)
                        and (match.player2.forename == player2.forename)
                ):
                    score_total += 1
                if score_total == 2:
                    return True
        return False

    def save(self):
        """
        Save tournament state (actual one)
        :return: Nothing
        """
        db = TinyDB("data/db.json")
        at_table = db.table("active_tournament")
        at_table.truncate()
        dic = {"Actual": jsonpickle.encode(self)}
        at_table.insert(dic)

    def restore(self):
        """
        Restore actual tournament from the database
        :return: Nothing
        """
        db = TinyDB("data/db.json")
        at_table = db.table("active_tournament")
        # Try to restore tournament, is none, just ignore it will be created later.
        try:
            self.__dict__.update(
                jsonpickle.decode(at_table.all()[0]["Actual"]).__dict__
            )
        except IndexError:
            pass

    def backup_new(self):
        """
        Add a tournament backup
        :return: Nothing
        """
        db = TinyDB("data/db.json")
        at_table = db.table("tournaments")
        dic = {"Tournaments": jsonpickle.encode(self)}
        at_table.insert(dic)

    def list_players_by_rank(self):
        players_unordered = self.players
        ranked_players = sorted(
            players_unordered,
            key=lambda ordering_value: (
                ordering_value.rank,
                self.score_player(ordering_value),
            ),
        )
        ranked_players.reverse()
        return ranked_players

    def list_players_by_names(self):
        players_unordered = self.players
        ranked_players = sorted(
            players_unordered,
            key=lambda ordering_value: (
                ordering_value.surname,
                ordering_value.forename,
            ),
        )
        return ranked_players


class Tour:
    def __init__(self, tournament):
        self.matchs = []
        self.tournament = tournament
        self.title = f"Round {self.tournament.active_tour + 1}"

        players_unordered = self.tournament.players
        self.ranked_players = sorted(
            players_unordered,
            key=lambda ordering_value: (
                ordering_value.rank,
                tournament.score_player(ordering_value),
            ),
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

            while self.tournament.played_togethers(player1,
                                                   player2) or out_of_players:

                if (_ + median + players_cursor) < (len_players_list - 1):
                    players_cursor += 1
                    # If players played together, then we swap players in the list
                    (
                        self.ranked_players[_ + median],
                        self.ranked_players[_ + median + players_cursor],
                    ) = (
                        self.ranked_players[_ + median + players_cursor],
                        self.ranked_players[_ + median],
                    )
                    player2 = self.ranked_players[_ + median]
                else:
                    out_of_players = True

            # Don't forget to re-initialize the players cursor for next match...
            players_cursor = 0

            print(f"Match {_ + 1} : {player1.surname} " f"{player2.surname}")
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
