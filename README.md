# 🚀 Starbound: Journey to Sector 9-Delta

**Starbound** is a terminal-based space exploration game written in Python. Players navigate a spaceship from Kepler-452b across a hostile and resource-scarce space grid to reach the destination at **Sector 9-Delta**. 
Strategize your movement, manage fuel, avoid hazards, and interact with the environment to survive and succeed.

---

## 🧠 Game Concept

You are the pilot of a spacecraft tasked with a dangerous mission: reach a distant destination through space filled with asteroids, enemies, and unexpected events. Your success depends on:
- Careful fuel management
- Avoiding or surviving enemy encounters
- Mining and using minerals
- Repairing your ship at the right time
- Reaching the final destination before running out of resources

---

## 🗂️ Project Structure

project/
│
├── game.py # Main program loop and user interaction
├── ship.py # Defines the Ship class and all ship-related functionality
└── space_map.py # Map creation, display, and hazard population


---

## 🕹️ How to Play

1. Run the game with:

```bash
python3 game.py
Configure your space map (choose size n >= 2).
Set your ship's name and initial fuel (1–99 units).
Place the destination and other map entities:
. : Asteroid (blocked path)
E : Enemy (damages health)
M : Mineral (collectible resource)
R : Repair station (heals if you have minerals)
X : Final destination
Enter commands to move or check status:
n / s / e / w → Move ship (if within bounds)
map → View current map
status → Show ship stats
q → Self-destruct and quit
Win if you reach the destination. Lose if fuel or health reaches zero.

## 📦 Features

Customizable map size and content
Dynamic ship status tracking (fuel, health, minerals)
Interaction with various space entities
Game-over logic based on health, fuel, and mission status
Simple and modular design, easy to expand

## ✅ Requirements

Python 3.7+
Terminal/command-line access
No third-party libraries are required.

## ✨ Sample Output

>>> STARTING ROUTE: Kepler-452b -> Sector 9-Delta
Enter size of map (n >= 2): 5
5 x 5 map initialised.

>> CONFIGURING SHIP SYSTEMS
Enter ship name: Voyager
Enter fuel (1-99): 20

Status Report - Voyager
-------------------------
Coordinates    : (0, 0)
Fuel Level     : 20 units
Health         : 3
Minerals       : 00
-------------------------

>>> EXECUTING LIFTOFF: EXITING Kepler-452b's ORBIT
>>> AWAITING COMMANDS

Enter (n,e,s,w | map | status): e
## 📌 Notes

Map coordinates follow [y][x] indexing.
Ship always starts at (0, 0).
Be careful with enemy encounters and fuel usage!
