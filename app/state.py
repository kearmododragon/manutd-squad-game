class DraftState:
    def __init__(self):
        self.team = []
        self.used_players = set()

    def is_used(self, player_name: str) -> bool:
        return player_name in self.used_players

    def add_player(self, player: dict):
        self.team.append(player)
        self.used_players.add(player["name"])