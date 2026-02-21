import argparse


def main() -> None:
    parser = argparse.ArgumentParser(prog="cem", description="Cem Utilities CLI (starter).")
    sub = parser.add_subparsers(dest="cmd", required=True)

    hello = sub.add_parser("hello", help="Print a hello message")
    hello.add_argument("--name", default="Cem", help="Name to greet")

    args = parser.parse_args()

    if args.cmd == "hello":
        print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
