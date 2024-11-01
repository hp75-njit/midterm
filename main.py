from calculator.repl import CalculatorREPL
from calculator.logger_config import logger

def main():
    logger.info("Starting Calculator REPL...")
    repl = CalculatorREPL()
    repl.run()

if __name__ == "__main__":
    main()