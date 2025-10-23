from random import randint


def create_card(rank: str, suite: str) -> dict:
    spacial_rank_dict = {"J": 11, "Q": 12, "K": 13, "A": 14}
    if rank.isnumeric():
        value = rank
    else:
        value = spacial_rank_dict[rank]
    return {"rank": rank, "suite": suite, "value": value}


def compare_cards(p1_card: dict, p2_card: dict) -> str:
    if int(p1_card["value"]) > int(p2_card["value"]):
        return "p1"
    if int(p2_card["value"]) > int(p1_card["value"]):
        return "p2"
    return "war"


def create_deck() -> list[dict]:
    full_deck = []

    rank_list = ["2", "3", "4", "5", "6", "7", "8", "9",
                 "10", "J", "Q", "K", "A"]

    suite_list = ["H", "C", "D", "S"]

    for rank in rank_list:
        for suite in suite_list:
            full_deck.append(create_card(rank, suite))

    return full_deck


def shuffle(deck: list[dict]) -> list[dict]:
    for _ in range(1000):
        while True:
            index1 = randint(2, 51)
            index2 = randint(2, 51)
            if index1 != index2:
                break

        deck[index1], deck[index2] = deck[index2], deck[index1]

    return deck

shuffle(create_deck())