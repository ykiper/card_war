from utils.deck import shuffle, create_deck, compare_cards

def create_player(name="AI") -> dict:
    return {"name": name, "hand": [], "won_pile": []}



def init_game() -> dict:
    yossi = create_player("yossi")
    AI = create_player()

    deck = create_deck()

    shuffle(deck)

    yossi["hand"] = deck[0:26]
    AI["hand"] = deck[26:52]

    shuffle(deck)

    game_dict = {"deck": deck, "player_1": yossi, "player_2": AI}
    return game_dict

def play_round(p1: dict, p2: dict):

    winner = compare_cards(p1["hand"][0], p2["hand"][0])
    if winner == "p1":
        p1["won_pile"].append(p1["hand"][0])
        p1["won_pile"].append(p2["hand"][0])
    elif winner == "p2":
        p2["won_pile"].append(p1["hand"][0])
        p2["won_pile"].append(p2["hand"][0])

    p1["hand"].pop(0)
    p2["hand"].pop(0)



