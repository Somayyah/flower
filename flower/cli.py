#!/usr/bin/env python3

from pathlib import Path
import argparse

media_directory = ["audio", "images", "subtitles", "videos"]

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
        type=str,
    )

    return parser.parse_args()

def create_skeleton_project(init=None, order=None):
    if init is None:
        print('No project name provided, using "project" instead')
        init = 'project'

    print(f"Initializing {init}...")
    project_path = Path.cwd() / init
    project_path.mkdir(parents=True, exist_ok=True)

    for sub in media_directory:
        (project_path / "media" / sub).mkdir(parents=True, exist_ok=True)

    if order is None:
        order = 'order.yaml'
    elif not order.endswith(".yaml"):
        order += ".yaml"
    
    order_file = project_path / order
    if not order_file.exists():
        order_file.write_text("# Define your video order here\n")
        print(f"Created order file: {order_file}")
    else:
        print(f"Order file already exists: {order_file}")

def main():
    args = parse_args()

    if args.order:
        pass

    if args.write:
        pass

    if args.project:
        print(args.project)
    elif args.init:
        create_skeleton_project(args.init, args.order)


if __name__ == "__main__":
    main()
