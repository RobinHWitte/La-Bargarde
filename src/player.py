from typing import List
from .card import Card

class Player:
    def __init__(self, name: str, deck: List[Card]):
        self.name = name
        self.deck = deck
        self.hand: List[Card] = []
        self.board: List[Card] = []
        self.mana = 0
        self.max_mana = 0
        self.health = 30

    def draw_card(self):
        if self.deck:
            card = self.deck.pop(0)
            self.hand.append(card)
            print(f"{self.name} drew {card.name}")

    def start_turn(self):
        self.max_mana = min(10, self.max_mana + 1)
        self.mana = self.max_mana
        self.draw_card()

    def play_card(self, card_index: int):
        if card_index < 0 or card_index >= len(self.hand):
            print("Invalid card index")
            return
        card = self.hand[card_index]
        if card.mana_cost > self.mana:
            print("Not enough mana")
            return
        self.mana -= card.mana_cost
        self.hand.pop(card_index)
        self.board.append(card)
        print(f"{self.name} played {card}")
