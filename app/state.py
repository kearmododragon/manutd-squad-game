class GameState:
    def __init__(self):
        self.formation = None

        self.selected_players = []   # final XI
        self.filled_positions = []

        self.used_players = set()    # player names only
        self.used_managers = set()   # manager names only

        self.rerolls = 3

        self.manager = None


    # ----------------------------
    # PLAYER USAGE LOGIC
    # ----------------------------

    def is_player_used(self, player):
        """
        Check if player has already been picked in this draft
        """
        return player["name"] in self.used_players


    def mark_player_used(self, player):
        """
        Mark player as unavailable
        """
        self.used_players.add(player["name"])


    def add_player(self, player, position):
        """
        Add player to final squad
        """
        self.selected_players.append({
            "player": player,
            "position": position
        })

        self.mark_player_used(player)


    # ----------------------------
    # MANAGER LOGIC
    # ----------------------------

    def is_manager_used(self, manager):
        """
        Check if manager has already been picked
        """
        return manager["name"] in self.used_managers


    def add_manager(self, manager):
        """
        Select the manager
        Only one allowed
        """

        if self.manager is not None:
            return False

        self.manager = manager
        self.used_managers.add(manager["name"])

        return True

    def formation_complete(self):
        return (
        len(self.filled_positions)
        ==
        len(self.available_positions)
    )

    # ----------------------------
    # RESET
    # ----------------------------

    def reset(self):
        """
        Reset the draft
        """

        self.formation = None

        self.selected_players = []
        self.filled_positions = []

        self.used_players = set()
        self.used_managers = set()

        self.rerolls = 3

        self.manager = None