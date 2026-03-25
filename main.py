import re
from logger import get_logger

# --------- CLUBS ----------
from repositories.clubs_repo import (
    add_club,
    list_clubs,
    find_club_by_name,
    update_club,
    delete_club,
)

# --------- PLAYERS ----------
from players_service import PlayersService

# --------- TRANSFERS ----------
from transfers_service import (
    transfer_player,
    list_transfers_by_player,
)

logger = get_logger()
players = PlayersService()

# =======================
# REGEX
# =======================

# --- CLUBS ---
ADD = re.compile(r"^Добави\s+клуб\s+(.+?)(?:\s+град\s+(.+))?$", re.IGNORECASE)
LIST = re.compile(r"^Покажи\s+всички\s+клубове$", re.IGNORECASE)
REN = re.compile(r"^Преименувай\s+клуб\s+(.+?)\s+на\s+(.+)$", re.IGNORECASE)
DEL = re.compile(r"^Изтрий\s+клуб\s+(.+)$", re.IGNORECASE)

# --- PLAYERS ---
P_ADD = re.compile(
    r"^Добави\s+играч\s+(.+?)\s+в\s+(.+?)\s+позиция\s+(GK|DF|MF|FW)\s+номер\s+(\d{1,2})"
    r"(?:\s+роден\s+(\d{4}-\d{2}-\d{2}))?"
    r"(?:\s+националност\s+(.+))?$",
    re.IGNORECASE
)

P_LIST = re.compile(r"^Покажи\s+играчи\s+на\s+(.+)$", re.IGNORECASE)
P_NUM = re.compile(r"^Смени\s+номер\s+на\s+(.+?)\s+на\s+(\d{1,2})$", re.IGNORECASE)
P_DEL = re.compile(r"^Изтрий\s+играч\s+(.+)$", re.IGNORECASE)

# --- TRANSFERS ---
T_TRANSFER = re.compile(
    r"^Трансфер\s+(.+?)\s+от\s+(.+?)\s+в\s+(.+?)\s+(\d{4}-\d{2}-\d{2})(?:\s+сума\s+(\d+))?$",
    re.IGNORECASE
)

T_SHOW_PLAYER = re.compile(
    r"^Покажи\s+трансфери\s+на\s+(.+)$",
    re.IGNORECASE
)

# --- SYSTEM ---
HELP = re.compile(r"^(помощ|help|покажи\s+команди)$", re.IGNORECASE)
EXIT = re.compile(r"^(изход|exit|quit)$", re.IGNORECASE)


# =======================
# HELP
# =======================

def help_text() -> str:
    return "\n".join([
        "Команди:",
        "",
        "Клубове:",
        "  Добави клуб <име> [град <град>]",
        "  Покажи всички клубове",
        "  Преименувай клуб <старо> на <ново>",
        "  Изтрий клуб <име>",
        "",
        "Играчѝ:",
        "  Добави играч <име> в <клуб> позиция <GK|DF|MF|FW> номер <N>",
        "  Покажи играчи на <клуб>",
        "  Смени номер на <име> на <N>",
        "  Изтрий играч <име>",
        "",
        "Трансфери:",
        "  Трансфер <играч> от <клуб> в <клуб> YYYY-MM-DD [сума N]",
        "  Покажи трансфери на <играч>",
        "",
        "Други:",
        "  помощ",
        "  изход",
    ])


# =======================
# FORMATTERS
# =======================

def format_clubs() -> str:
    clubs = list_clubs()
    if not clubs:
        return "Няма клубове."
    return "\n".join(
        f"{c['id']}. {c['name']}" + (f" ({c['city']})" if c.get("city") else "")
        for c in clubs
    )


# =======================
# MAIN
# =======================

def main():
    print(help_text())

    while True:
        cmd = input("> ").strip()
        if not cmd:
            continue

        logger.info(cmd)

        # EXIT
        if EXIT.match(cmd):
            break

        # HELP
        if HELP.match(cmd):
            print(help_text())
            continue

        # =======================
        # CLUBS
        # =======================

        m = ADD.match(cmd)
        if m:
            try:
                new_id = add_club(m.group(1), m.group(2))
                print(f"OK: добавен клуб id={new_id}")
            except ValueError as e:
                print(f"Грешка: {e}")
            continue

        if LIST.match(cmd):
            print(format_clubs())
            continue

        m = REN.match(cmd)
        if m:
            club = find_club_by_name(m.group(1))
            if not club:
                print("Грешка: няма такъв клуб.")
                continue
            try:
                affected = update_club(club["id"], m.group(2), club.get("city"))
                print(f"OK: преименувано ({affected})")
            except ValueError as e:
                print(f"Грешка: {e}")
            continue

        m = DEL.match(cmd)
        if m:
            club = find_club_by_name(m.group(1))
            if not club:
                print("Грешка: няма такъв клуб.")
                continue
            try:
                affected = delete_club(club["id"])
                print(f"OK: изтрито ({affected})")
            except ValueError as e:
                print(f"Грешка: {e}")
            continue

        # =======================
        # PLAYERS
        # =======================

        m = P_ADD.match(cmd)
        if m:
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

        # =======================
        # TRANSFERS
        # =======================

        m = T_TRANSFER.match(cmd)
        if m:
            try:
                print(transfer_player(
                    m.group(1),
                    m.group(2),
                    m.group(3),
                    m.group(4),
                    m.group(5)
                ))
            except Exception as e:
                print(f"Грешка: {e}")
            continue

        m = T_SHOW_PLAYER.match(cmd)
        if m:
            try:
                rows = list_transfers_by_player(m.group(1))
                if not rows:
                    print("Няма трансфери.")
                else:
                    for r in rows:
                        print(f"{r['transfer_date']}: {r['from_club']} → {r['to_club']}")
            except Exception as e:
                print(f"Грешка: {e}")
            continue

        print("Неразпозната команда. Напиши 'помощ'.")


if __name__ == "__main__":
    main()