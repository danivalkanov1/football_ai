from ai.features import FeaturesService


class AIService:

    @staticmethod
    def predict(home_club, away_club):

        home = FeaturesService.club_exists(home_club)
        if not home:
            raise ValueError("Няма такъв домакин.")

        away = FeaturesService.club_exists(away_club)
        if not away:
            raise ValueError("Няма такъв гост.")

        if not FeaturesService.same_league(home["id"], away["id"]):
            raise ValueError("Отборите не са в една лига.")

        home_stats = FeaturesService.calculate_form(home["id"])
        away_stats = FeaturesService.calculate_form(away["id"])

        # home advantage
        home_power = (
            home_stats["form"] * 40 +
            home_stats["gf_avg"] * 25 -
            home_stats["ga_avg"] * 10 +
            10
        )

        away_power = (
            away_stats["form"] * 40 +
            away_stats["gf_avg"] * 25 -
            away_stats["ga_avg"] * 10
        )

        draw_power = 20

        total = home_power + away_power + draw_power

        home_pct = round((home_power / total) * 100)
        draw_pct = round((draw_power / total) * 100)
        away_pct = 100 - home_pct - draw_pct

        if home_pct < 0:
            home_pct = 0

        if away_pct < 0:
            away_pct = 0

        return (
            f"Прогноза:\n"
            f"Победа {home_club}: {home_pct}%\n"
            f"Равен: {draw_pct}%\n"
            f"Победа {away_club}: {away_pct}%"
        )