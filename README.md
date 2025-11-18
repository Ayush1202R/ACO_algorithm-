# 🐜 Ant Colony Optimization (ACO) – Interactive Route Optimization App

This project is a **custom-built Ant Colony Optimization (ACO)** system implemented in **Python** and deployed using **Streamlit**.  
It allows users to simulate how multiple ants explore different paths, apply pheromone updates, and gradually move toward more optimal solutions.

The app supports:
- Custom distance matrix  
- Any number of stations (3–10)  
- Any number of ants (1–20)  
- Custom pheromone update rules  
- Interactive visual output of each ant’s route and pheromone matrix  

---

## 📌 What Problems Does This Solve?

Ant Colony Optimization is used to solve **combinatorial optimization problems**, including:

- Travelling Salesman Problem (TSP)  
- Shortest path or route finding  
- Logistics & delivery optimization  
- Network routing  
- Robot path planning  
- Resource allocation  

---

## ✨ Features of This ACO Implementation

- Interactive UI  
- Supports multiple ants  
- Custom pheromone updating:  
  - Ant 1 → evaporation + deposit  
  - Others → deposit only  
- Probability calculation using:  
  - Efficiency `η = 1/distance`  
  - Pheromone level `τ`  
  - Formula `(η² × τ²)`  
- Prevents revisiting until full tour  
- Pheromone matrices for each ant shown in expanders  

---

## 📦 Requirements

You need Python **3.8+** and these packages:

```
streamlit
numpy
```

Install them using:

```bash
pip install streamlit numpy
```

Or using:

```bash
pip install -r requirements.txt
```

---

## ▶ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/aco.git
cd aco
```

### 2. Install dependencies
```bash
pip install streamlit numpy
```

### 3. Run the Streamlit app
```bash
streamlit run app.py
```

---

## 🧠 How the Algorithm Works

### 1. Efficiency
```
η(i,j) = 1 / distance(i,j)
```

### 2. Probability
```
value(i,j) = (η(i,j)^2) * (τ(i,j)^2)
p(i,j) = value(i,j) / Σ value(i,k)
```

### 3. Pheromone Update

#### Ant 1 (Evaporation + Deposit)
```
τ_new = 0.5 * τ_old
τ_new(u,v) += deposit
```

#### Ant 2, 3, 4… (Deposit Only)
```
τ_new(u,v) = τ_after_ant1(u,v) + deposit
```

Deposit formula:
```
deposit = 1 / total_distance_traveled
```

---

## 📊 Output You Get

For every ant:
- Route taken  
- Total distance  
- Pheromone deposited  
- Updated pheromone matrix  

---

## 🎯 Why This Project Is Useful

This project is perfect for:
- Optimization learning  
- Swarm intelligence demo  
- TSP and routing intuition  
- Multi-ant experimentation  
- Visualization of ACO behavior  

---

## 👨‍💻 Author

**Ayush Radharaman Pandey**

