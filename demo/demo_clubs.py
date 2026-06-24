from repositories.clubs_repo import (
    list_clubs, add_club, find_club_by_name, update_club, delete_club
)

def print_clubs(title: str):
    print("\n" + title)
    for c in list_clubs():
        print(f"{c['id']}. {c['name']}" + (f" ({c['city']})" if c["city"] else ""))

def ensure_deleted(name: str):
    club = find_club_by_name(name)
    if club:
        delete_club(club["id"])

def ensure_added(name: str, city: str):
    club = find_club_by_name(name)
    if club:
        return club["id"]
    return add_club(name, city)

def main():
    # гарантира чист старт за demo записите
    ensure_deleted("Арда")
    ensure_deleted("Славия")
    ensure_deleted("Славия София")
    ensure_deleted("Черно море")

    print_clubs("LIST (before)")

    ensure_added("Славия", "София")
    ensure_added("Арда", "Кърджали")
    ensure_added("Черно море", "Варна")

    print_clubs("LIST (after add)")

    slavia = find_club_by_name("Славия")
    if slavia:
        affected = update_club(slavia["id"], "Славия София", "София")
        print("\nUPDATE affected:", affected)

    arda = find_club_by_name("Арда")
    if arda:
        affected = delete_club(arda["id"])
        print("\nDELETE affected:", affected)

    print_clubs("LIST (final)")

if __name__ == "__main__":
    main()
