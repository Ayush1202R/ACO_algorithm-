# 🐜 Ant Colony Optimization (ACO) – Interactive Route Optimization App

This project is a **custom-built Ant Colony Optimization (ACO)** system implemented in **Python** and deployed using **Streamlit**.  
It allows users to simulate how multiple ants explore different paths, apply pheromone updates, and gradually move toward more optimal solutions.

The app supports:
- Custom distance matrix  
- Any number of stations (3–10)  
- Any number of ants (1–20)  
- Custom pheromone update rules  
- Interactive visual output of each ant’s route and pheromone matrix  

This makes the project useful for learning, teaching, and experimenting with optimization techniques inspired by real ant behavior.

---

## 📌 What Problems Does This Solve?

Ant Colony Optimization is widely used to solve **combinatorial optimization problems**, especially those involving path planning or route selection.

This project can be used to solve and visualize:
- **Travelling Salesman Problem (TSP)**  
- **Shortest route finding**  
- **Logistics & delivery route optimization**  
- **Network routing**  
- **Robot path planning**  
- **Resource allocation problems**  

The model simulates how ants search for paths, update pheromones, and collectively converge toward the best route.

---

## ✨ Features of This ACO Implementation

- Interactive UI: input stations, distances, and number of ants  
- Multi-ant support (each ant improves the pheromone map)  
- Custom pheromone update rules:
  - Ant 1 → **evaporation + deposit**
  - Ant 2, 3, 4… → **deposit only**
- Dynamic probability selection using:
  - Efficiency `η = 1 / distance`
  - Pheromone intensity `τ`
  - Probability formula `(η² × τ²)`
- No revisit until all stations are covered  
- Pheromone matrices shown after each ant  
- Easy visualization through Streamlit expanders  
- Great for teaching optimization algorithms  

---

## 📦 Requirements

You need Python **3.8+** and these packages:

streamlit
numpy


Install them using:

```bash
pip install streamlit numpy


or using:

pip install -r requirements.txt


▶ How to Run the Project
1. Clone the repository
git clone https://github.com/your-username/aco.git
cd aco

2. Install dependencies
pip install streamlit numpy

3. Run the Streamlit application
streamlit run app.py



🧠 How the Algorithm Works
1. Efficiency

Shorter routes are more attractive:

η(i,j) = 1 / distance(i,j)

2. Probability

Ants choose their next station based on:

value(i,j) = (η(i,j)^2) * (τ(i,j)^2)
p(i,j) = value(i,j) / Σ value(i,k)

3. Pheromone Update
Ant 1 (Evaporation + Deposit)
τ_new = 0.5 * τ_old
τ_new(u,v) += deposit

Ant 2, 3, 4… (Deposit Only)
τ_new(u,v) = τ_after_ant1(u,v) + deposit


where:

deposit = 1 / total_distance_traveled


This allows the pheromone map to evolve over multiple ants, gradually improving the route quality.



📊 Output You Get

For every ant:

Route taken (station labels)

Total distance

Pheromone deposited

Updated pheromone matrix
All neatly displayed using Streamlit expanders.


🎯 Why This Project Is Useful

This project is perfect for:

Students learning optimization

Demonstrating swarm intelligence

Building intuition for probabilistic search

Understanding TSP and route optimization

Experimenting with different numbers of ants and distances

It provides visual clarity and a hands-on understanding of how ACO works internally.

👨‍💻 Author

Ayush Radharaman Pandey
