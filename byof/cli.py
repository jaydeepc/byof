"""


byof - Build Your Own Framework
.. A tool to auto generate REST API framework

Usage:
  byof initialise
  byof -h | --help
  byof --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.



"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import byof.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items(): 
        if hasattr(byof.commands, k) and v:
            module = getattr(byof.commands, k)
            byof.commands = getmembers(module, isclass)
            command = [command[1] for command in byof.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
