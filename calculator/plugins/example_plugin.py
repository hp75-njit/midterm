# calculator/plugins/example_plugin.py
from calculator.commands import Command

class ExamplePluginCommand(Command):
    def execute(self, args):
        print("Example plugin executed with args:", args)

plugin = ExamplePluginCommand()

