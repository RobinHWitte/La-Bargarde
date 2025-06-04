from typing import List
from .card import Card
from .player import Player

class Game:
    def __init__(self, player: Player, opponent: Player):
        self.player = player
        self.opponent = opponent
        self.turn = 0

    def start(self):
        print("Starting game!")
        for _ in range(3):
            self.player.draw_card()
            self.opponent.draw_card()
        self.game_loop()

    def game_loop(self):
        while self.player.health > 0 and self.opponent.health > 0:
            self.turn += 1
            print(f"\n-- Turn {self.turn} --")
            self.player.start_turn()
            self.player_turn()
            if self.opponent.health <= 0:
                break
            self.opponent.start_turn()
            self.opponent_ai_turn()

        winner = self.player if self.player.health > 0 else self.opponent
        print(f"{winner.name} wins!")

    def player_turn(self):
        print(f"{self.player.name}'s hand: ")
        for i, card in enumerate(self.player.hand):
            print(f"{i}: {card}")
        choice = input("Choose card to play (index or 'pass'): ")
        if choice.isdigit():
            self.player.play_card(int(choice))

    def opponent_ai_turn(self):
        if self.opponent.hand:
            self.opponent.play_card(0)
        else:
            print(f"{self.opponent.name} passes.")
