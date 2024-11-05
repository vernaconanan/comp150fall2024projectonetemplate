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

import unittest

class TestGame(unittest.TestCase):

    def setUp(self):
        self.ralph = Character("Ralph", vitality=20)
        self.felix = Character("Felix", vitality=15)

    def test_level_up(self):
        self.ralph.experience = 20
        self.ralph.level_up()
        self.assertEqual(self.ralph.level, 2)
        self.assertEqual(self.ralph.vitality, 25)

    def test_break_obstacle(self):
        # Testing method with just a print statement, so using mock for print
        with unittest.mock.patch('builtins.print') as mocked_print:
            self.ralph.break_obstacle()
            mocked_print.assert_any_call("Ralph is breaking an obstacle...")
            mocked_print.assert_any_call("Ralph broke the obstacle!\n")

    def test_gain_powerup(self):
        self.ralph.gain_powerup()
        self.assertEqual(self.ralph.powerups, 1)
        self.ralph.gain_powerup()
        self.assertEqual(self.ralph.powerups, 2)

    def test_event_trigger(self):
        description = "A wild obstacle appears!"
        choices = [
            {"description": "Break the obstacle", "outcome": {"success": "Obstacle broken!", "failure": "Failed to break the obstacle!", "experience": 10, "damage": 5}},
            {"description": "Avoid the obstacle", "outcome": {"success": "Avoided successfully!", "failure": "Could not avoid!", "experience": 5, "damage": 2}}
        ]
        event = event(description, choices)
        with unittest.mock.patch('builtins.input', return_value='1'):
            with unittest.mock.patch('builtins.print'):
                event.trigger_event(self.ralph)
        self.assertEqual(self.ralph.experience, 10)

    def test_game_levels(self):
        game = Game()
        with unittest.mock.patch('builtins.print'):
            game.start_level_1()
            self.assertEqual(game.ralph.powerups, 1)

            game.start_level_2()
            self.assertGreaterEqual(game.ralph.powerups, 1)

            game.start_level_3()
            self.assertGreaterEqual(game.ralph.powerups, 1)

            game.start_level_4()
            # Continue adding assertions for different levels based on game requirements

if __name__ == '__main__':
    unittest.main()

## RUN CODE WITH THIS:
   # python -m unittest discover -s tests

import unittest

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()  # Create an instance of the Game

    def test_character_fail_to_break_obstacle(self):
        initial_vitality = self.game.character.vitality
        # Simulate an attempt to break an obstacle (test failure condition)
        self.assertEqual(initial_vitality, self.game.character.vitality)
    
    def test_inventory_add_item(self):
        self.game.inventory.add_item("Health Potion", 5)
        self.assertIn("Health Potion", self.game.inventory.items)
        self.assertEqual(self.game.inventory.items["Health Potion"], 5)
    
    def test_inventory_use_item(self):
        self.game.inventory.add_item("Health Potion", 1)
        self.game.inventory.use_item("Health Potion", self.game.character)
        self.assertEqual(self.game.character.vitality, 110)  # Assuming health potion gives 10 vitality
        self.assertEqual(self.game.inventory.items["Health Potion"], 0)
    
    def test_inventory_use_item_when_empty(self):
        self.game.inventory.use_item("Health Potion", self.game.character)
        self.assertEqual(self.game.character.vitality, 100)  # No effect because the inventory was empty

    def test_level_up(self):
        self.game.character.experience = 20  # Enough experience to level up
        self.game.character.level_up()
        self.assertEqual(self.game.character.level, 2)  # Character should have leveled up

if __name__ == '__main__':
    unittest.main()

# Alt unit testing code:
import unittest
from unittest.mock import patch
from io import StringIO
import random
class TestGame(unittest.TestCase):

    def setUp(self):
        """Set up the test environment for the game"""
        self.game = Game()

    @patch('random.choice', return_value=False)  # Simulate failure in breaking the obstacle
    def test_character_fail_to_break_obstacle(self, mock_random):
        """Test that the character fails to break the obstacle."""
        initial_vitality = self.game.character.vitality
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.game.character.break_obstacle()  # Attempt to break the obstacle
            
        output = mock_stdout.getvalue().strip()
        self.assertIn("failed to break the obstacle", output)
        self.assertEqual(self.game.character.vitality, initial_vitality - 1)  # Vitality should decrease by 1

    def test_inventory_add_item(self):
        """Test adding an item to the inventory."""
        self.game.inventory.add_item("Health Potion", 5)
        self.assertEqual(self.game.inventory.items.get("Health Potion", 0), 5)

    def test_inventory_use_item(self):
        """Test using an item from the inventory."""
        self.game.inventory.add_item("Health Potion", 1)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.game.inventory.use_item("Health Potion", self.game.character)
        
        output = mock_stdout.getvalue().strip()
        self.assertIn("Ralph uses Health Potion", output)
        self.assertEqual(self.game.character.vitality, 30)  # Assuming vitality starts at 20 and potion adds 10

    def test_inventory_use_item_when_empty(self):
        """Test trying to use an item when it's not in the inventory."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.game.inventory.use_item("Health Potion", self.game.character)
        
        output = mock_stdout.getvalue().strip()
        self.assertIn("No Health Potion left in inventory", output)

    def test_level_up(self):
        """Test the character leveling up after gaining enough experience."""
        self.game.character.experience = 20  # Enough to level up
        current_level = self.game.character.level
        self.game.character.level_up()
        self.assertEqual(self.game.character.level, current_level + 1)
        self.assertEqual(self.game.character.vitality, 25)  # Vitality should increase by 5
pass 

if __name__ == "__main__":
    # Run the tests
    print("\nRunning Unit Tests...")
    unittest.main(argv=[''], verbosity=2, exit=False)