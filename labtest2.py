# LABTEST 2 - CHO-HAN GAME

# Pedro Afonso Guimaraes Fernandes
# D23124885
# TU856

import random

class GameParticipant:
    # TASK 1
    """
        Represents the person playing and controls the players balance
    """
    def __init__(self, name: str, balance: float):
        """
            Initializes the participant
        """
        # two instance attributes:
        self.name = name
        self.balance = balance

    # TASK 1: controlling the player's balance
    def add_balance(self, amount: float):
        """
            Adds the amount to the balance
        """
        self.balance += amount

    def subtract_balance(self, amount: float):
        """
            Subtracts the amount from the balance
        """
        self.balance -= amount

    def __str__(self):
        return f"Name: {self.name}, Balance: {self.balance}"

# TASK 2
class Player(GameParticipant):
    """
        Represents a player and allows them to make bets
    """

    def __init__(self, name: str, balance: float):
        """
            initialize player
        """
        super().__init__(name, balance)

        # new instance attribute (TASK 2):
        self.bet = None

    def place_bet(self, amount: float, choice: str):
        """
            Place a bet on the game
        """
        # check if player has enough balance
        if amount > self.balance:
            raise ValueError("Insufficient Funds.")
        # validate choice
        if choice not in ["cho", "han"]:
            raise ValueError("Invalid Choice. Your choice must be 'Cho' or 'Han'")
        self.bet = {"amount": amount, "choice": choice}

        # once bet is placed, subtract it from the amount
        self.subtract_balance(amount)

    def check(self, outcome: str) -> bool:
        """
            Check if player made the right choice
        """
        return self.bet["choice"] == outcome

# TASK 3
class DiceCup:
    """
        Represents the dice cup (the two dice used for the game)
    """
    def __init__(self):
        """
            initialize the dice cup
        """
        self.dice = [0,0]

    # roll dices with random numbers between 1 and 6
    def roll_dice(self):
        """
            Rolls the dice
        """
        self.dice = [random.randint(1,6),random.randint(1,6)]

    def result(self):
        """
            check if sum is even or odd and return cho or han
        """
        total = sum(self.dice)
        if total % 2 == 0:
            return "cho"
        else:
            return "han"

    # display values of the dice
    def __str__(self):
        return f"Dice values: {self.dice[0]} and {self.dice[1]}"

# TASK 4: simulating the game
if __name__ == "__main__":
    # create player with name and starting balance
    player = Player(name = "Pedro Fernandes", balance = 100)
    print("CHO-HAN GAME")
    print("") # new line
    print(player)

    # dice cup instance
    dice_cup = DiceCup()

    # game time
    try:
        # prompt player for bet amount and choice and update their balance
        bet_amount = float(input("Enter bet amount: "))
        bet_choice = input("Choose 'Cho' or 'Han': ").strip().lower()

        # place bet
        player.place_bet(bet_amount, bet_choice)

        # roll the dice and determine the outcome
        dice_cup.roll_dice()
        outcome = dice_cup.result()

        print(dice_cup)
        print(f"The outcome is {outcome}!")
        print("")

        # check if the player wins or loses
        if player.check(outcome):
            amount_won = bet_amount * 2
            player.add_balance(amount_won)
            print(f"LETS GO, {player.name}! YOU WON!")
        else:
            print(f"Sorry, {player.name}. You lost {bet_amount}!")

        # print updated balance
        print("")
        print(player)
    except ValueError as e:
        print(f"Error: {e}")



