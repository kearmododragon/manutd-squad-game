from app.services.draft_services import DraftService
from app.state import GameState

POSITION_MAP = {

    # Central midfield
    "CDM": ["CM"],
    "CAM": ["CM"],


    # Strikers
    "CF": ["ST"],


    # Left/right attack
    "LW": [
        "LW",
        "RW",
        "LM",
        "RM"
    ],

    "RW": [
        "RW",
        "LW",
        "RM",
        "LM"
    ],


    # Wide midfielders
    "LM": [
        "LM",
        "LW"
    ],

    "RM": [
        "RM",
        "RW"
    ]
}

def choose_formation(state):

    formations = {
        "1": {
            "name": "4-3-3",
            "positions": [
                "GK",
                "RB",
                "CB1",
                "CB2",
                "LB",
                "CM1",
                "CM2",
                "CM3",
                "RW",
                "ST",
                "LW"
            ]
        },

        "2": {
            "name": "4-4-2",
            "positions": [
                "GK",
                "RB",
                "CB1",
                "CB2",
                "LB",
                "RM",
                "CM1",
                "CM2",
                "LM",
                "ST1",
                "ST2"
            ]
        }
    }


    print("Choose formation:\n")

    for key, formation in formations.items():
        print(
            f"{key}: {formation['name']}"
        )


    choice = input("\nSelect formation: ")

    while choice not in formations:
        print("Invalid choice")
        choice = input("\nSelect formation: ")


    state.formation = formations[choice]["name"]

    state.filled_positions = []

    state.available_positions = formations[choice]["positions"]


    print(
        f"\nFormation selected: {state.formation}"
    )

def choose_position(player, state):

    available_positions = [
        p for p in state.available_positions
        if p not in state.filled_positions
    ]

possible = []

def choose_position(player, state):

    available_positions = [
        p for p in state.available_positions
        if p not in state.filled_positions
    ]


    possible = []


    for slot in available_positions:

        slot_type = (
            slot
            .replace("1", "")
            .replace("2", "")
            .replace("3", "")
        )


        for player_pos in player["positions"]:

            compatible_positions = POSITION_MAP.get(
                player_pos,
                [player_pos]
            )


            if slot_type in compatible_positions:

                if slot not in possible:
                    possible.append(slot)



    if not possible:

        print(
            f"\n❌ No available position for {player['name']}"
        )

        return None



    print(
        f"\nWhere should {player['name']} play?"
    )


    for i, pos in enumerate(possible):

        print(
            f"{i}: {pos}"
        )


    choice = int(
        input("\nSelect position: ")
    )


    if choice < 0 or choice >= len(possible):

        return None


    return possible[choice]
def show_draft_status(state):

    print("\n====================")
    print("YOUR TEAM")

    if state.manager:
        print(
            "👔 Manager:",
            state.manager["name"]
        )
    else:
        print("👔 Manager: None")


    if not state.selected_players:
        print("No players selected")

    else:
        for p in state.selected_players:
            print(
                f"{p['position']}: "
                f"{p['player']['name']}"
            )


    print("\nAVAILABLE POSITIONS:")

    remaining = [
        p for p in state.available_positions
        if p not in state.filled_positions
    ]


    if remaining:
        for pos in remaining:
            print("-", pos)
    else:
        print("None")


    print("====================\n")

def show_final_team(state):

    print("\n🏁 FINAL TEAM\n")

    if state.manager:

        print(
            "👔 Manager:",
            state.manager["name"]
        )

    print("\nFormation:")
    print(state.formation)


    print("\nSquad:")

    total_rating = 0


    for position in state.available_positions:

        for player in state.selected_players:

            if player["position"] == position:

                p = player["player"]

                print(
                    f"{position}: "
                    f"{p['name']} "
                    f"| {p['rating']}"
                )

                total_rating += p["rating"]


    average = total_rating / len(state.selected_players)


    print(
        f"\n⭐ Squad Rating: {average:.1f}"
    )

def main():

    draft = DraftService()
    state = GameState()

    choose_formation(state)

    print("\n🎮 MAN UTD DRAFT GAME STARTED\n")


    while not state.formation_complete():

        show_draft_status(state)
        squad = draft.get_random_squad()


        print(f"\n🔥 {squad['season']}")
        print("Pick ONE player or manager:\n")
        print(
    f"🔄 Rerolls remaining: {state.rerolls}"
)
        print("Type R to reroll\n")


        available = []


        manager = squad["manager"]


        if (
            not state.is_manager_used(manager)
            and state.manager is None
        ):
            available.append({
                "type": "manager",
                "data": manager
            })


        for p in squad["players"]:

            if not state.is_player_used(p):

                available.append({
                    "type": "player",
                    "data": p
                })


        for i, item in enumerate(available):

            if item["type"] == "manager":

                m = item["data"]

                print(
                    f"{i}: 👔 {m['name']} | {m['rating']}"
                )

            else:

                p = item["data"]

                print(
                    f"{i}: {p['name']} "
                    f"({', '.join(p['positions'])}) | {p['rating']}"
                )



        while True:

            choice = input("\nSelect number or R: ")


            if choice.lower() == "r":

                if state.rerolls > 0:

                    state.rerolls -= 1

                    print(
                        "🔄 Squad rerolled!"
                    )

                    break

                else:

                    print(
                        "❌ No rerolls remaining"
                    )

                    continue


            choice = int(choice)


            if choice < 0 or choice >= len(available):

                print("Invalid selection")
                continue



            selected = available[choice]



            if selected["type"] == "manager":

                state.add_manager(
                    selected["data"]
                )

                print(
                    f"\n✅ Manager selected: "
                    f"{selected['data']['name']}"
                )

                break



            player = selected["data"]


            position = choose_position(
                player,
                state
            )


            if position is None:

                print(
                    "\n❌ Cannot place that player. Choose again."
                )

                continue



            state.add_player(
                player,
                position
            )


            state.filled_positions.append(position)


            print(
                f"\n✅ Added: {player['name']} as {position}"
            )


            break



            player = selected["data"]


            position = choose_position(
                player,
                state
            )


            if position is None:

                print(
                    "\n❌ Cannot place that player. Choose again."
                )

                continue



            state.add_player(
                player,
                position
            )


            state.filled_positions.append(position)


            print(
                f"\n✅ Added: {player['name']} as {position}"
            )


            break



    show_final_team(state)

if __name__ == "__main__":
    main()