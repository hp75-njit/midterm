from abc import ABC, abstractmethod
from calculator.history_manager import HistoryManager
from calculator.logger_config import logger

class Command(ABC):
    @abstractmethod
    def execute(self, args):
        pass

class AddCommand(Command):
    def __init__(self, history_manager):
        self.history_manager = history_manager
        
    def execute(self, args):
        # Log the start of execution with arguments
        logger.info("Executing AddCommand with args: %s", args) 
        result = sum(map(float, args))
        # Log the result
        logger.debug("AddCommand result: %f", result) 
        # Logic to save result to history
        self.history_manager.add_entry("add", args, result)

class SubtractCommand(Command):
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self, args):
        # Log the start of execution with arguments
        logger.info("Executing SubtractCommand with args: %s", args)
        result = float(args[0]) - float(args[1])
        # Log the result
        logger.debug("SubtractCommand result: %f", result) 
        # Logic to save result to history
        self.history_manager.add_entry("subtract", args, result)

class MultiplyCommand(Command):
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self, args):
        # Log the start of execution with arguments
        logger.info("Executing MultiplyCommand with args: %s", args) 
        result = float(args[0]) * float(args[1])
        # Log the result
        logger.debug("MultiplyCommand result: %f", result)
        # Logic to save result to history
        self.history_manager.add_entry("multiply", args, result)

class DivideCommand(Command):
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self, args):
        # Log the start of execution with arguments
        logger.info("Executing DivideCommand with args: %s", args) 
        try:
            result = float(args[0]) / float(args[1])
            # Log the result
            logger.debug("DivideCommand result: %f", result)
            # Logic to save result to history
            self.history_manager.add_entry("divide", args, result)
        except ZeroDivisionError:
            logger.error("Error: Division by zero")

class HistoryCommand(Command):
    def __init__(self, history_manager: HistoryManager):
        self.history_manager = history_manager

    def execute(self, args):
        if args and args[0] == "save":
            self.history_manager.save()
        elif args and args[0] == "clear":
            self.history_manager.clear()
        elif args and args[0] == "load":
            self.history_manager.load()
        else:
            self.history_manager.show_history()