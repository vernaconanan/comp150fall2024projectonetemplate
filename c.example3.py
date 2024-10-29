## CODE FOR LEVELS 1 - 5 ##
import time

class Character:
    def __init__(self, name):
        self.name = name
        self.powerups = 0

    def break_obstacle(self):
        print(f"{self.name} is breaking an obstacle...")
        time.sleep(1)  # Simulate time taken to break
        print(f"{self.name} broke the obstacle!\n")

    def gain_powerup(self):
        self.powerups += 1
        print(f"{self.name} gained a power-up! Total power-ups: {self.powerups}\n")


class Game:
    def __init__(self):
        self.ralph = Character("Ralph")

    def start_level_1(self):
        print("Welcome to Level 1: The Tutorial")
        print("A virus is infecting the game, turning characters into monsters.")
        print("It's up to Ralph to save them!\n")
        
        input("Press Enter to continue...")
        
        # Introduce basic mechanics
        print("Ralph learns how to break obstacles!")
        time.sleep(1)
        
        # Simulate breaking the first obstacle
        self.ralph.break_obstacle()
        
        print("Ralph sees an infected character!")
        input("Press Enter to attempt to save them...")
        
        # Simulate another action
        self.ralph.break_obstacle()
        
        print("Ralph has saved the infected character!")
        self.ralph.gain_powerup()
        
        print("Tutorial complete! You have learned the basics of gameplay.")
        print("Now you can move on to the next level.\n")


# Start the game LEVEL 1:
if __name__ == "__main__":
    game = Game()
    game.start_level_1()
import time

class Character:
    def __init__(self, name):
        self.name = name
        self.powerups = 0

    def break_obstacle(self):
        print(f"{self.name} is breaking an obstacle...")
        time.sleep(1)  # Simulate time taken to break
        print(f"{self.name} broke the obstacle!\n")

    def gain_powerup(self):
        self.powerups += 1
        print(f"{self.name} gained a power-up! Total power-ups: {self.powerups}\n")


class Game:
    def __init__(self):
        self.ralph = Character("Ralph")
        self.infected_characters = 5  # Number of characters to save

    def start_level_2(self):
        print("Welcome to Level 2: Freeing Felix")
        print("Ralph needs to break free non-infected characters to find Felix.\n")

        while self.infected_characters > 0:
            action = input("Press 'b' to break an obstacle or 's' to skip: ").lower()
            if action == 'b':
                self.ralph.break_obstacle()
                self.infected_characters -= 1
                print(f"Ralph saved a non-infected character! {self.infected_characters} left to save.\n")
                self.ralph.gain_powerup()  # Gain a power-up for each character saved
            elif action == 's':
                print("Ralph is searching the area for clues...")
                time.sleep(1)
                print("Ralph finds some debris that can be broken!\n")
                self.ralph.break_obstacle()
            else:
                print("Invalid input! Please press 'b' to break or 's' to skip.")

        print("All non-infected characters have been freed!")
        print("Ralph has located Felix! Time to move to the next level.\n")


# Start the game LEVEL 2:
if __name__ == "__main__":
    game = Game()
    game.start_level_2()

import time
import random

class Character:
    def __init__(self, name):
        self.name = name
        self.powerups = 0

    def break_obstacle(self):
        print(f"{self.name} is breaking an obstacle...")
        time.sleep(1)  # Simulate time taken to break
        print(f"{self.name} broke the obstacle!\n")

    def gain_powerup(self):
        self.powerups += 1
        print(f"{self.name} gained a power-up! Total power-ups: {self.powerups}\n")

class Game:
    def __init__(self):
        self.ralph = Character("Ralph")
        self.debris_count = 5  # Number of debris to break
        self.powerups_found = 0

    def start_level_3(self):
        print("Welcome to Level 3: Finding the Back Staircase")
        print("Ralph needs to break through debris to find the staircase leading to Felix.\n")

        while self.debris_count > 0:
            action = input("Press 'b' to break an obstacle or 's' to search for power-ups: ").lower()
            if action == 'b':
                self.ralph.break_obstacle()
                self.debris_count -= 1
                self.ralph.gain_powerup()  # Gain a power-up for each debris broken
                print(f"Debris left to break: {self.debris_count}\n")
            elif action == 's':
                found = random.choice([True, False])
                if found:
                    self.powerups_found += 1
                    print(f"{self.ralph.name} found a hidden power-up! Total power-ups found: {self.powerups_found}\n")
                else:
                    print("No power-ups found this time.\n")
            else:
                print("Invalid input! Please press 'b' to break or 's' to search.")

        print("Ralph has cleared the path and found the back staircase!")
        print("Time to advance to Level 4.\n")


