import re
import sqlite3
from repositories.clubs_repo import ClubsRepository

class ClubsService:
    def __init__(self, repo: ClubsRepository):
        self.repo = repo

    @staticmethod
    def _clean(s: str | None) -> str | None:
        if s is None:
            return None
        s = re.sub(r"\s+", " ", s.strip())
        return s

    def add(self, name: str, city: str | None = None) -> str:
        name = self._clean(name) or ""
        city = self._clean(city)

        if len(name) < 2:
            return "Грешка: невалидно име на клуб."

        try:
            new_id = self.repo.create(name, city)
            return f"OK: добавен клуб id={new_id}"
        except sqlite3.IntegrityError:
            return "Грешка: клуб с това име вече съществува."

    def list_all(self) -> str:
        clubs = self.repo.list_all()
        if not clubs:
            return "Няма клубове."
        return "\n".join(
            f"{c['id']}. {c['name']}" + (f" ({c['city']})" if c["city"] else "")
            for c in clubs
        )

    def rename(self, old_name: str, new_name: str) -> str:
        old_name = self._clean(old_name) or ""
        new_name = self._clean(new_name) or ""

        club = self.repo.get_by_name(old_name)
        if not club:
            return "Грешка: няма такъв клуб."

        if len(new_name) < 2:
            return "Грешка: невалидно ново име."

        try:
            self.repo.update(club["id"], new_name, club["city"])
            return "OK: преименувано."
        except sqlite3.IntegrityError:
            return "Грешка: новото име вече съществува."

    def delete(self, name: str) -> str:
        name = self._clean(name) or ""
        club = self.repo.get_by_name(name)
        if not club:
            return "Грешка: няма такъв клуб."

        try:
            self.repo.delete(club["id"])
            return "OK: изтрито."
        except sqlite3.IntegrityError:
            return "Грешка: клубът се използва в други таблици (FK)."
