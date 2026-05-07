import re
from logger import get_logger

# clubs
from repositories.clubs_repo import (
    add_club,
    list_clubs,
    find_club_by_name,
    update_club,
    delete_club,
)

# services
from services.players_service import PlayersService
from services.transfers_service import TransfersService
from services.matches_service import MatchesService
from services.standings_service import StandingsService

logger = get_logger()

# =========================
# REGEX
# =========================

# clubs
ADD_CLUB = re.compile(r"^Добави\s+клуб\s+(.+?)(?:\s+град\s+(.+))?$", re.IGNORECASE)
LIST_CLUBS = re.compile(r"^(?:Покажи\s+всички\s+)?клубове$", re.IGNORECASE)
REN_CLUB = re.compile(r"^Преименувай\s+клуб\s+(.+?)\s+на\s+(.+)$", re.IGNORECASE)
DEL_CLUB = re.compile(r"^Изтрий\s+клуб\s+(.+)$", re.IGNORECASE)

# players
ADD_PLAYER = re.compile(
    r"^Добави\s+играч\s+(.+?)\s+в\s+(.+?)\s+позиция\s+(GK|DF|MF|FW)\s+номер\s+(\d+)$",
    re.IGNORECASE
)

LIST_PLAYERS = re.compile(
    r"^Покажи\s+играчи\s+на\s+(.+)$",
    re.IGNORECASE
)

UPDATE_NUMBER = re.compile(
    r"^Смени\s+номер\s+на\s+(.+?)\s+на\s+(\d+)$",
    re.IGNORECASE
)

DEL_PLAYER = re.compile(
    r"^Изтрий\s+играч\s+(.+)$",
    re.IGNORECASE
)

# transfers
TRANSFER = re.compile(
    r"^Трансфер\s+(.+?)\s+от\s+(.+?)\s+в\s+(.+?)\s+(\d{4}-\d{2}-\d{2})(?:\s+(\d+))?$",
    re.IGNORECASE
)

SHOW_TRANSFERS_PLAYER = re.compile(
    r"^Покажи\s+трансфери\s+на\s+(.+)$",
    re.IGNORECASE
)

# matches
SELECT_MATCH = re.compile(
    r"^Избери\s+мач\s+(\d+)$",
    re.IGNORECASE
)

RESULT = re.compile(
    r"^Резултат\s+(.+?)-(.+?)\s+(\d+):(\d+)\s+запиши$",
    re.IGNORECASE
)

GOAL = re.compile(
    r"^Гол\s+(.+?)\s+(.+?)\s+(\d+)\s+минута$",
    re.IGNORECASE
)

CARD = re.compile(
    r"^Картон\s+(.+?)\s+(.+?)\s+(Y|R)\s+(\d+)$",
    re.IGNORECASE
)

EVENTS = re.compile(
    r"^Покажи\s+събития$",
    re.IGNORECASE
)

# standings
STANDINGS = re.compile(
    r"^Покажи\s+класиране\s+(.+?)\s+(\d{4}/\d{4})$",
    re.IGNORECASE
)

# system
HELP = re.compile(r"^(помощ|help)$", re.IGNORECASE)
EXIT = re.compile(r"^(изход|exit|quit)$", re.IGNORECASE)


# =========================
# HELP
# =========================

def help_text():
    return "\n".join([
        "=== CLUBS ===",
        "Добави клуб <име> [град <град>]",
        "клубове",
        "Преименувай клуб <старо> на <ново>",
        "Изтрий клуб <име>",
        "",

        "=== PLAYERS ===",
        "Добави играч <име> в <клуб> позиция <GK/DF/MF/FW> номер <№>",
        "Покажи играчи на <клуб>",
        "Смени номер на <играч> на <№>",
        "Изтрий играч <име>",
        "",

        "=== TRANSFERS ===",
        "Трансфер <играч> от <клуб> в <клуб> YYYY-MM-DD [сума]",
        "Покажи трансфери на <играч>",
        "",

        "=== MATCHES ===",
        "Избери мач <id>",
        "Резултат <Домакин>-<Гост> X:Y запиши",
        "Гол <Играч> <Отбор> <минута> минута",
        "Картон <Играч> <Отбор> Y/R <минута>",
        "Покажи събития",
        "",

        "=== STANDINGS ===",
        "Покажи класиране <лига> <сезон>",
        "",

        "помощ / изход"
    ])


