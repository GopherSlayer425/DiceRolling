import random
from datetime import datetime, UTC  # Import datetime with UTC timezone
import uuid                         # Import for generating unique roll IDs

def roll_die(sides=6, fair=True):
    """
    Simulate rolling a die and return the result with metadata.

    Parameters:
    - sides (int): Number of sides on the die (default is 6).
    - fair (bool): Whether the die is fair (equal probability). If False, the die is weighted.

    Returns:
    - dict: A dictionary containing:
        - 'roll_id': A unique identifier for this roll (UUID string).
        - 'roll_value': The integer result of the die roll.
        - 'roll_timestamp': The current UTC time when the roll was made.
    """
    
    if not fair:
        # Create a weighted die where the number 1 is more likely (30%)
        # and all other outcomes share the remaining 70% evenly.
        weights = [0.3] + [0.14] * (sides - 1)
        value = random.choices(range(1, sides + 1), weights=weights)[0]
    else:
        # Use a fair die: all sides have equal chance
        value = random.randint(1, sides)

    return {
        'roll_id': str(uuid.uuid4()),          # Generate a unique ID for the roll
        'roll_value': value,                   # The result of the die roll
        'roll_timestamp': datetime.now(UTC)    # Record the time of the roll in UTC
    }
