from db import get_connection
from repositories.clubs_repo import find_club_by_name
from repositories.players_repo import find_player_by_name


class TransfersService:

    def transfer_player(
        self,
        player_name,
        from_club_name,
        to_club_name,
        transfer_date,
        fee=None
    ):

        player = find_player_by_name(player_name)

        if not player:
            raise ValueError("няма такъв играч")

        from_club = find_club_by_name(from_club_name)

        if not from_club:
            raise ValueError("няма такъв клуб (from)")

        to_club = find_club_by_name(to_club_name)

        if not to_club:
            raise ValueError("няма такъв клуб (to)")

        if from_club["id"] == to_club["id"]:
            raise ValueError("from и to не могат да са еднакви")

        if player["club_id"] != from_club["id"]:
            raise ValueError(
                f"{player_name} не е в {from_club_name}"
            )

        conn = get_connection()

        try:

            conn.execute(
                """
                INSERT INTO transfers (
                    player_id,
                    from_club_id,
                    to_club_id,
                    transfer_date,
                    fee
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    player["id"],
                    from_club["id"],
                    to_club["id"],
                    transfer_date,
                    fee
                )
            )

            conn.execute(
                """
                UPDATE players
                SET club_id = ?
                WHERE id = ?
                """,
                (
                    to_club["id"],
                    player["id"]
                )
            )

            conn.commit()

            return (
                f"OK: {player_name} "
                f"от {from_club_name} "
                f"в {to_club_name}"
            )

        except Exception as e:

            conn.rollback()
            raise ValueError(str(e))

        finally:
            conn.close()

    def list_transfers_by_player(self, player_name):

        player = find_player_by_name(player_name)

        if not player:
            raise ValueError("няма такъв играч")

        conn = get_connection()

        rows = conn.execute(
            """
            SELECT
                t.id,
                c1.name AS from_club,
                c2.name AS to_club,
                t.transfer_date,
                t.fee
            FROM transfers t
            LEFT JOIN clubs c1
                ON t.from_club_id = c1.id
            JOIN clubs c2
                ON t.to_club_id = c2.id
            WHERE t.player_id = ?
            ORDER BY t.transfer_date DESC
            """,
            (player["id"],)
        ).fetchall()

        conn.close()

        if not rows:
            return "няма трансфери"

        lines = []

        for r in rows:

            fee_text = ""

            if r["fee"] is not None:
                fee_text = f" | {r['fee']}"

            lines.append(
                f"{r['transfer_date']} | "
                f"{r['from_club']} -> "
                f"{r['to_club']}"
                f"{fee_text}"
            )

        return "\n".join(lines)