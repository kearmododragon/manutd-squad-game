from app.services.draft_services import DraftService
from app.state import GameState
from app.data_loader import get_all_seasons, get_random_season

def main():
    draft = DraftService()
    state = GameState()

    print("\n🎮 MAN UTD DRAFT GAME STARTED\n")

    while len(state.selected_players) < 3:

        squad = draft.get_random_squad()

        print(f"\n🔥 {squad['season']}")
        print("Pick ONE player:\n")

        available = [p for p in squad["players"] if not state.is_used(p)]

        for i, p in enumerate(available):
            print(f"{i}: {p['name']} ({', '.join(p['positions'])}) | {p['rating']}")

        choice = int(input("\nSelect player number: "))

        if choice < 0 or choice >= len(available):
            print("Invalid selection")
            continue

        selected = available[choice]

        state.add_player(selected, None)

        print(f"\n✅ Added: {selected['name']}")

    print("\n🏁 FINAL TEAM:")
    for p in state.selected_players:
        print("-", p["player"]["name"])

if __name__ == "__main__":
    main()