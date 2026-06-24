import logging
from pathlib import Path

def get_logger() -> logging.Logger:
    Path("logs").mkdir(exist_ok=True)

    logger = logging.getLogger("football_ai")
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("logs/commands.log", encoding="utf-8")
    fh.setFormatter(logging.Formatter("%(asctime)s | %(message)s"))
    logger.addHandler(fh)
    return logger