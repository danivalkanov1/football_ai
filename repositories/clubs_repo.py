import sqlite3
from db import execute, fetch_all, fetch_one

def add_club(name: str, city: str | None = None) -> int:
    name = (name or "").strip()
    if not name:
        raise ValueError("name is required")

    try:
        last_id, _ = execute(
            "INSERT INTO clubs (name, city) VALUES (?, ?)",
            (name, city),
        )
        return int(last_id)
    except sqlite3.IntegrityError as e:
        raise ValueError("club name already exists") from e

def list_clubs() -> list[dict]:
    return fetch_all("SELECT id, name, city FROM clubs ORDER BY name")

def get_club_by_id(club_id: int) -> dict | None:
    return fetch_one(
        "SELECT id, name, city FROM clubs WHERE id = ?",
        (club_id,),
    )

def find_club_by_name(name: str) -> dict | None:
    return fetch_one(
        "SELECT id, name, city FROM clubs WHERE name = ?",
        (name,),
    )

def update_club(club_id: int, name: str, city: str | None = None) -> int:
    if not isinstance(club_id, int) or club_id <= 0:
        raise ValueError("invalid club_id")

    name = (name or "").strip()
    if not name:
        raise ValueError("name is required")

    try:
        _, affected = execute(
            "UPDATE clubs SET name = ?, city = ? WHERE id = ?",
            (name, city, club_id),
        )
        return int(affected)
    except sqlite3.IntegrityError as e:
        raise ValueError("club name already exists") from e

def delete_club(club_id: int) -> int:
    if not isinstance(club_id, int) or club_id <= 0:
        raise ValueError("invalid club_id")

    try:
        _, affected = execute("DELETE FROM clubs WHERE id = ?", (club_id,))
        return int(affected)
    except sqlite3.IntegrityError as e:
        raise ValueError("cannot delete club (FK constraint)") from e
