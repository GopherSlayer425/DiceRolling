from flask import Flask, render_template, jsonify
from roll_logic import roll_die
from db import init_db, save_roll

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll')
def roll():
    result = roll_die(sides=6, fair=True)
    save_roll(result)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)