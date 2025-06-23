# 🚀 Starbound: Journey to Sector 9-Delta (Python Terminal Game)

## 🎯 Project Overview

**Starbound** is a grid-based terminal game where players pilot a spaceship from Kepler-452b across a space sector filled with hazards, resources, and unknown threats. The goal is to safely reach **Sector 9-Delta** before running out of fuel or getting destroyed.

Written in **Python**, the game demonstrates **object-oriented programming**, interactive I/O, and map-based exploration logic. It simulates survival mechanics in a simple, engaging format suitable for learning game loops and class interactions.

---

## 🌌 Game Mechanics

- Control a ship (`@`) navigating a 2D space map
- Interact with map entities:
  - `.` = Asteroid (impassable)
  - `E` = Enemy (damages ship)
  - `M` = Mineral (collect and use to repair)
  - `R` = Repair Station (heals if you have minerals)
  - `X` = Destination
- Game ends with:
  - ✅ Victory: reaching destination
  - ❌ Defeat: running out of fuel or health

---

## 🛠️ Core Features

- Dynamic map creation and population
- Ship system with:
  - Position tracking
  - Fuel and health management
  - Mineral collection and consumption
- Real-time status updates
- Victory/failure condition checking
- Modular structure using multiple `.py` files

---

## 🧩 Key Modules

| File | Description |
|------|-------------|
| `game.py` | Main gameplay loop, command input, and state control |
| `ship.py` | Ship class with attributes and interaction methods |
| `space_map.py` | Map creation, entity placement, and rendering |

---

## 🕹️ Gameplay Commands

- `n`, `s`, `e`, `w`: Move in a direction
- `map`: View current space map
- `status`: Show ship's current stats
- `q`: Quit (self-destruct)

---

## ✅ How to Run

1. Ensure all three files are in the same directory:
   - `game.py`
   - `ship.py`
   - `space_map.py`

2. Open a terminal and run:
3. Follow the prompts to:
  - Configure map size
  - Set ship name and fuel
  - Place destination and hazards
  - Start your mission!

## Example

>>> STARTING ROUTE: Kepler-452b -> Sector 9-Delta
Enter size of map (n >= 2): 4
4 x 4 map initialised.

>> CONFIGURING SHIP SYSTEMS
Enter ship name: Odyssey
Enter fuel (1-99): 15

>>> EXECUTING LIFTOFF: EXITING Kepler-452b's ORBIT

Enter (n,e,s,w | map | status): s
+1 mineral! Minerals: 1
Enter (n,e,s,w | map | status): e
Ship repaired! Health: 3/3
...
>>> MISSION COMPLETED

```bash
python3 game.py
