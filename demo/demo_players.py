from repositories.players_repo import (
	add_player,
	list_players_by_club,
	find_player_by_name,
	update_player_number,
	delete_player
)

def main():
	print("PLAYERS of Левски София (before)")
	for p in list_players_by_club("Левски София"):
		print(p["id"], p["full_name"], p["position"], p["shirt_number"])

	pid = add_player("Петър Георгиев", "Левски София", "DF", 5, "2005-01-15", "BG", "ACTIVE")
	print("\nADD id=", pid)

	p = find_player_by_name("Петър Георгиев")
	if p:
		print("\nUPDATE number affected:", update_player_number(int(p["id"]), 15))

	p = find_player_by_name("Петър Георгиев")
	if p:
		print("\nDELETE affected:", delete_player(int(p["id"])))

	print("\nPLAYERS of Левски София (final)")
	for p in list_players_by_club("Левски София"):
		print(p["id"], p["full_name"], p["position"], p["shirt_number"])

if __name__ == "__main__":
	main()