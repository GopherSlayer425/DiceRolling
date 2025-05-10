import sqlite3

def drop_table():
    """
    Drop the 'rolls' table if it exists.
    This is useful for resetting the database schema during development or testing.
    """
    conn = sqlite3.connect('rolls.db')  # Connect to the SQLite database (or create it if it doesn't exist)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS rolls")  # Drop the 'rolls' table if it exists
    conn.commit()
    conn.close()
    print("Table 'rolls' dropped.")

def init_db(drop_existing=False):
    """
    Initialize the database and create the 'rolls' table.
    
    Parameters:
    - drop_existing (bool): If True, drops the existing 'rolls' table before creating a new one.
    """
    if drop_existing:
        drop_table()  # Remove the existing table before creating a new one

    conn = sqlite3.connect('rolls.db')  # Connect to the SQLite database
    c = conn.cursor()
    
    # Create the 'rolls' table if it does not already exist
    c.execute('''CREATE TABLE IF NOT EXISTS rolls (
        roll_id TEXT PRIMARY KEY,        -- Unique identifier for each roll (e.g., UUID)
        roll_value INTEGER,              -- The value/result of the dice roll
        roll_timestamp TEXT              -- The timestamp of when the roll occurred (ISO format)
    )''')
    
    conn.commit()  # Save changes to the database
    conn.close()   # Close the connection

def save_roll(roll):
    """
    Save a single roll to the database.

    Parameters:
    - roll (dict): A dictionary with keys 'roll_id', 'roll_value', and 'roll_timestamp'.
                   'roll_timestamp' should be a datetime object.
    """
    conn = sqlite3.connect('rolls.db')  # Connect to the SQLite database
    c = conn.cursor()
    
    # Insert the roll into the 'rolls' table
    c.execute("INSERT INTO rolls VALUES (?, ?, ?)",
              (roll['roll_id'], roll['roll_value'], roll['roll_timestamp'].isoformat()))
    
    conn.commit()  # Save the changes
    conn.close()   # Close the connection
