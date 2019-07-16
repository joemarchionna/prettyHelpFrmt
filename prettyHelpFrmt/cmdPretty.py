import sys

sys.path.append(".")
from prettyHelpFrmt.prettyHelpFormatter import PrettyHelpFormatter
import prettyHelpFrmt.createArgs as createArgs
import argparse

if __name__ == "__main__":
    formatter = lambda prog: PrettyHelpFormatter(
        prog, max_help_position=80, actionSeparation=22
    )
    parser = argparse.ArgumentParser(
        description="Pretty Command Parser", formatter_class=formatter
    )

    createArgs.getBaseArgs(parser)
    createArgs.addInputArgs(parser)
    parser.print_help()
