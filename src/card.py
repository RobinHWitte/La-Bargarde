class Card:
    def __init__(self, name: str, mana_cost: int, attack: int, health: int):
        self.name = name
        self.mana_cost = mana_cost
        self.attack = attack
        self.health = health

    def __str__(self):
        return f"{self.name} (Cost:{self.mana_cost} Atk:{self.attack} HP:{self.health})"