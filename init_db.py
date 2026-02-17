from pathlib import Path
from db import get_connection

BASE_DIR = Path(__file__).resolve().parent

def run_sql_file(path: Path) -> None:
    conn = get_connection()
    try:
        conn.executescript(path.read_text(encoding="utf-8"))
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def main():
    run_sql_file(BASE_DIR / "schema.sql")
    run_sql_file(BASE_DIR / "seed.sql")
    print("OK: DB initialized")

if __name__ == "__main__":
    main()
