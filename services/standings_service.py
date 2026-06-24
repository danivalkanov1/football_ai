from repositories.standings_repo import (
    get_league,
    get_league_teams,
    get_played_matches,
)


class StandingsService:

    def show_table(self, league_name, season):

        league = get_league(league_name, season)

        if not league:
            raise ValueError("няма такава лига")

        teams = get_league_teams(league["id"])

        if not teams:
            raise ValueError("няма отбори в лигата")

        table = {}

        for t in teams:
            table[t["id"]] = {
                "team": t["name"],
                "MP": 0,
                "W": 0,
                "D": 0,
                "L": 0,
                "GF": 0,
                "GA": 0,
                "GD": 0,
                "PTS": 0,
            }

        matches = get_played_matches(league["id"])

        for m in matches:

            home = table[m["home_club_id"]]
            away = table[m["away_club_id"]]

            hg = m["home_goals"]
            ag = m["away_goals"]

            home["MP"] += 1
            away["MP"] += 1

            home["GF"] += hg
            home["GA"] += ag

            away["GF"] += ag
            away["GA"] += hg

            if hg > ag:
                home["W"] += 1
                away["L"] += 1
                home["PTS"] += 3

            elif hg < ag:
                away["W"] += 1
                home["L"] += 1
                away["PTS"] += 3

            else:
                home["D"] += 1
                away["D"] += 1

                home["PTS"] += 1
                away["PTS"] += 1

        for t in table.values():
            t["GD"] = t["GF"] - t["GA"]

        standings = sorted(
            table.values(),
            key=lambda x: (
                -x["PTS"],
                -x["GD"],
                -x["GF"],
                x["team"]
            )
        )

        lines = []

        pos = 1

        for t in standings:

            gd = f"+{t['GD']}" if t["GD"] >= 0 else str(t["GD"])

            lines.append(
                f"{pos}. "
                f"{t['team']} | "
                f"MP:{t['MP']} "
                f"W:{t['W']} "
                f"D:{t['D']} "
                f"L:{t['L']} "
                f"{t['GF']}:{t['GA']} "
                f"GD:{gd} "
                f"PTS:{t['PTS']}"
            )

            pos += 1

        return "\n".join(lines)