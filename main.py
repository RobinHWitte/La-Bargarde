from src.card import Card
from src.player import Player
from src.game import Game


def create_deck() -> list:
    return [
        Card("Warrior", 1, 1, 1),
        Card("Archer", 2, 2, 1),
        Card("Knight", 3, 3, 3),
        Card("Giant", 5, 5, 5),
    ] * 2


if __name__ == "__main__":
    player_deck = create_deck()
    opponent_deck = create_deck()
    player = Player("Player", player_deck)
    opponent = Player("AI", opponent_deck)
    game = Game(player, opponent)
    game.start()