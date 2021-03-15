from active_tournament_info import active_tournament_info
from create_tournament import create_tournament
from enter_results import enter_results
from next_tour import next_tour
from parse_arguments import parse_arguments
from restore_tournament import restore_tournament
from sorted_by_names import sorted_by_names
from sorted_by_rank import sorted_by_rank
from tournament_backup import tournament_backup
from tournament_score import tournament_score
from tournaments_list import tournaments_list
from update_players_ranks import update_players_ranks


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
    if args.sortedbyrank:
        sorted_by_rank()
    if args.sortedbynames:
        sorted_by_names()


if __name__ == "__main__":
    main()
