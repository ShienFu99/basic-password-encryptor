import argparse

def main():
    parser = argparse.ArgumentParser(description="Testing exclusivity")

    group = parser.add_mutually_exclusive_group()

    group.add_argument("-n", default=3, help="number of symbols per encrypt_symbol - between 2 and 7 (inclusive)", type=int)
    group.add_argument("-r", help="reuse previous scheme", action='store_true')
    group.add_argument("-d", help="decrypt a previously encrypted message", action='store_true')

    args = parser.parse_args()

    if args.n:
        print(args.n)

    if args.r:
        print("-r used")
    elif args.d:
        print("-d used")


if __name__ == "__main__":
    main()
