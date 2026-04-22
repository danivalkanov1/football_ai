import re
import sqlite3
from db import execute, fetch_all, fetch_one

ALLOWED_POSITIONS = {"GK", "DF", "MF", "FW"}
ALLOWED_STATUS = {"ACTIVE", "INJURED", "SUSPENDED", "RETIRED", "FREE_AGENT"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def _clean(s: str | None) -> str | None:
	if s is None:
		return None
	return re.sub(r"\s+", " ", s.strip())

def _validate_position(position: str) -> str:
	p = (_clean(position) or "").upper()
	if p not in ALLOWED_POSITIONS:
		raise ValueError("позицията трябва да е GK, DF, MF или FW")
	return p

def _validate_status(status: str | None) -> str:
	if status is None:
		return "ACTIVE"
	st = (_clean(status) or "").upper()
	if st not in ALLOWED_STATUS:
		raise ValueError("невалиден статус")
	return st

def _validate_birth_date(birth_date: str | None) -> str | None:
	if birth_date is None:
		return None
	bd = _clean(birth_date)
	if not bd or not DATE_RE.match(bd):
		raise ValueError("датата трябва да е във формат YYYY-MM-DD")
	return bd

from db import fetch_one

def find_player_by_name(name):
    return fetch_one("SELECT * FROM players WHERE full_name=?", (name,))

def _validate_number(number: int | str | None) -> int | None:
	if number is None:
		return None
	try:
		n = int(number)
	except Exception as e:
		raise ValueError("номерът трябва да е число") from e
	if not (1 <= n <= 99):
		raise ValueError("номерът трябва да е между 1 и 99")
	return n

def _club_id_by_name(club_name: str) -> int:
	name = _clean(club_name) or ""
	if not name:
		raise ValueError("липсва име на клуб")
	club = fetch_one("SELECT id, name FROM clubs WHERE name = ?", (name,))
	if not club:
		raise ValueError("няма такъв клуб")
	return int(club["id"])

# --- CRUD ---

def add_player(
	full_name: str,
	club_name: str,
	position: str,
	shirt_number: int | str,
	birth_date: str | None = None,
	nationality: str | None = None,
	status: str | None = None,
) -> int:
	name = _clean(full_name) or ""
	if len(name) < 3:
		raise ValueError("невалидно име на играч")

	club_id = _club_id_by_name(club_name)
	pos = _validate_position(position)
	num = _validate_number(shirt_number)
	bd = _validate_birth_date(birth_date)
	nat = _clean(nationality)
	st = _validate_status(status)

	try:
		last_id, _ = execute(
			"""
			INSERT INTO players (full_name, birth_date, nationality, position, shirt_number, club_id, status)
			VALUES (?, ?, ?, ?, ?, ?, ?)
			""",
			(name, bd, nat, pos, num, club_id, st),
		)
		return int(last_id)
	except sqlite3.IntegrityError as e:
		raise ValueError("грешка при запис (провери UNIQUE/FK ограничения)") from e

def list_players() -> list[dict]:
	return fetch_all(
		"""
		SELECT p.id, p.full_name, p.position, p.shirt_number, p.status,
		p.birth_date, p.nationality,
		c.name AS club_name
		FROM players p
		LEFT JOIN clubs c ON c.id = p.club_id
		ORDER BY c.name, p.position, p.shirt_number, p.full_name
		"""
	)

def list_players_by_club(club_name: str) -> list[dict]:
	club_id = _club_id_by_name(club_name)
	return fetch_all(
		"""
		SELECT p.id, p.full_name, p.position, p.shirt_number, p.status,
		p.birth_date, p.nationality
		FROM players p
		WHERE p.club_id = ?
		ORDER BY p.position, p.shirt_number, p.full_name
		""",
		(club_id,),
	)

def find_player_by_name(full_name: str) -> dict | None:
	name = _clean(full_name) or ""
	if not name:
		return None
	return fetch_one(
		"""
		SELECT p.id, p.full_name, p.position, p.shirt_number, p.status,
		c.name AS club_name
		FROM players p
		LEFT JOIN clubs c ON c.id = p.club_id
		WHERE p.full_name = ?
		""",
		(name,),
	)

def update_player_number(player_id: int, new_number: int | str) -> int:
	if not isinstance(player_id, int) or player_id <= 0:
		raise ValueError("невалиден player_id")
	num = _validate_number(new_number)
	_, affected = execute(
		"UPDATE players SET shirt_number = ? WHERE id = ?",
		(num, player_id),
	)
	return int(affected)

def update_player_position(player_id: int, new_position: str) -> int:
	if not isinstance(player_id, int) or player_id <= 0:
		raise ValueError("невалиден player_id")
	pos = _validate_position(new_position)
	_, affected = execute(
		"UPDATE players SET position = ? WHERE id = ?",
		(pos, player_id),
	)
	return int(affected)

def update_player_status(player_id: int, new_status: str) -> int:
	if not isinstance(player_id, int) or player_id <= 0:
		raise ValueError("невалиден player_id")
	st = _validate_status(new_status)
	_, affected = execute(
		"UPDATE players SET status = ? WHERE id = ?",
		(st, player_id),
	)
	return int(affected)

def delete_player(player_id: int) -> int:
	if not isinstance(player_id, int) or player_id <= 0:
		raise ValueError("невалиден player_id")
	try:
		_, affected = execute("DELETE FROM players WHERE id = ?", (player_id,))
		return int(affected)
	except sqlite3.IntegrityError as e:
		raise ValueError("не може да се изтрие (има свързани записи)") from e