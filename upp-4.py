import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        names = {
            11: "J",
            12: "D",
            13: "K",
            14: "A"
        }

        value = names.get(self.value, self.value)

        return f"{self.suit} {value}"


class Deck:
    def __init__(self, cards):
        self.cards = cards

    def deal(self, num_cards):
        if num_cards > len(self.cards):
            raise ValueError("inte tillräckligt många kort")

        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]

        return dealt_cards

    def shuffle(self):
        cards = self.cards

        for i in range(len(cards)-1,0,-1):
            random_card = random.randint(0, i)

            temp_card = cards[i]
            cards[i] = cards[random_card]
            cards[random_card] = temp_card

    @staticmethod
    def make_deck():
        cards = []
        suits = ["♠", "♥", "♣", "♦"]

        for suit in suits:
            for value in range(2, 15):
                cards.append(Card(suit, value))

        return cards


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def take_cards(self, cards):
        self.hand.extend(cards)

    def play_card(self):
        return self.hand.pop() if self.hand else None


def low_or_high():
    deck = Deck(Deck.make_deck())
    deck.shuffle()

    guess = input("välj lågt [L] eller högt [H] : ")

    card = deck.deal(1)[0]

    print("du drog:", card)

    if card.value <=7:
        result = "lågt"

    else:
        result = "högt"

    print("fortet är: ", result)

    if guess == result:
        print("Du vann")
    else:
        print("du förlorade")

def play_game():
    deck = Deck(Deck.make_deck())
    deck.shuffle()

    player1 = Player("Spelare 1")
    player2 = Player("Spelare 2")

    player1.take_cards(deck.deal(1))
    card1 = player1.play_card()

    player2.take_cards(deck.deal(1))
    card2 = player2.play_card()

    print()
    print(player1.name, "fick:", card1)
    print(player2.name, "fick:", card2)

    if card1.value > card2.value:
        print(f"\n{player1.name} vinner!")

    elif card2.value > card1.value:
        print(f"\n{player2.name} vinner!")

    else:
        print("\nOavgjort!")


game = input("vilket spel fill du spela\n"
"\n[1] KORT MOT KORT"
"\n[2] eller HÖGT ELLER LÅGT" \
"\n: ")

if game == 1:

    while True:
        play_game()

        again = input("\nVill du spela igen? (ja/nej): ").lower()

        if again == "nej":
            print("Spelet avslutas.")
            break
else:
    while True:
        low_or_high()

        again = input("\nVill du spela igen? (ja/nej): ").lower()

        if again == "nej":
            print("Spelet avslutas.")
            break