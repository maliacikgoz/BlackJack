import random

# TODO: Add betting with money
# TODO: Add card decks
# TODO: Generate cards from card decks
# TODO: Shuffle the card decs with shuffle module
# TODO: Add soft hand feature (Ace 1/11)
# TODO: Add lagging while hitting the cards with time module
# TODO: Add doubling feature
# TODO: Add splitting feature
# TODO: Change into OOP Concept

# Game plays non-stop (True)
while True:
    print("""
    ----------------
    -   New Game   -
    ----------------""")

    dealer_cards = []
    player_cards = []
    action_taken = ""

    # Dealer's cards initials
    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1, 10))
    #Hide the first card of Dealer
    print("Dealer's cards: X", dealer_cards[1:], sep=", ")

    # Player's cards initial
    while len(player_cards) != 2:
        player_cards.append(random.randint(1, 10))
        if len(player_cards) == 2:
            print("Your cards:   ", player_cards)

        # Check BLACKJACKS
    #Check if we both have Blackjack
    while sorted(dealer_cards) == sorted(player_cards) == [1, 10]:
        print("TIE! You both have BLACKJACK")
    #Check if Dealer has Blackjack
        if sorted(dealer_cards) == [1, 10]:
            print("Dealer has BLACKJACK, You lose")
    #Check if Player has Blackjack
        elif sorted(player_cards) == [1, 10]:
            print("BLACKJACK, You win")
        else:
            pass

    # Ask if player wants to stand or hit
    while sum(player_cards) < 21 and action_taken != "stand":
        action_taken = str(input("Do you want to [stand] or [hit] ? ")).lower()

        if action_taken == "hit":
            player_cards.append(random.randint(1, 11))
            print("Your cards: ", player_cards)

        elif action_taken == "stand":
            # Dealer must have a hand over 16
            # If it's less, add new card till reach 17 at least
            while sum(dealer_cards) < 17:
                dealer_cards.append(random.randint(1, 10))
                # Sum of the Dealer cards
                if sum(dealer_cards) == 21:
                    print("Dealer has 21!")
                elif sum(dealer_cards) > 21:
                    print("Dealer has Busted!")
                print("Dealer's cards: ", dealer_cards)

            # Compare the hands
            while sum(dealer_cards) <= 21:
                if sum(dealer_cards) > sum(player_cards):
                    print("You Lose!")
                else:
                    print("You Win!")
                break
        else:
            print("Please write [stand] or [hit]")

    if sum(player_cards) == 21:
        print("You reached 21, You win!")
        print("Dealer's cards: ", dealer_cards)

    elif sum(player_cards) > 21:
        print("You Busted!")
        print("Dealer's cards: ", dealer_cards)
    else:
        pass
