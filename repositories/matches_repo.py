from db import execute, fetch_one, fetch_all


def get_match_by_id(match_id):
    return fetch_one("SELECT * FROM matches WHERE id=?", (match_id,))


def get_match_with_clubs(match_id):
    return fetch_one(
        """SELECT m.*, h.name AS home_name, a.name AS away_name
           FROM matches m
           JOIN clubs h ON h.id = m.home_club_id
           JOIN clubs a ON a.id = m.away_club_id
           WHERE m.id = ?""",
        (match_id,),
    )


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


def finish_match(match_id):
    return execute(
        "UPDATE matches SET status='FINISHED' WHERE id=? AND status='SCHEDULED'",
        (match_id,),
    )


def inc_goal(match_id, home_goals, away_goals):
    return execute(
        "UPDATE matches SET home_goals=?, away_goals=? WHERE id=?",
        (home_goals, away_goals, match_id),
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


def get_matches_by_league(league_id):
    return fetch_all(
        """SELECT m.id, m.round_no, m.match_date,
                  h.name AS home_club, a.name AS away_club,
                  m.home_goals, m.away_goals, m.status
           FROM matches m
           JOIN clubs h ON h.id = m.home_club_id
           JOIN clubs a ON a.id = m.away_club_id
           WHERE m.league_id = ?
           ORDER BY m.round_no, m.id""",
        (league_id,),
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