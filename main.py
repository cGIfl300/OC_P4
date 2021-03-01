import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--create",
        help="create a new tournament",
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


def main():
    args = parse_arguments()
    if args.create:
        pass


if __name__ == "__main__":
    main()
