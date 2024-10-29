# Extra file to run code separately.
# more scenarios and gaming option.

# Settings: initial setting is in a digital arcade game of "wreck it ralph" as the game progress the setting can change into different kinds of arcade games where various characters will be offered and players will select who they will play to win the level. Depending upon the setting this will determine the level's difficulty!!
    # Final boss levels, glitches or bugs will be the unexpected obstacles players occur, and possible crossovers with characters/ abilities/ and settings.

# party: additional characters that can be added/ earned once certain milestone levels are passed:
    # unique characteristics are encouraged for each character.

# For leveling up new characters can be unlocked as well as coins/ or points added to the players characters. Or possiblilty of when they level up special abilities can be unlocked for a limited time for specific characters'.
    ## Possible code class for leveling up: *COPILOT* added characters could be villians.

def level_up(self):
    self.level += 1
    self.strength += 1
    self.dexterity += 1
    self.constitution += 1
    self.vitality += 1
    self.endurance += 1
    self.intelligence += 1
    self.wisdom += 1
    self.knowledge += 1
    self.willpower += 1
    self.spirit += 1
    self.capacity += 1
    print(f"{self.name} leveled up to level {self.level}!")

## Ralph and Fleix would get plugged in here:
    ralph = Character("Ralph", 10, 5, 8, 12, 7, 4, 3, 6, 9, 5, 10)
    ralph.level_up()

## Possible code for un-eventful scenarios:
# import random

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

### Scenario example:
event = Event(
   "A glitch in the system causes chaos!",
    [
        {"description": "Use Dexterity to navigate through.", "outcome": {"success": "You navigated successfully!", "failure": "You got hurt!", "experience": 10, "damage": 2}},
        {"description": "Use Intelligence to stabilize the system.", "outcome": {"success": "You stabilized the system!", "failure": "It didn't work!", "experience": 15, "damage": 3}},
    ]
)

event.trigger_event(Ralph)

def game_loop():
    ralph = Character("Ralph", 10, 5, 8, 12, 7, 4, 3, 6, 9, 5, 10)
    events = [
        Event(
            "A glitch in the system causes chaos!",
            [
                {"description": "Use Dexterity to navigate through.", "outcome": {"success": "You navigated successfully!", "failure": "You got hurt!", "experience": 10, "damage": 2}},
                {"description": "Use Intelligence to stabilize the system.", "outcome": {"success": "You stabilized the system!", "failure": "It didn't work!", "experience": 15, "damage": 3}},
            ]
        )
    ]

    while ralph.vitality > 0:
        event = random.choice(events)
        event.trigger_event(ralph)
        if ralph.experience >= 20:
            ralph.level_up()
            ralph.experience = 0

    print("Game Over")

game_loop()

### LEVEL 6 COPILOT CODE ** Puzzle **
#import random
#import time

class GearPuzzle:
   def __init__(self):
        self.gear_sequence = [random.randint(1, 5) for _ in range(5)]  # Random gear sequence
        self.player_sequence = [0] * 5  # Player's current sequence

def display_puzzle(self):
    print("Current Gear Sequence: ", self.player_sequence)
    
def input_move(self, index, value):
    if 0 <= index < len(self.gear_sequence):
        self.player_sequence[index] = value
    
def check_solution(self):
    return self.player_sequence == self.gear_sequence

class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def attack(self):
        print(f"{self.name} is attacking!")
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

def main():
    puzzle = GearPuzzle()
    enemies = [Enemy("Minion", 10) for _ in range(5)]  # Initial set of enemies

    while not puzzle.check_solution():
        puzzle.display_puzzle()
        
        # Felix's turn to make a move
        index = int(input("Enter gear index (0-4): "))
        value = int(input("Enter gear value (1-5): "))
        puzzle.input_move(index, value)

        # Ralph's turn to defend
        for enemy in enemies:
            if enemy.health > 0:
                enemy.attack()
                time.sleep(1)  # Simulate time taken for Ralph to react
                enemy.take_damage(10)  # Ralph's attack damage
                
        print("\n")

    print("Puzzle Solved! Door Unlocked.")

if __name__ == "__main__":
    main()

# Extra file to run code separately. 
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        print(f"Added {quantity} {item_name}(s) to your inventory.")

    def use_item(self, item_name, character):
        if item_name in self.items and self.items[item_name] > 0:
            print(f"{character.name} uses {item_name}.")
            # Define item effects, e.g., healing:
            if item_name == "Health Potion":
                character.vitality += 10
                print(f"{character.name} regained 10 vitality points!")
            self.items[item_name] -= 1
        else:
            print(f"No {item_name} left in inventory.")

inventory = Inventory()
inventory.add_item("Health Potion", 3)
inventory.use_item("Health Potion", ralph)