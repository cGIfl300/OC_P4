import argparse


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

    parser.add_argument(
        "-srank", "--sortedbyrank", help="print players ordered by ranks",
        action="store_true"
    )

    parser.add_argument(
        "-snames", "--sortedbynames", help="print players ordered by names",
        action="store_true"
    )

    return parser.parse_args()
