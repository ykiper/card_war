from game_logic.game import create_player, init_game, play_round


if __name__ == "__main__":
    game_dict = init_game()
    play_round(game_dict["player_1"], game_dict["player_2"])
    if game_dict["player_1"]["hand"] == 0 or game_dict["player_2"]["hand"] == 0:
        exit()

