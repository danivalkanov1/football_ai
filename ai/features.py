from db import fetch_all, fetch_one


class FeaturesService:

    @staticmethod
    def club_exists(name):
        row = fetch_one(
            "SELECT id FROM clubs WHERE LOWER(name)=LOWER(?)",
            (name,)
        )
        return row

    @staticmethod
    def same_league(home_id, away_id):
        row = fetch_one("""
            SELECT lt1.league_id
            FROM league_teams lt1
            JOIN league_teams lt2
                ON lt1.league_id = lt2.league_id
            WHERE lt1.club_id = ?
              AND lt2.club_id = ?
        """, (home_id, away_id))

        return row is not None

    @staticmethod
    def last_matches(club_id, limit=5):

        rows = fetch_all("""
            SELECT *
            FROM matches
            WHERE status='FINISHED'
              AND (home_club_id=? OR away_club_id=?)
            ORDER BY match_date DESC
            LIMIT ?
        """, (club_id, club_id, limit))

        return rows

    @staticmethod
    def calculate_form(club_id):

        matches = FeaturesService.last_matches(club_id)

        if not matches:
            raise ValueError("Няма мачове за този отбор.")

        n = len(matches)
        points = 0
        gf = 0
        ga = 0

        for m in matches:
            home = m["home_club_id"] == club_id
            scored = m["home_goals"] if home else m["away_goals"]
            conceded = m["away_goals"] if home else m["home_goals"]

            gf += scored
            ga += conceded

            if scored > conceded:
                points += 3
            elif scored == conceded:
                points += 1

        max_points = n * 3
        return {
            "form": points / max_points if max_points > 0 else 0,
            "gf_avg": gf / n,
            "ga_avg": ga / n
        }