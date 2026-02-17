import re
from db import Database
from logger import get_logger
from repositories.clubs_repo import ClubsRepository
from clubs_service import ClubsService

logger = get_logger()

ADD = re.compile(r"^Добави\s+клуб\s+(.+?)(?:\s+град\s+(.+))?$", re.IGNORECASE)
LIST = re.compile(r"^Покажи\s+всички\s+клубове$", re.IGNORECASE)
REN = re.compile(r"^Преименувай\s+клуб\s+(.+?)\s+на\s+(.+)$", re.IGNORECASE)
DEL = re.compile(r"^Изтрий\s+клуб\s+(.+)$", re.IGNORECASE)
HELP = re.compile(r"^(помощ|help|покажи\s+команди)$", re.IGNORECASE)
EXIT = re.compile(r"^(изход|exit|quit)$", re.IGNORECASE)

def help_text() -> str:
    return "\n".join([
        "Команди (clubs):",
        "  Добави клуб <име> [град <град>]",
        "  Покажи всички клубове",
        "  Преименувай клуб <старо> на <ново>",
        "  Изтрий клуб <име>",
        "  помощ",
        "  изход",
    ])

def main():
    db = Database("football.db")
    svc = ClubsService(ClubsRepository(db))

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

        m = ADD.match(cmd)
        if m:
            print(svc.add(m.group(1), m.group(2)))
            continue

        if LIST.match(cmd):
            print(svc.list_all())
            continue

        m = REN.match(cmd)
        if m:
            print(svc.rename(m.group(1), m.group(2)))
            continue

        m = DEL.match(cmd)
        if m:
            print(svc.delete(m.group(1)))
            continue

        print("Неразпозната команда. Напиши 'помощ'.")

if __name__ == "__main__":
    main()
