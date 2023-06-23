import sys

sys.path.append(".")
from prettyHelpFrmt.prettyHelpFormatter import PrettyHelpFormatter
import prettyHelpFrmt.createArgs as createArgs
import argparse

if __name__ == "__main__":
    formatter = lambda prog: PrettyHelpFormatter(prog, max_help_position=70, actionSeparation=30)
    parser = argparse.ArgumentParser(description="Pretty Command Parser", formatter_class=formatter)

    createArgs.getBaseArgs(parser)
    createArgs.addInputArgs(parser)
    createArgs.addSubParsers(parser, formatterClass=formatter)
    parser.parse_args()
