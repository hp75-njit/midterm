import sys
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, HistoryCommand
from calculator.plugin_loader import PluginLoader
from calculator.history_manager import HistoryManager
from calculator.logger_config import logger

class CalculatorREPL:
    def __init__(self):
        self.history_manager = HistoryManager()
        self.plugin_loader = PluginLoader()
        self.commands = {
            'add': AddCommand(self.history_manager),
            'subtract': SubtractCommand(self.history_manager),
            'multiply': MultiplyCommand(self.history_manager),
            'divide': DivideCommand(self.history_manager),
            'history': HistoryCommand(self.history_manager),
            'menu': self.show_menu
        }
        self.load_plugins()

    def load_plugins(self):
        for name, command in self.plugin_loader.load_plugins().items():
            self.commands[name] = command

    def show_menu(self):
        print("Available commands:")
        for command in self.commands.keys():
            print(f"- {command}")

    def run(self):
        while True:
            user_input = input("> ").strip().split()
            if not user_input:
                continue

            command_name = user_input[0]
            args = user_input[1:]

            if command_name == "exit":
                logger.info("Exiting...")
                sys.exit()

            command = self.commands.get(command_name)
            if command:
                command.execute(args)
            else:
                logger.debug("Unknown command. Type 'menu' for available commands.")