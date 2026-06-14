import json
import random
from pathlib import Path

DATA_PATH = Path("data/squads.json")


def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_all_seasons():
    data = load_data()
    return data


def get_season(season_name: str):
    data = load_data()
    for season in data:
        if season["season"] == season_name:
            return season
    return None


def get_random_season():
    data = load_data()
    return random.choice(data)