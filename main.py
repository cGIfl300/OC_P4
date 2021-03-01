import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--create",
        help="create a new tournament",
    )


def main():
    args = parse_arguments()
    if args.create:
        pass


if __name__ == "__main__":
    main()
