import time
import random

class Character:
    def __init__(self, name, vitality, experience=0, level=1):
        self.name = name
        self.vitality = vitality
        self.experience = experience
        self.level = level
        self.powerups = 0

    def level_up(self):
        self.level += 1
        self.vitality += 5
        print(f"{self.name} leveled up to level {self.level}! Vitality is now {self.vitality}.")

    def break_obstacle(self):
        print(f"{self.name} is breaking an obstacle...")
        time.sleep(1)
        print(f"{self.name} broke the obstacle!\n")

    def gain_powerup(self):
        self.powerups += 1
        print(f"{self.name} gained a power-up! Total power-ups: {self.powerups}")

class Event:
    def __init__(self, description, choices):
        self.description = description
        self.choices = choices

    def trigger_event(self, character):
        print(self.description)
        for i, choice in enumerate(self.choices):
            print(f"{i + 1}. {choice['description']}")
        choice = int(input("Choose an option: ")) - 1
        outcome = self.choices[choice]['outcome']
        self.resolve_outcome(character, outcome)

    def resolve_outcome(self, character, outcome):
        success = random.choice([True, False])  # Simplified success check
        if success:
            print(outcome['success'])
            character.experience += outcome['experience']
        else:
            print(outcome['failure'])
            character.vitality -= outcome['damage']
        if character.experience >= 20:
            character.level_up()
            character.experience = 0

class Game:
    def __init__(self):
        self.ralph = Character("Ralph", vitality=20)
        self.inventory = Inventory()

    def start_level_1(self):
        print("Welcome to Level 1: The Tutorial")
        self.ralph.break_obstacle()
        self.ralph.gain_powerup()

    def start_level_2(self):
        print("Welcome to Level 2: Freeing Felix")
        infected_characters = 5
        while infected_characters > 0:
            action = input("Press 'b' to break an obstacle or 's' to skip: ").lower()
            if action == 'b':
                self.ralph.break_obstacle()
                infected_characters -= 1
                self.ralph.gain_powerup()
                print(f"Infected characters left to save: {infected_characters}")
            elif action == 's':
                print("Searching for obstacles...")
                time.sleep(1)
            else:
                print("Invalid input! Please press 'b' to break an obstacle or 's' to skip.")

        # When all infected characters are saved, break the loop and proceed
        print("All infected characters have been saved! Proceeding to the next level...\n")


    def start_level_3(self):
        print("Welcome to Level 3: Finding the Back Staircase")
        debris_count = 5
        while debris_count > 0:
            action = input("Press 'b' to break an obstacle or 's' to search for power-ups: ").lower()
            if action == 'b':
                self.ralph.break_obstacle()
                debris_count -= 1
                self.ralph.gain_powerup()
            elif action == 's':
                print("Searching for power-ups...")
                time.sleep(1)

    def start_level_4(self):
        print("Welcome to Level 4: Unlocking Felix")
        bars_broken = 0
        total_bars = 3
        while bars_broken < total_bars:
            action = input("Press 'b' to break a bar or 's' to check surroundings: ").lower()
            if action == 'b':
                self.ralph.break_obstacle()
                bars_broken += 1

    def start_level_5(self):
        print("Welcome to Level 5: Solving Puzzles with Felix")
        puzzles_solved = 0
        total_puzzles = 3
        while puzzles_solved < total_puzzles:
            action = input("Press 'p' to solve a puzzle or 'b' to break an obstacle: ").lower()
            if action == 'p':
                puzzles_solved += 1
                print(f"Solved puzzle {puzzles_solved} of {total_puzzles}")
                
    def start_level_6(self):
        print("Welcome to Level 6: Solving Puzzles and Finding the Hammer")
        puzzles_solved = 0
        total_puzzles = 3
        while puzzles_solved < total_puzzles:
            action = input("Press 'p' to have Felix solve a puzzle or 'b' to have Ralph break an obstacle: ").lower()
            if action == 'p':
                puzzles_solved += 1
                print(f"Felix solved puzzle {puzzles_solved} of {total_puzzles}.")
                if puzzles_solved == total_puzzles:
                    print("Felix has found his hammer!")
            elif action == 'b':
                self.ralph.break_obstacle()
            else:
                print("Invalid input! Please press 'p' for puzzle or 'b' to break obstacles.")

    def run(self):
        levels = [self.start_level_1, self.start_level_2, self.start_level_3, self.start_level_4, self.start_level_5]
        for level in levels:
            level()

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        self.items[item_name] = self.items.get(item_name, 0) + quantity
        print(f"Added {quantity} {item_name}(s) to your inventory.")

    def use_item(self, item_name, character):
        if self.items.get(item_name, 0) > 0:
            print(f"{character.name} uses {item_name}.")
            if item_name == "Health Potion":
                character.vitality += 10
                print(f"{character.name} regained 10 vitality points!")
            self.items[item_name] -= 1
        else:
            print(f"No {item_name} left in inventory.")

# Initialize and run the game
game = Game()
game.run()
