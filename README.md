# U.S. States Guessing Game (Python)

A fun and interactive U.S. States guessing game built using **Python**, **Turtle Graphics**, and **Pandas**.  
The goal is to correctly guess all 50 U.S. states. Each correct guess is displayed at the correct position on the map.

---

## 🎮 How the Game Works

- A blank map of the United States is displayed
- The player types the name of a U.S. state
- If the guess is correct:
  - The state name appears at its correct location on the map
  - The score counter increases
- Duplicate guesses are ignored
- The player can type **`exit`** at any time to quit the game
- On exit, a CSV file containing the **states not guessed** is generated

---

## 🧠 Exit Feature & Learning Mode

If the user types `exit` during the game:

- The game ends gracefully
- A file called `states_to_learn.csv` is created
- This file contains all U.S. states that were **not guessed**
- This allows the player to review and practice missed states later

---

## 📸 Screenshot

![Game Screenshot](assets/screenshot.png)

---

## 🛠 Technologies Used

- Python 3
- Turtle Graphics
- Pandas
- CSV file handling

---

## 📂 Project Files
```text
us-states-game/
├── main.py # Main game logic
├── 50_states.csv # State names and x,y coordinates
├── blank_states_img.gif # U.S. map image
├── assets/
│ └── screenshot.png
├── README.md
└── requirements.txt
```
---

## ▶️ How to Run the Game

1. Clone the repository:
```bash
git clone https://github.com/your-username/us-states-game.git
```
2. Navigate into the project folder:
```bash
cd us-states-game
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the game:
```bash
python main.py
```
---

## 🧠 What I Learned From This Project

- Filtering and extracting single values from Pandas DataFrames
- Preventing duplicate user inputs using Python lists
- Gracefully exiting an interactive Turtle application
- Exporting dynamically generated data to CSV using Pandas
- Structuring a Python project for clarity and reusability

---

🚀 Possible Improvements

- Add a timer or score penalty for wrong guesses
- Save missed states to a CSV file at the end
- Make state name matching more forgiving (partial matches)
- Add an option to quit and show remaining states
