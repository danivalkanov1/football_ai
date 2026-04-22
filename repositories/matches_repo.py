from db import execute, fetch_one, fetch_all


def get_match_by_id(match_id):
    return fetch_one("SELECT * FROM matches WHERE id=?", (match_id,))


def find_match_by_teams(home_id, away_id):
    return fetch_one(
        """SELECT * FROM matches 
           WHERE home_club_id=? AND away_club_id=?""",
        (home_id, away_id)
    )


def update_result(match_id, hg, ag):
    return execute(
        """UPDATE matches 
           SET home_goals=?, away_goals=?, status='FINISHED' 
           WHERE id=?""",
        (hg, ag, match_id)
    )


def insert_goal(match_id, player_id, club_id, minute):
    return execute(
        "INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (?, ?, ?, ?)",
        (match_id, player_id, club_id, minute)
    )


def insert_card(match_id, player_id, club_id, minute, card_type):
    return execute(
        "INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (?, ?, ?, ?, ?)",
        (match_id, player_id, club_id, minute, card_type)
    )


def get_events(match_id):
    goals = fetch_all(
        "SELECT minute, 'GOAL' as type, player_id FROM goals WHERE match_id=?",
        (match_id,)
    )
    cards = fetch_all(
        "SELECT minute, card_type as type, player_id FROM cards WHERE match_id=?",
        (match_id,)
    )
    return sorted(goals + cards, key=lambda x: x["minute"])