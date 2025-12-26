import random


class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards=[]
        self.create_deck()
        pass

    def create_deck(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.__cards.append((rank,suit))

# In shuffle_deck, random.shuffle() modifies the list in-place and returns None, so you shouldn't assign its result
    def shuffle_deck(self):
        random.shuffle(self.__cards)


    def deal_card(self):
        if self.__cards:
            first_card = self.__cards.pop()
            return first_card
        print("else card ", self.__cards)
        return None
        
    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"
