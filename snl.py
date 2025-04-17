import random

# Player class to hold player name and position
class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, steps):
        self.position += steps
        if self.position > 100:
            self.position = 100

    def set_position(self, pos):
        self.position = pos

# Board class to hold snakes and ladders
class Board:
    def __init__(self):
        self.snakes = {
            16: 6, 48: 30, 62: 19, 88: 24,
            95: 56, 97: 78
        }
        self.ladders = {
            1: 38, 4: 14, 8: 30, 21: 42,
            28: 76, 50: 67, 71: 92, 80: 99
        }

    def check_snakes_ladders(self, position):
        if position in self.snakes:
            print(f"🐍 Bitten by a snake at {position}! Going down to {self.snakes[position]}")
            return self.snakes[position]
        elif position in self.ladders:
            print(f"🪜 Climbed a ladder at {position}! Going up to {self.ladders[position]}")
            return self.ladders[position]
        return position

# Function to simulate dice roll
def roll_dice():
    return random.randint(1, 6)

# Main game logic
def main():
    print("🎲 Welcome to Snake and Ladders Game!\n")
    name1 = input("Enter name for Player 1: ")
    name2 = input("Enter name for Player 2: ")

    board = Board()
    p1 = Player(name1)
    p2 = Player(name2)
    players = [p1, p2]

    while True:
        for player in players:
            input(f"\n{player.name}'s turn. Press Enter to roll the dice...")
            dice = roll_dice()
            print(f"{player.name} rolled a {dice}")
            player.move(dice)
            player.set_position(board.check_snakes_ladders(player.position))
            print(f"{player.name} is now at position {player.position}")

            if player.position == 100:
                print(f"\n🏆 {player.name} WINS the game! Congratulations!")
                return

if __name__ == "__main__":
    main()
