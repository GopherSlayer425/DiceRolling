import random
from datetime import datetime, UTC
import uuid

def roll_die(sides=6, fair=True):
    if not fair:
        weights = [0.3] + [0.14] * (sides - 1)
        value = random.choices(range(1, sides + 1), weights=weights)[0]
    else:
        value = random.randint(1, sides)

    return {
        'roll_id': str(uuid.uuid4()),
        'roll_value': value,
        'roll_timestamp': datetime.now(UTC)
    }


