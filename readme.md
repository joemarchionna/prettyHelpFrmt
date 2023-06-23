prettyHelpFrmt - Python argparse HelpFormatter
==============================================
argparse HelpFormatter-derived class that helps with text alignment
when the -h argparse switch is invoked. It left aligns the second set
of actions for each switch based on a code-supplied constant</p>
Based on the code here: [argparse](https://hg.python.org/cpython/file/3.5/Lib/argparse.py)

Dependancies
============
This project uses the following projects:

* argparse

Use
===
see the file <b>prettyHelpFrmt/cmdPretty.py</b> to see the formatter code used</p>

the file <b>prettyHelpFrmt/cmdOriginal.py</b> the originally-supplied help formatter</p>

Both run the same command switches, see the example output below. Note that if using sub_parsers, you 
need to specifiy the formatter_class when creating the sub_parser, otherwise the help for the 
sub_parser will revert back to the default HelpFormatter


Example
=======

![bash example](https://user-images.githubusercontent.com/52943266/61336414-3a697680-a7ff-11e9-8404-ea1990d8d851.png)
