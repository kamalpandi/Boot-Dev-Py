fireball_damage = 500
potion_mana = 100


class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def get_fireballed(self) -> None:
        self.health = self.health -500
        pass

    def drink_mana_potion(self) -> None:
        self.mana = self.mana +100
        pass
