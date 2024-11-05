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

    def __init__(self):
        self.ralph = Character("Ralph", vitality=20)
        self.felix = Character("Felix", vitality=15)  # Add Felix here
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
    
    def start_level_7(self):
        print("Welcome to Level 7: Healing Infected Characters")
        monsters_defeated = 0
        infected_characters = 3
        while infected_characters > 0:
            action = input("Press 'f' to have Felix heal or 'r' for Ralph to fight monsters: ").lower()
            if action == 'f':
                infected_characters -= 1
                print(f"Felix healed an infected character! Remaining: {infected_characters}")
                self.felix.gain_powerup()
            elif action == 'r':
                monsters_defeated += 1
                print(f"Ralph is fighting monsters! Monsters defeated: {monsters_defeated}")
                self.ralph.gain_powerup()
            else:
                print("Invalid input! Please press 'f' to heal or 'r' to fight.")

    def start_level_8(self):
        print("Welcome to Level 8: Combat and Repairs")
        repairs_needed = 3
        waves_of_monsters = 3
        while repairs_needed > 0 or waves_of_monsters > 0:
            action = input("Press 'f' for Felix to repair or 'r' for Ralph to fight waves: ").lower()
            if action == 'f' and repairs_needed > 0:
                repairs_needed -= 1
                print(f"Felix repaired a corrupted area! Remaining repairs: {repairs_needed}")
                self.felix.gain_powerup()
            elif action == 'r' and waves_of_monsters > 0:
                waves_of_monsters -= 1
                print(f"Ralph defeated a wave of monsters! Waves remaining: {waves_of_monsters}")
                self.ralph.gain_powerup()
            else:
                print("Invalid input or no more actions left for this character.")

    def start_level_9(self):
        print("Welcome to Level 9: Combat with Mini Bosses and Puzzle Solving")
        bosses_remaining = 3
        locked_doors = 2
        while bosses_remaining > 0 or locked_doors > 0:
            action = input("Press 'r' for Ralph to fight mini bosses or 'f' for Felix to solve puzzles: ").lower()
            if action == 'r' and bosses_remaining > 0:
                bosses_remaining -= 1
                print(f"Ralph defeated a mini boss! Bosses remaining: {bosses_remaining}")
                self.ralph.level_up()  # Double reward
            elif action == 'f' and locked_doors > 0:
                locked_doors -= 1
                print(f"Felix solved a puzzle and unlocked a door! Locked doors remaining: {locked_doors}")
                self.felix.gain_powerup()
            else:
                print("Invalid input or no more actions left for this character.")

    import time
    import random

    def start_level_10(self):
        print("Welcome to Level 10: The Final Boss - The Source of the Virus")
        
        # Phase 1: Ralph breaks the shield while dodging attacks
        print("\nPhase 1: Ralph must break the shield while dodging power attacks.")
        shield_strength = 3  # Number of obstacles to break
        while shield_strength > 0:
            action = input("Press 'b' to have Ralph break the shield or 'd' to dodge an attack: ").lower()
            if action == 'b':
                self.ralph.break_obstacle()
                shield_strength -= 1
                print(f"Shield strength remaining: {shield_strength}")
            elif action == 'd':
                print("Ralph dodged an attack!")
            else:
                print("Invalid input! Press 'b' to break the shield or 'd' to dodge.")
        
        print("Phase 1 Complete! Ralph broke the shield.")
        
        # Phase 2: Felix solves a complex problem while avoiding virus-infected minions (Timed)
        print("\nPhase 2: Felix is solving a complex problem while avoiding the boss's minions.")
        minions_to_avoid = 5
        start_time = time.time()
        while minions_to_avoid > 0:
            action = input("Press 's' to solve the puzzle or 'd' to dodge a minion: ").lower()
            elapsed_time = time.time() - start_time
            if elapsed_time > 30:
                print("Time’s up! The boss overwhelmed Felix!")
                return  # End game if time runs out
            if action == 's':
                minions_to_avoid -= 1
                print(f"Puzzle progress made. Remaining minions to avoid: {minions_to_avoid}")
            elif action == 'd':
                print("Felix dodged a minion attack!")
            else:
                print("Invalid input! Press 's' to solve or 'd' to dodge.")
        
        print("Phase 2 Complete! Felix solved the puzzle and avoided the minions.")
        
        # Phase 3: Alternating between Ralph and Felix to defeat the boss (Timed and Reflex-based)
        print("\nPhase 3: Alternating characters to combat the virus.")
        rounds_remaining = 5
        while rounds_remaining > 0:
            current_character = "Ralph" if rounds_remaining % 2 != 0 else "Felix"
            start_phase_time = time.time()
            print(f"\n{current_character}'s turn!")
            if current_character == "Ralph":
                input("Press 'b' for Ralph to attack the virus! ")
            else:
                input("Press 'h' for Felix to deactivate a virus code! ")
            
            # Check timing for reflex-based gameplay
            elapsed_phase_time = time.time() - start_phase_time
            if elapsed_phase_time <= 3:
                print(f"{current_character} succeeded with precise timing!")
                rounds_remaining -= 1
            else:
                print(f"{current_character} was too slow! Try again.")
            
        print("\nPhase 3 Complete! The virus has been defeated. Congratulations, you’ve completed the game!")

    

    def run(self):
        levels = [self.start_level_1, self.start_level_2, self.start_level_3, self.start_level_4, self.start_level_5, self.start_level_6, self.start_level_7, self.start_level_8, self.start_level_9, self.start_level_10]
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

# -- Unit Test Code --
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

print("\nRunning Unit Tests...")
unittest.main(argv=[''], verbosity=2, exit=False)