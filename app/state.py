class GameState:
    def __init__(self):
        self.formation = None
        self.selected_players = []   # final XI
        self.used_players = set()    # IMPORTANT: store names only
        self.rerolls = 3
        self.manager = None

    # ----------------------------
    # PLAYER USAGE LOGIC
    # ----------------------------

    def is_used(self, player):
        """
        Check if player has already been picked in this draft
        """
        return player["name"] in self.used_players

    def mark_used(self, player):
        """
        Mark a player as used so they cannot be selected again
        """
        self.used_players.add(player["name"])
    def add_player(self, player, position):
        """
        Lock a player into the user's team
        """
        self.selected_players.append({
            "player": player,
            "position": position
        })
        self.mark_used(player)

    def reset(self):
        """
        Reset the draft (new game)
        """
        self.formation = None
        self.selected_players = []
        self.used_players = set()
        self.rerolls = 3
        self.manager = None