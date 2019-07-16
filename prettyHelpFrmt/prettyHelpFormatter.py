import argparse
import os
import re

# This was modified based on the the following:
# https://hg.python.org/cpython/file/3.5/Lib/argparse.py
class PrettyHelpFormatter(argparse.HelpFormatter):
    """Help Formatter for argparse library which increases readability of
    -h help command; actionSeparation is equal to the spacing to be put
    between actions (-a and --action for example), the original value for
    argparse was 2, which is the default for this implementation
    
    usage:
    formatter = lambda prg: PrettyHelpFormatter(prg)
    parser = argparse.ArgumentParser(description="Command Parser", formatter_class=formatter)
    """
    def __init__(
        self,
        prog,
        indent_increment=4,
        max_help_position=80,
        width=160,
        actionSeparation=2,
    ):
        super().__init__(prog, indent_increment, max_help_position, width)
        # changes Joe Marchionna 2019 07 15
        self.actionSeparation = actionSeparation

    def _format_action_invocation(self, action):
        if not action.option_strings:
            default = self._get_default_metavar_for_positional(action)
            metavar, = self._metavar_formatter(action, default)(1)
            return metavar

        else:
            parts = []

            # if the Optional doesn't take a value, format is:
            #    -s, --long
            if action.nargs == 0:
                parts.extend(action.option_strings)

            # if the Optional takes a value, format is:
            #    -s ARGS, --long ARGS
            else:
                default = self._get_default_metavar_for_optional(action)
                args_string = self._format_args(action, default)
                for option_string in action.option_strings:
                    parts.append("%s %s" % (option_string, args_string))

            # changes by Joe Marchionna 2019 07 15
            # the following is new, length is equal to the number of spaces to be added
            # after the first action, where 2 spaces is the absolute minimum
            length = self.actionSeparation
            if parts[0].startswith("--"):
                parts[0] = (
                    "{message:{fill}>{width}}".format(
                        message="", fill=" ", width=length
                    )
                    + parts[0]
                )
            length = max(2, (self.actionSeparation - len(parts[0])))

            # actually create the text
            separation = "{message:{fill}<{width}}".format(
                message=",", fill=" ", width=length
            )
            return separation.join(parts)
