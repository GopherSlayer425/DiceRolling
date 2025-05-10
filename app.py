from flask import Flask, render_template, jsonify  # Import Flask and helper functions
from roll_logic import roll_die                     # Import custom dice-rolling function
from db import init_db, save_roll                   # Import database initialization and save functions

# Create the Flask application instance
app = Flask(__name__)

# Initialize the database (creates the table if it doesn't exist)
init_db(drop_existing=False)

@app.route('/')
def index():
    """
    Route for the home page.
    Renders an HTML template (index.html).
    """
    return render_template('index.html')

@app.route('/roll')
def roll():
    """
    Route to handle a dice roll request.
    Rolls a 6-sided fair die, saves the result to the database, and returns it as JSON.
    """
    result = roll_die(sides=6, fair=True)  # Call the dice-rolling logic
    save_roll(result)                      # Save the roll result to the database
    return jsonify(result)                 # Return the result as a JSON response

# Run the Flask app only if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)  # Start the development server with debug mode enabled
