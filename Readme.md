# 🚦 Real-Time Traffic Analysis using Dijkstra's Algorithm

## Project Overview
This project is developed as part of the **Design and Analysis of Algorithms (DAA)** course in **MCA (Cloud Computing & DevOps)**.  
It demonstrates how **Dijkstra’s Algorithm** can be applied to analyze **real-time traffic data** and determine the **shortest path** between locations.

The system takes city routes and traffic conditions as input and visualizes the shortest path for vehicles using a simple and elegant **Python web interface**.

---

## Objectives
- Implement **Dijkstra’s Algorithm** efficiently.
- Demonstrate its real-world application in **traffic route optimization**.
- Build a clean **web-based interface** using Python (Flask).
- Show how algorithmic concepts help in **smart city traffic systems**.

---

## Tech Stack
| Component | Technology |
|------------|-------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python (Flask Framework) |
| **Algorithm** | Dijkstra’s Algorithm |
| **Visualization** | Graph plotting using `networkx` and `matplotlib` |

---

## Project Structure
---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
2.Create a Virtual Environment (optional but recommended)

python -m venv venv
# Windows
venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Run the App

python app.py

Then open your browser and visit: http://127.0.0.1:5000/


---
 How It Works

1. User enters Start Node and End Node (A–E).


2. Flask calls NetworkX to compute shortest path using Dijkstra’s Algorithm.


3. Matplotlib dynamically plots the graph:

🔵 Blue nodes → All cities

🔴 Red edges → Shortest path

🟠 Orange nodes → Path highlights

4. Result + total distance displayed on screen.


5. Graph image updates instantly (no browser cache).
