from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_TYPE = "sqlite"
DB_PATH = str(BASE_DIR / "football.db")
