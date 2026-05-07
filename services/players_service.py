from repositories.players_repo import (
	add_player,
	list_players_by_club,
	find_player_by_name,
	update_player_number,
	delete_player,
)

def _fmt_player(p: dict) -> str:
	num = p.get("shirt_number")
	num_txt = f"#{num}" if num is not None else "#-"
	return f"{p['id']}. {p['full_name']} {p['position']} {num_txt} [{p['status']}]"

class PlayersService:
	def add(self, full_name: str, club: str, position: str, number: str, birth_date=None, nationality=None) -> str:
		try:
			pid = add_player(
				full_name=full_name,
				club_name=club,
				position=position,
				shirt_number=number,
				birth_date=birth_date,
				nationality=nationality,
				status="ACTIVE",
			)
			return f"OK: добавен играч id={pid}"
		except ValueError as e:
			return f"Грешка: {e}"

	def list_by_club(self, club: str) -> str:
		try:
			items = list_players_by_club(club)
			if not items:
				return "Няма играчи за този клуб."
			return "\n".join(_fmt_player(p) for p in items)
		except ValueError as e:
			return f"Грешка: {e}"

	def change_number(self, player_name: str, new_number: str) -> str:
		p = find_player_by_name(player_name)
		if not p:
			return "Грешка: няма такъв играч (по точно име)."
		try:
			affected = update_player_number(int(p["id"]), new_number)
			return f"OK: сменен номер (affected={affected})"
		except ValueError as e:
			return f"Грешка: {e}"

	def delete(self, player_name: str) -> str:
		p = find_player_by_name(player_name)
		if not p:
			return "Грешка: няма такъв играч (по точно име)."
		try:
			affected = delete_player(int(p["id"]))
			return f"OK: изтрит играч (affected={affected})"
		except ValueError as e:
			return f"Грешка: {e}"