# Start the game LEVEL 3:
if __name__ == "__main__":
    game = Game()
    game.start_level_3()
import time

class Character:
    def __init__(self, name):
        self.name = name
        self.powerups = 0

    def break_obstacle(self):
        print(f"{self.name} is breaking an obstacle...")
        time.sleep(1)  # Simulate time taken to break
        print(f"{self.name} broke the obstacle!\n")

    def gain_powerup(self):
        self.powerups += 1
        print(f"{self.name} gained a power-up! Total power-ups: {self.powerups}\n")


class Game:
    def __init__(self):
        self.ralph = Character("Ralph")
        self.felix_locked = True  # Indicates if Felix is locked
        self.bars_broken = 0
        self.total_bars = 3  # Number of bars to break to unlock Felix

    def start_level_4(self):
        print("Welcome to Level 4: Unlocking Felix")
        print("Ralph needs to break the bars to free Felix.\n")

        while self.felix_locked:
            action = input("Press 'b' to break a bar or 's' to check surroundings: ").lower()
            if action == 'b':
                if self.bars_broken < self.total_bars:
                    self.ralph.break_obstacle()
                    self.bars_broken += 1
                    print(f"Bars left to break: {self.total_bars - self.bars_broken}\n")
                    if self.bars_broken == self.total_bars:
                        self.felix_locked = False  # Unlock Felix
                        print("Felix is now free!")
                        print("Felix reveals that his hammer has been taken. We need to find it!\n")
                else:
                    print("All bars are already broken!\n")
            elif action == 's':
                print("Ralph searches the area but finds nothing useful.\n")
            else:
                print("Invalid input! Please press 'b' to break or 's' to search.")

        print("Ralph and Felix will now search for the hammer in the next level!\n")


# Start the game LEVEL 4:
if __name__ == "__main__":
    game = Game()
    game.start_level_4()

import time
import random

class Character:
    def __init__(self, name):
        self.name = name
        self.powerups = 0

    def break_obstacle(self):
        print(f"{self.name} is breaking an obstacle...")
        time.sleep(1)  # Simulate time taken to break
        print(f"{self.name} broke the obstacle!\n")

    def gain_powerup(self):
        self.powerups += 1
        print(f"{self.name} gained a power-up! Total power-ups: {self.powerups}\n")


class Game:
    def __init__(self):
        self.ralph = Character("Ralph")
        self.felix = Character("Fix-It Felix")
        self.puzzles_solved = 0
        self.total_puzzles = 3  # Number of puzzles to solve

    def start_level_5(self):
        print("Welcome to Level 5: Solving Puzzles with Felix")
        print("Felix must solve puzzles to find his hammer while Ralph breaks obstacles.\n")

        while self.puzzles_solved < self.total_puzzles:
            action = input("Press 'p' to solve a puzzle or 'b' to have Ralph break an obstacle: ").lower()
            if action == 'p':
                self.solve_puzzle()
            elif action == 'b':
                self.ralph.break_obstacle()
            else:
                print("Invalid input! Please press 'p' to solve a puzzle or 'b' to break an obstacle.")

        print("Felix has solved all the puzzles and located his hammer!")
        print("Ralph and Felix are ready to take on the next challenge!\n")

    def solve_puzzle(self):
        # Simulating a simple puzzle-solving mechanic
        print(f"{self.felix.name} is attempting to solve a puzzle...")
        time.sleep(1)  # Simulate time taken to solve
        success = random.choice([True, False])  # Random success/failure

        if success:
            self.puzzles_solved += 1
            print(f"{self.felix.name} solved a puzzle! Puzzles solved: {self.puzzles_solved}/{self.total_puzzles}\n")
            self.felix.gain_powerup()  # Gain a power-up for each puzzle solved
        else:
            print(f"{self.felix.name} failed to solve the puzzle. Try again!\n")


# Start the game
if __name__ == "__main__":
    game = Game()
    game.start_level_5()
#### Felix is solving puzzles and Ralph is assisting while wrecking obtascles.