def format_clubs():

    clubs = list_clubs()

    if not clubs:
        return "Няма клубове."

    return "\n".join(
        f"{c['id']}. {c['name']}" +
        (f" ({c['city']})" if c["city"] else "")
        for c in clubs
    )


# =========================
# MAIN
# =========================

def main():

    players_service = PlayersService()
    transfers_service = TransfersService()
    matches_service = MatchesService()
    standings_service = StandingsService()

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

        # ================= CLUBS =================

        m = ADD_CLUB.match(cmd)

        if m:
            try:
                cid = add_club(m.group(1), m.group(2))
                print(f"OK: клуб id={cid}")
            except ValueError as e:
                print(e)

            continue

        if LIST_CLUBS.match(cmd):
            print(format_clubs())
            continue

        m = REN_CLUB.match(cmd)

        if m:

            club = find_club_by_name(m.group(1))

            if not club:
                print("няма такъв клуб")
                continue

            update_club(
                club["id"],
                m.group(2),
                club["city"]
            )

            print("OK")
            continue

        m = DEL_CLUB.match(cmd)

        if m:

            club = find_club_by_name(m.group(1))

            if not club:
                print("няма такъв клуб")
                continue

            delete_club(club["id"])

            print("OK")
            continue

        # ================= PLAYERS =================

        m = ADD_PLAYER.match(cmd)

        if m:
            try:
                print(
                    players_service.add(
                        m.group(1),
                        m.group(2),
                        m.group(3),
                        int(m.group(4))
                    )
                )
            except ValueError as e:
                print(e)

            continue

        m = LIST_PLAYERS.match(cmd)

        if m:
            print(players_service.list_by_club(m.group(1)))
            continue

        m = UPDATE_NUMBER.match(cmd)

        if m:
            try:
                print(
                    players_service.update_number(
                        m.group(1),
                        int(m.group(2))
                    )
                )
            except ValueError as e:
                print(e)

            continue

        m = DEL_PLAYER.match(cmd)

        if m:
            try:
                print(players_service.delete(m.group(1)))
            except ValueError as e:
                print(e)

            continue

        # ================= TRANSFERS =================

        m = TRANSFER.match(cmd)

        if m:
            try:
                print(
                    transfers_service.transfer_player(
                        m.group(1),
                        m.group(2),
                        m.group(3),
                        m.group(4),
                        m.group(5)
                    )
                )
            except ValueError as e:
                print(e)

            continue

        m = SHOW_TRANSFERS_PLAYER.match(cmd)

        if m:
            print(
                transfers_service.list_transfers_by_player(
                    m.group(1)
                )
            )

            continue

        # ================= MATCHES =================

        m = SELECT_MATCH.match(cmd)

        if m:
            try:
                print(
                    matches_service.select_match(
                        int(m.group(1))
                    )
                )
            except ValueError as e:
                print(e)

            continue

        m = RESULT.match(cmd)

        if m:
            try:
                print(
                    matches_service.add_result(
                        m.group(1),
                        m.group(2),
                        int(m.group(3)),
                        int(m.group(4))
                    )
                )
            except ValueError as e:
                print(e)

            continue

        m = GOAL.match(cmd)

        if m:
            try:
                print(
                    matches_service.add_goal(
                        m.group(1),
                        m.group(2),
                        int(m.group(3))
                    )
                )
            except ValueError as e:
                print(e)

            continue

        m = CARD.match(cmd)

        if m:
            try:
                print(
                    matches_service.add_card(
                        m.group(1),
                        m.group(2),
                        m.group(3),
                        int(m.group(4))
                    )
                )
            except ValueError as e:
                print(e)

            continue

        if EVENTS.match(cmd):
            try:
                print(matches_service.show_events())
            except ValueError as e:
                print(e)

            continue

        # ================= STANDINGS =================

        m = STANDINGS.match(cmd)

        if m:
            try:
                print(
                    standings_service.show_table(
                        m.group(1),
                        m.group(2)
                    )
                )
            except ValueError as e:
                print(e)

            continue

        # ================= UNKNOWN =================

        print("Неразпозната команда.")


if __name__ == "__main__":
    main()