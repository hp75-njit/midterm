import pandas as pd
import os
from datetime import datetime
from calculator.logger_config import logger

class HistoryManager:
    def __init__(self):
        self.history = pd.DataFrame(columns=["operation", "inputs", "result", "timestamp"])
        self.history_file = "calculator/history.csv"
        logger.info("HistoryManager initialized with history file: %s", self.history_file)

    def add_entry(self, operation, inputs, result):
        # Create a new entry as a dictionary
        entry = pd.DataFrame({
            "operation": [operation],
            "inputs": [inputs],
            "result": [result],
            "timestamp": [pd.Timestamp.now()]
        })
        self.history = pd.concat([self.history, entry], ignore_index=True)
        logger.debug("Added in history: %s", entry)

    def save(self):
        try:
            print(self.history)
            logger.info("Saving history to file: %s", self.history_file)
            self.history.to_csv(self.history_file, index=False)
            logger.info("History saved successfully.")
        except Exception as e:
            logger.error("Error saving history: %s", e)

    def load(self):
        if os.path.exists(self.history_file):
            self.history = pd.read_csv(self.history_file)
            logger.info("History loaded from file: %s", self.history_file)
            print(self.history)
        else:
            logger.warning("No history file found.")

    def clear(self):
        self.history = pd.DataFrame(columns=["operation", "inputs", "result", "timestamp"])
        logger.debug("History cleared.")

    def show_history(self):
        print(self.history)