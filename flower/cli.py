#!/usr/bin/env python3

import pathlib
import argparse

parser = argparse.ArgumentParser(description="flower — a simple, declarative video editor")

def parse_args():
    parser.add_argument(
        "-i",
        "--init",
        metavar="PROJECT",
        help="Initialize a new project directory",
        nargs=1,
        type=str
    )

    parser.add_argument(
        "-o",
        "--order",
        metavar="ORDERFILE",
        help="""Order file to use (Default: order.yaml)""",
        default="order.yaml",
        nargs=1,
        type=str
    )

    parser.add_argument(
        "-w",
        "--write",
        metavar="OUTPUTFILE",
        help="""Output video filename (default: output.mp4)""",
        default="output.mp4",
        nargs=1,
        type=str
    )

    return parser.parse_args()

def main():
    args = parse_args()
    print(args)

if __name__ == "__main__":
    main()
