from db import get_connection, fetch_one
from datetime import datetime


def _get_player(name):
    return fetch_one("SELECT * FROM players WHERE full_name = ?", (name,))


def _get_club(name):
    return fetch_one("SELECT * FROM clubs WHERE name = ?", (name,))


def _validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except:
        raise ValueError("Невалидна дата (YYYY-MM-DD)")


def transfer_player(player_name, from_club, to_club, date, fee=None):
    player = _get_player(player_name)
    if not player:
        raise ValueError("Няма такъв играч")

    to = _get_club(to_club)
    if not to:
        raise ValueError("Няма такъв клуб (to)")

    _validate_date(date)

    conn = get_connection()
    try:
        cur = conn.cursor()

        # FROM логика
        if from_club:
            frm = _get_club(from_club)
            if not frm:
                raise ValueError("Няма такъв клуб (from)")

            if player["club_id"] != frm["id"]:
                raise ValueError("Играчът не е в този клуб")

            from_id = frm["id"]
        else:
            if player["club_id"] is not None:
                raise ValueError("Играчът има клуб, трябва да се посочи from")
            from_id = None

        if from_id == to["id"]:
            raise ValueError("from и to са еднакви")

        # INSERT transfer
        cur.execute("""
            INSERT INTO transfers (player_id, from_club_id, to_club_id, transfer_date, fee)
            VALUES (?, ?, ?, ?, ?)
        """, (player["id"], from_id, to["id"], date, fee))

        # UPDATE player club
        cur.execute("""
            UPDATE players SET club_id = ? WHERE id = ?
        """, (to["id"], player["id"]))

        conn.commit()

        return f"OK: {player_name} → {to_club} ({date})"

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        conn.close()


def list_transfers_by_player(player_name):
    player = _get_player(player_name)
    if not player:
        raise ValueError("Няма такъв играч")

    conn = get_connection()
    rows = conn.execute("""
        SELECT t.transfer_date, c1.name as from_club, c2.name as to_club, t.fee
        FROM transfers t
        LEFT JOIN clubs c1 ON t.from_club_id = c1.id
        LEFT JOIN clubs c2 ON t.to_club_id = c2.id
        WHERE t.player_id = ?
        ORDER BY t.transfer_date DESC
    """, (player["id"],)).fetchall()
    conn.close()

    return rows