from random import randint

class Die:
    """A class, representing a die."""
    def __init__(self, sides=6):
        """Describing a die with 6 sides."""
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = []
for roll_num in range (10):
    result = d6.roll_die()
    results.append(result)
print ("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided, and show the results of 10 rolls.
d10 = Die(sides=10)

results_2 = []
for roll_num in range (10):
    result = d10.roll_die()
    results_2.append(result)
print("10 rolls of a 10-sided die:")
print(results_2)

# Make a 20-sided, and show the results of 10 rolls.
d10 = Die(sides=20)

results_3 = []
for roll_num in range (10):
    result = d10.roll_die()
    results_3.append(result)
print("10 rolls of a 10-sided die:")
print(results_3)