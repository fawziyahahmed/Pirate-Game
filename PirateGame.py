import random  # Importing the random module for generating random numbers.

class PirateGame:  # Declaring a class named PirateGame.
    def __init__(self, initial_bank=100):  # Initializing the PirateGame class with an optional parameter initial_bank.
        self.bank = initial_bank  # Initializing the bank attribute with the initial_bank value.
        self.treasure_chest = ['Gold', 'Diamond', 'Gems', 'Toy', 'Rock', 'Shoe']  # Initializing the treasure_chest attribute with a list of treasure items.

    def play(self):  # Defining a method named play within the PirateGame class.
        # Printing a welcome message and explaining the game rules.
        print("Welcome to the Pirate's Game of Chance!")
        print("You currently have {} coins in your bank.".format(self.bank))
        print("In this game, you have the chance to find various treasures in the chest.")
        print("Here are the potential outcomes:")
        print("- If you find Gold, you will double your wager.")
        print("- If you find a Diamond, you will triple your wager.")
        print("- If you find Gems, you will earn your wager plus one third of it.")
        print("- If you find a Toy, you will lose twice your wager.")
        print("- If you find a Shoe, you will lose your entire wager.")
        print("- If you find a Rock, you will lose three times your wager.\n")

        while self.bank > 0:  # Starting a loop that continues until the bank balance is zero or negative.
            wager = self.get_wager()  # Getting the wager from the user.
            item = random.choice(self.treasure_chest)  # Selecting a random item from the treasure chest.
            print("You wagered {} coins...".format(wager))  # Displaying the user's wager.
            print("You grabbed from the treasure chest and found: {}".format(item))  # Displaying the item found.

            # Determining the outcome based on the item found and updating the bank balance accordingly.
            if item == 'Gold':
                winnings = wager * 2
                print("Congratulations! You found Gold and doubled your wager! You won {} coins!".format(winnings))
            elif item == 'Diamond':
                winnings = wager * 3
                print("Congratulations! You found a Diamond and tripled your wager! You won {} coins!".format(winnings))
            elif item == 'Gems':
                winnings = wager + wager // 3
                print("Congratulations! You found Gems and won {} coins!".format(winnings))
            elif item == 'Toy':
                winnings = -wager * 2
                print("Sorry, you found a Toy. You lost {} coins.".format(wager * 2))
            elif item == 'Shoe':
                winnings = -wager
                print("Sorry, you found a Shoe. You lost {} coins.".format(wager))
            elif item == 'Rock':
                winnings = -wager * 3
                print("Sorry, you found a Rock. You lost {} coins.".format(wager * 3))

            self.bank += winnings  # Updating the bank balance with the winnings.
            print("Your current bank balance is: {} coins.\n".format(self.bank))  # Displaying the updated bank balance.

        print("Game Over! You've run out of coins.")  # Printing a game over message when the bank balance is zero or negative.

    def get_wager(self):  # Defining a method named get_wager within the PirateGame class.
        while True:  # Starting an infinite loop.
            try:
                wager = int(input("Enter your wager (up to {} coins): ".format(self.bank)))  # Getting the wager input from the user.
                if wager <= 0:  # Checking if the wager is less than or equal to zero.
                    print("Please enter a positive wager.")  # Prompting the user to enter a positive wager.
                elif wager > self.bank:  # Checking if the wager is greater than the bank balance.
                    print("You don't have enough coins to make that wager!")  # Prompting the user that they don't have enough coins.
                else:
                    return wager  # Returning the valid wager entered by the user.
            except ValueError:  # Handling the ValueError exception if the input is not an integer.
                print("Please enter a valid integer wager.")  # Prompting the user to enter a valid integer.

# Example usage
game = PirateGame()  # Creating an instance of the PirateGame class.
game.play()  # Calling the play method to start the game.