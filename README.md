# Elevator System Simulation

This project simulates an elevator scheduling system. It consists of classes to represent elevators and requests, and a function to process the scheduling based on certain conditions.

## 📝 Table of Contents
- [Classes Description](#classes-description)
  - [Elevator](#elevator)
  - [Requests](#requests)
- [Function](#function)
- [Installation](#installation)
- [Usage](#usage)

## 🚀 Classes Description

### Elevator
- `Elevator` class represents an elevator with attributes such as current floor, weight, and direction. It allows adding services and showing details of served floors.

#### Attributes:
- `no`: Elevator number.
- `cur_floor`: Current floor of the elevator.
- `cur_weight`: Current weight inside the elevator.
- `cur_direction`: Current movement direction of the elevator (1 for up, -1 for down, 0 for stationary).
- `dir_floor`: Target floor the elevator is heading towards.

#### Methods:
- `add_service(floor)`: Add a floor to the list of served floors.
- `show_details()`: Return the list of served floors.

### Requests
- `Requests` class represents a request made by users to travel in the elevator.

#### Attributes:
- `persons`: Number of persons making the request.
- `weight`: Total weight of the persons.
- `direction`: Desired direction of travel.
- `floor`: Target floor for the request.

## 🛠 Function

### process_scheduling
- `process_scheduling(elevators, requests)`: Processes all elevator requests. Elevators serve requests based on direction, weight capacity, and floor proximity.

## ⚙️ Installation

To run this simulation, you will need Python installed on your computer. Clone this repository or download the files directly.

```bash
git https://github.com/dhruvpuri-goswami/Elevator-Simulator.git
cd Elevator-Simulator
```

## 🏃 Usage

To run the simulation, execute the script from the command line:

```bash
python pressme.py
```

You will see the output of which floors each elevator served in your terminal.

---

Feel free to explore the code and adapt it to different scenarios or add new functionalities!

