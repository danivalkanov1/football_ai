from db import fetch_all, fetch_one


def get_league(name, season):
    return fetch_one(
        """
        SELECT id, name, season
        FROM leagues
        WHERE name = ? AND season = ?
        """,
        (name, season)
    )


def get_league_teams(league_id):
    return fetch_all(
        """
        SELECT c.id, c.name
        FROM league_teams lt
        JOIN clubs c ON c.id = lt.club_id
        WHERE lt.league_id = ?
        ORDER BY c.name
        """,
        (league_id,)
    )


def get_played_matches(league_id):
    return fetch_all(
        """
        SELECT
            id,
            home_club_id,
            away_club_id,
            home_goals,
            away_goals
        FROM matches
        WHERE league_id = ?
          AND status = 'FINISHED'
          AND home_goals IS NOT NULL
          AND away_goals IS NOT NULL
        """,
        (league_id,)
    )