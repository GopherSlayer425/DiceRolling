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

## Copyright Information

Copyright [2025] [Christopher Barnett]

This code is provided for educational and non-commercial use only. You are welcome to read, learn from, and adapt this code for personal or classroom projects.

You may not use this code, in whole or in part, for any commercial purpose without my explicit written permission.

If you wish to contribute improvements or fixes, please open a pull request or contact me directly. By contributing, you agree that your contributions will also be shared under these same terms.

For any questions or requests for commercial use, please contact: [barnettcp@gmail.com]

## Contributor License Agreement
By submitting a contribution (e.g., via a pull request), you agree that your contribution will be licensed under the same terms as the main project: for educational and non-commercial use only, unless otherwise specified.

You retain copyright to your contribution, but you grant Christopher Barnett and all users of this project the right to use, modify, and distribute your contribution under these terms.

Please note: This project may receive donations or other support to help cover costs and development time. By contributing, you acknowledge and agree that donations may benefit the project owner and do not entitle contributors to compensation.


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


