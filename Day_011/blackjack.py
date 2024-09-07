# The task of day 11 was creating a simple blackjack game.
# There are no probabilities added in this game.
# The considered rules were:
#   - On game start, two cards are drawn by the player and the dealer.
#   - When the player goes over 21, the player loses.
#   - When the dealer goes over 21, the dealer loses.
#   - When both the player and the dealer go over 21, its a draw.
#   - When both the player and the dealer have the same score, its a draw.
#   - If the dealer has less than 17 points, the dealer draws more cards until the dealer has 17 or more points.
#   - If needed, to prevent going over 21 points, the Ace is treated as a 1 point card.

from ascii_art import logo
import random
import os

# * Clears the screen.
def cls():
    os.system("cls" if os.name == "nt" else "clear")


def draw():
    """
    Draws a random card from the available cards list
    """

    global cards

    return random.choice(list(cards.keys()))


def start_game():
    """
    Starts the game by populating the dealer's and player's hands.
    """

    global dealer
    global player

    for i in range(2):
        dealer.append(draw())
        player.append(draw())

    print(logo)


def get_cards(x):
    """
    Gets the cards from either the player or the dealer
    """
    if x == "player":
        global player
        global player_sum
        player_sum = 0
        for card in player:
            player_sum += int(cards[card])
        # ? Treats the ace card as a 1 point card, if needed.
        if player_sum > 21 and "A" in player:
            player_sum -= 10
        if player_sum >= 21:
            get_winner()
        else:
            print(f"Your cards: {player}, current score: {player_sum}")
    elif x == "dealer":
        global dealer
        print(f"Dealer's first card: {dealer[0]}")


def get_game_status():
    """
    Displays the dealer's and player's cards aswell as total points on the screen.
    """

    global is_game_over

    get_cards("player")
    if not is_game_over:
        get_cards("dealer")


def get_winner():
    global is_game_over
    global player_sum
    dealer_sum = 0
    # ? Displays player's hand.
    print(f"Your cards: {player}, final score: {player_sum}")
    # ? Displays dealer's hand.
    for card in dealer:
        dealer_sum += int(cards[card])
    while dealer_sum <= 17:
        dealer.append(draw())
        dealer_sum = 0
        for card in dealer:
            dealer_sum += int(cards[card])
        # ? Treats the ace card as a 1 point card, if needed.
        if dealer_sum > 21 and "A" in dealer:
            dealer_sum -= 10
    print(f"Dealer's cards: {dealer}, final score: {dealer_sum}")
    if player_sum > 21 and dealer_sum > 21:
        print("You both went over 21, it's a draw!")
    elif player_sum > dealer_sum and player_sum <= 21:
        print("You won!")
    elif player_sum > dealer_sum and player_sum > 21:
        print("You went over 21, dealer wins!")
    elif player_sum == dealer_sum:
        print("It's a draw!")
    elif player_sum < dealer_sum and dealer_sum >= 21:
        print("The dealer went over 21, you win!")
    elif player_sum < dealer_sum and dealer_sum <= 21:
        print("You lost!")

    is_game_over = True


cards = {
    "A": "11",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "10",
    "J": "10",
    "Q": "10",
    "K": "10",
}

is_play_again = True

while is_play_again:
    cls()
    dealer = []
    player = []
    player_sum = 0
    is_game_over = False
    start_game()
    get_game_status()

    while not is_game_over:
        draw_card = ""
        while draw_card != "y" and draw_card != "n":
            draw_card = input("Draw another card? [Y/N]: ").lower()
            if draw_card != "y" and draw_card != "n":
                print("Error: Invalid input. Try again.")
        if draw_card == "y":
            player.append(draw())
            get_game_status()
        elif draw_card == "n":
            get_winner()
    play_again = ""
    while play_again != "y" and play_again != "n":
        play_again = input("Would you like to play again? [Y/N]: ").lower()
        if play_again != "y" and play_again != "n":
            print("Error: Invalid input!")
    match play_again:
        case "y":
            is_play_again = True
        case "n":
            is_play_again = False
