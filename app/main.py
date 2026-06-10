from app.services.draft_services import DraftService
from app.state import DraftState

def main():
    draft = DraftService()
    state = DraftState()

    print("\n🎮 MAN UTD DRAFT GAME STARTED\n")

    while len(state.team) < 3:  # start small (we’ll scale to 11 later)
        squad = draft.get_random_squad()

        print(f"\n🔥 {squad['season']}")
        print("Pick ONE player:\n")

        available = []

        for i, p in enumerate(squad["players"]):
            if not state.is_used(p):
                available.append(p)
                print(f"{i}: {p['name']} ({', '.join(p['positions'])}) | {p['rating']}")

        choice = int(input("\nSelect player number: "))
        selected = available[choice]

        state.add_player(selected)

        print(f"\n✅ Added: {selected['name']}")

    print("\n🏁 FINAL TEAM:")
    for p in state.team:
        print("-", p["name"])

if __name__ == "__main__":
    main()