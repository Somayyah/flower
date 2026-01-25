#!/usr/bin/env python3

import pathlib
import argparse

class CustomFormatter(
    argparse.ArgumentDefaultsHelpFormatter,
    argparse.RawTextHelpFormatter
):
    pass

def parse_args():

    parser = argparse.ArgumentParser(
        description="🌷 flower — a simple, declarative video editor 🌷",
        formatter_class=CustomFormatter,
        epilog = "Example:\n  flower -i my_project -o order.yaml -w final.mp4"
    )

    parser.add_argument(
        "-i",
        "--init",
        metavar="PROJECT",
        help="Initialize a new project directory",
        type=str,
    )

    parser.add_argument(
        "-o",
        "--order",
        metavar="ORDERFILE",
        help="Order file to use",
        default="order.yaml",
        type=str,
    )

    parser.add_argument(
        "-w",
        "--write",
        metavar="OUTPUTFILE",
        help="""Output video filename""",
        default="output.mp4",
        type=str,
    )

    parser.add_argument(
        "-p",
        "--project",
        metavar="PROJECTDIR",
        help="""Project directory to render""",
        default="media",
        type=str,
    )

    return parser.parse_args()

def create_skeleton_project(order=None, write=None, project=None):
    
    pass

def main():
    args = parse_args()

    if args.order:
        pass

    if args.write:
        pass

    if args.project:
        pass

    if args.init:
        create_skeleton_project()


if __name__ == "__main__":
    main()
