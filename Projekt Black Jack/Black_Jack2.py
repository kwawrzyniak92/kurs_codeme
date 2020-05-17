import random
class Card:
    RANKS = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
    SUITS = ["♣", "♦","♥","♠"]

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep  = self.rank + self.suit
        return rep
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<pusta>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
            random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Koniec kart!")

deck1 = Deck()
print("Utworzono nową talię.")
print("Talia:")
print(deck1)
deck1.populate()
print("\nDodałem do talii komplet kart.")
print("Talia:")
print(deck1)
deck1.shuffle()
print("Talia potasowana ")
print(deck1)

my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]
deck1.deal(hands, per_hand = 5)

print("\nRozdałem graczom po 5 kart.")
print("Moja ręka:")
print(my_hand)
print("Twoja ręka:")
print(your_hand)
print("Talia:")
print(deck1)
deck1.clear()
print("Talia kart usunięta!")
print("Talia:", deck1)
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")



