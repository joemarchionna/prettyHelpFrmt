prettyHelpFrmt - Python argparse HelpFormatter
==============================================
argparse HelpFormatter-derived class that helps with text alignment
when the -h argparse switch is invoked. It left aligns the second set
of actions for each switch based on a code-supplied constant</p>
Based on the code here: [argparse](https://hg.python.org/cpython/file/3.5/Lib/argparse.py)

Installation
============
To install this project in another project run the following command::
pip install git+ssh://git@github.com/joemarchionna/prettyHelpFrmt.git

Dependancies
============
This project uses the following projects:

* argparse

Use
===
see the file prettyHelpFrmt/cmdPretty.py
to see the formatter code used</p>

the file prettyHelpFrmt/cmdOriginal.py is the same switches used with the
originally-supplied help formatter
