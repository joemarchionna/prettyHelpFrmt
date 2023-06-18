import sys
import argparse


def getBaseArgs(parser, configOptions=["prod", "test"], defaultConfigOption="test"):
    lp = parser.add_mutually_exclusive_group()

    lp.add_argument(
        "-q",
        "--quiet",
        help="Quiet, Produce Almost No Logging",
        action="store_true",
        default=False,
    )

    lp.add_argument(
        "-v",
        "--verbose",
        help="Verbose, Produce Excessive Logging",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "-n",
        "--dryrun",
        help="No Changes, Ie, Perform A 'Dry Run'",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "-c",
        "--config",
        choices=configOptions,
        help="Configuration 'name' To Use, Default: '" + defaultConfigOption + "', Options: " + ", ".join(configOptions),
        metavar="name",
        default=defaultConfigOption,
    )

    parser.add_argument("--magic", help="Use black-box magic", action="store_true", default=False)

    return parser


def addInputArgs(parser):
    inputGrp = parser.add_mutually_exclusive_group()
    inputGrp.add_argument(
        "-l",
        "--list",
        help="List, Get Items As Space-Delimited List From The Command Line",
        metavar="items",
        type=str,
        nargs="+",
        default=None,
    )
    inputGrp.add_argument(
        "-f",
        "--file",
        help="File Path, Get Items To Work On From A File, Each Line An Item",
        metavar="filepath",
        type=str,
        default=None,
    )
