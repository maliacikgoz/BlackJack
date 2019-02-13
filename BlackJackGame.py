import random

while True:
    print("""
    ----------------
    -   New Game   -
    ----------------""")

    dealer_cards = []
    player_cards = []

    # Dealer's cards initial
    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1, 10))

        if len(dealer_cards) == 2:
            print("Dealer's cards: X", dealer_cards[1], sep=", ")
    # Player's cards initial
    while len(player_cards) != 2:
        player_cards.append(random.randint(1, 10))
        if len(player_cards) == 2:
            print("Your cards:   ", player_cards)

    # Check BLACKJACKS
    while sorted(dealer_cards) == sorted(player_cards) == [1, 10]:
        print("TIE! You both have BLACKJACK")

        if sorted(dealer_cards) == [1, 10]:
            print("Dealer has BLACKJACK, You lose")

        elif sorted(player_cards) == [1, 10]:
            print("BLACKJACK, You win")
        else:
            pass
            # Sum of the Dealer cards
            if sum(dealer_cards) == 21:
                print("Dealer has 21 and You Lose!")
            elif sum(dealer_cards) > 21:
                print("Dealer has Busted!")
    # Sum of the Player Cards
    while sum(player_cards) < 21:
        action_taken = str(input("Do you want to [stand] or [hit] ? ")).lower()
        if action_taken == "hit":
            player_cards.append(random.randint(1, 11))
            print("Your cards: ", player_cards)

        elif action_taken == "stand":
            print("Dealer's cards: ", dealer_cards)
            # Sum of the Player Cards
            if sum(dealer_cards) > sum(player_cards):
                print("You Lose!")
                break
            else:
                print("You Win!")
                break
        else:
            print("-Please write [hit] or [stay]")

    if sum(player_cards) == 21:
        print("You reached 21, You win!")
        print("Dealer's cards: ", dealer_cards)

    elif sum(player_cards) > 21:
        print("You Busted!")
        print("Dealer's cards: ", dealer_cards)
    else:
        pass

