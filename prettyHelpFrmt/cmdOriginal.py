import sys

sys.path.append(".")
from prettyHelpFrmt.prettyHelpFormatter import PrettyHelpFormatter
import prettyHelpFrmt.createArgs as createArgs
import argparse

if __name__ == "__main__":
    formatter = lambda prog: argparse.HelpFormatter(prog, max_help_position=80)
    parser = argparse.ArgumentParser(description="Original Command Parser", formatter_class=formatter)

    createArgs.getBaseArgs(parser)
    createArgs.addInputArgs(parser)
    parser.print_help()
