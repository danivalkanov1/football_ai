from repositories.matches_repo import *
from repositories.clubs_repo import find_club_by_name
from repositories.players_repo import find_player_by_name


class MatchesService:
    def __init__(self):
        self.current_match_id = None

    def select_match(self, match_id):
        m = get_match_by_id(match_id)
        if not m:
            raise ValueError("няма такъв мач")
        self.current_match_id = match_id
        return f"OK: избран мач {match_id}"

    def add_result(self, home_name, away_name, hg, ag):
        home = find_club_by_name(home_name)
        away = find_club_by_name(away_name)

        if not home or not away:
            raise ValueError("невалидни отбори")

        match = find_match_by_teams(home["id"], away["id"])
        if not match:
            raise ValueError("няма такъв мач")

        if match["status"] == "FINISHED":
            raise ValueError("вече има резултат")

        update_result(match["id"], hg, ag)
        return f"OK: {home_name}-{away_name} {hg}:{ag}"

    def add_goal(self, player_name, club_name, minute):
        if not self.current_match_id:
            raise ValueError("няма избран мач")

        if minute < 1 or minute > 120:
            raise ValueError("невалидна минута")

        player = find_player_by_name(player_name)
        club = find_club_by_name(club_name)
        match = get_match_by_id(self.current_match_id)

        if not player or not club:
            raise ValueError("невалидни данни")

        if club["id"] not in (match["home_club_id"], match["away_club_id"]):
            raise ValueError("отборът не участва")

        if player["club_id"] != club["id"]:
            raise ValueError("играчът не е в този отбор")

        insert_goal(self.current_match_id, player["id"], club["id"], minute)
        return "OK: гол записан"

    def add_card(self, player_name, club_name, card_type, minute):
        if not self.current_match_id:
            raise ValueError("няма избран мач")

        if card_type not in ("Y", "R"):
            raise ValueError("невалиден картон")

        if minute < 1 or minute > 120:
            raise ValueError("невалидна минута")

        player = find_player_by_name(player_name)
        club = find_club_by_name(club_name)

        if not player or not club:
            raise ValueError("невалидни данни")

        insert_card(self.current_match_id, player["id"], club["id"], minute, card_type)
        return "OK: картон записан"

    def show_events(self):
        if not self.current_match_id:
            raise ValueError("няма избран мач")

        events = get_events(self.current_match_id)

        if not events:
            return "няма събития"

        return "\n".join(
            f"{e['minute']} мин - {e['type']} (player_id={e['player_id']})"
            for e in events
        )