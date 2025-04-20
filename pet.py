

class Pet:

    def __init__(self, name: str, hunger: int = 0, energy: int = 10, happiness: int = 10):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.tricks = []

    def eat(self):
        """ reduces hunger by 3 points (but not below 0), and increases happiness by 1."""
        self.attr_op(self, "hunger", "-", 3)
        self.attr_op(self, "happiness", "+", 1)

    def sleep(self):
        """ increases energy by 5 points (but not above 10)."""
        self.attr_op(self, "energy", "+", 5)

    def play(self):
        """decreases energy by 2, increases happiness by 2, and increases hunger by 1."""
        self.attr_op(self, "energy", "-", 2)
        self.attr_op(self, "happiness", "+", 2)
        self.attr_op(self, "hunger", "+", 1)

    def get_status(self):
        """ prints the current state of the pet"""
        print(f"Status\nHappiness: {self.happiness}\nHunger: {self.hunger}\nEnergy: {self.energy}")

    def train(self, trick: str):
        """ that teaches your pet a new trick and stores it in a list"""
        self.tricks.append(trick)

    def show_tricks(self):
        """that prints all learned tricks."""
        print(self.tricks)

    @staticmethod
    def attr_op(pet, attr: str, op: str, val: int):
        if hasattr(pet, attr):
            match op:
                case "+":
                    if (getattr(pet, attr) + val) <= 10:
                        setattr(pet, attr, getattr(pet, attr)+val)
                    elif (getattr(pet, attr) + 1) <= 10:
                        setattr(pet, attr, getattr(pet, attr) + 1)
                    else:
                        print(f"{pet.name} {attr} at Max")
                case "-":
                    if (getattr(pet, attr) - val) > 0:
                        setattr(pet, attr, getattr(pet, attr)-val)
                    elif (getattr(pet, attr) - 1) > 0:
                        setattr(pet, attr, getattr(pet, attr) - 1)
                    else:
                        print(f"{pet.name} {attr} at Min")
                case _:
                    raise ValueError("Unknown operator")
        else:
            raise AttributeError(f"{pet} has no attribute named {attr}")   
