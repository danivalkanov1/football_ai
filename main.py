import re
from logger import get_logger

from repositories.clubs_repo import (
	add_club,
	list_clubs,
	find_club_by_name,
	update_club,
	delete_club,
)

from players_service import PlayersService

logger = get_logger()
players = PlayersService()

# --------- CLUBS regex ----------
C_ADD = re.compile(r"^Добави\s+клуб\s+(.+?)(?:\s+град\s+(.+))?$", re.IGNORECASE)
C_LIST = re.compile(r"^Покажи\s+всички\s+клубове$", re.IGNORECASE)
C_REN = re.compile(r"^Преименувай\s+клуб\s+(.+?)\s+на\s+(.+)$", re.IGNORECASE)
C_DEL = re.compile(r"^Изтрий\s+клуб\s+(.+)$", re.IGNORECASE)

# --------- PLAYERS regex ----------
# Добави играч <име> в <клуб> позиция <GK|DF|MF|FW> номер <N> [роден YYYY-MM-DD] [националност XX]
P_ADD = re.compile(
	r"^Добави\s+играч\s+(.+?)\s+в\s+(.+?)\s+позиция\s+(GK|DF|MF|FW)\s+номер\s+(\d{1,2})"
	r"(?:\s+роден\s+(\d{4}-\d{2}-\d{2}))?"
	r"(?:\s+националност\s+(.+))?$",
	re.IGNORECASE
)
P_LIST = re.compile(r"^Покажи\s+играчи\s+на\s+(.+)$", re.IGNORECASE)
P_NUM = re.compile(r"^Смени\s+номер\s+на\s+(.+?)\s+на\s+(\d{1,2})$", re.IGNORECASE)
P_DEL = re.compile(r"^Изтрий\s+играч\s+(.+)$", re.IGNORECASE)

HELP = re.compile(r"^(помощ|help|покажи\s+команди)$", re.IGNORECASE)
EXIT = re.compile(r"^(изход|exit|quit)$", re.IGNORECASE)


def help_text() -> str:
	return "\n".join([
		"Команди:",
		"",
		"Клубове:",
		" Добави клуб <име> [град <град>]",
		" Покажи всички клубове",
		" Преименувай клуб <старо> на <ново>",
		" Изтрий клуб <име>",
		"",
		"Играчѝ:",
		" Добави играч <име> в <клуб> позиция <GK|DF|MF|FW> номер <N> [роден YYYY-MM-DD] [националност XX]",
		" Покажи играчи на <клуб>",
		" Смени номер на <име> на <N>",
		" Изтрий играч <име>",
		"",
		"Други:",
		" помощ",
		" изход",
	])


def format_clubs() -> str:
	clubs = list_clubs()
	if not clubs:
		return "Няма клубове."
	return "\n".join(
		f"{c['id']}. {c['name']}" + (f" ({c['city']})" if c.get("city") else "")
		for c in clubs
	)


def main():
	print(help_text())

	while True:
		cmd = input("> ").strip()
		if not cmd:
			continue

		logger.info(cmd)

		if EXIT.match(cmd):
			break

		if HELP.match(cmd):
			print(help_text())
			continue

		# --------- CLUBS handlers ----------
		m = C_ADD.match(cmd)
		if m:
			try:
				new_id = add_club(m.group(1), m.group(2))
				print(f"OK: добавен клуб id={new_id}")
			except ValueError as e:
				print(f"Грешка: {e}")
			continue

		if C_LIST.match(cmd):
			print(format_clubs())
			continue

		m = C_REN.match(cmd)
		if m:
			old_name, new_name = m.group(1).strip(), m.group(2).strip()
			club = find_club_by_name(old_name)
			if not club:
				print("Грешка: няма такъв клуб.")
				continue
			try:
				affected = update_club(int(club["id"]), new_name, club.get("city"))
				if affected == 0:
					print("Грешка: нищо не е променено.")
				else:
					print("OK: преименувано.")
			except ValueError as e:
				print(f"Грешка: {e}")
			continue

		m = C_DEL.match(cmd)
		if m:
			name = m.group(1).strip()
			club = find_club_by_name(name)
			if not club:
				print("Грешка: няма такъв клуб.")
				continue
			try:
				affected = delete_club(int(club["id"]))
				print(f"OK: изтрито (affected={affected})")
			except ValueError as e:
				print(f"Грешка: {e}")
			continue

		# --------- PLAYERS handlers ----------
		m = P_ADD.match(cmd)
		if m:
			# groups: name, club, position, number, birth_date?, nationality?
			print(players.add(
				full_name=m.group(1),
				club=m.group(2),
				position=m.group(3),
				number=m.group(4),
				birth_date=m.group(5),
				nationality=m.group(6),
			))
			continue

		m = P_LIST.match(cmd)
		if m:
			print(players.list_by_club(m.group(1)))
			continue

		m = P_NUM.match(cmd)
		if m:
			print(players.change_number(m.group(1), m.group(2)))
			continue

		m = P_DEL.match(cmd)
		if m:
			print(players.delete(m.group(1)))
			continue

		print("Неразпозната команда. Напиши 'помощ'.")


if __name__ == "__main__":
	main()