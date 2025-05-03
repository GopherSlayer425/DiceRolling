# Dice Stats Web App

A Python-based web app to simulate rolling dice, store roll data (value, timestamp, ID), and visualize basic statistics like histograms. Initially supports a fair 6-sided die and can be extended to support multiple dice, unfair probabilities, and educational statistics.

## Features

* Roll a fair 6-sided die with animation
* Store each roll with a unique ID and timestamp
* Visualize dice roll history using a histogram
* Flask backend using Python
* Simple HTML/CSS frontend

## Future Enhancements

* Support for multiple and custom-sided dice
* Unfair dice with custom probability weights
* Roll history persistence in database
* Educational statistics (mean, mode, standard deviation, etc.)

## Tech Stack

* Python 3.11+
* Flask
* SQLite (for initial data storage)
* Matplotlib (for histogram rendering)
* HTML5 / CSS3 / JavaScript (for frontend & animation)

## File Structure

```
dice_stats_app/
├── app.py                # Main Flask app
├── roll_logic.py         # Dice roll function logic
├── db.py                 # SQLite DB setup and interaction
├── static/
│   └── style.css         # Styles for frontend
├── templates/
│   └── index.html        # Main frontend UI
├── rolls.db              # SQLite DB file (created at runtime)
├── README.md             # Project overview
└── requirements.txt      # Python dependencies
```

## Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/dice_stats_app.git
cd dice_stats_app
```

2. **Create and Activate Virtual Environment (optional)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the App**

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.


