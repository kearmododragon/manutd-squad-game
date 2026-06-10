import json
import random

class DraftService:
    def __init__(self, path="data/squads.json"):
        with open(path, "r") as f:
            self.squads = json.load(f)

    def get_random_squad(self):
        return random.choice(self.squads)