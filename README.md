# 🐜 Ant Colony Optimization (ACO) – Custom Route Optimization Model

A fully customized Ant Colony Optimization system built with Python and Streamlit.  
This project simulates how ants find optimal paths using pheromone trails and probabilistic decision-making.  
Includes custom pheromone update logic, dynamic probability rules, and an interactive Streamlit UI.

---

## 🌐 Live Demo (Optional)
If deployed on Streamlit Cloud, add the link here:
👉 **[Live ACO Model](#)**

---

## 📌 Overview
This project demonstrates how autonomous agents (ants) explore routes and optimize path selection using:

- Efficiency-based decisions  
- Pheromone reinforcement  
- Evaporation  
- Cumulative probability selection  

The system uses **two ants**, each updating the pheromone matrix differently to simulate learning over time.

---

## ✨ Key Features
- Fully custom ACO algorithm  
- Dynamic probability calculation (`η² × τ²`)  
- Pheromone evaporation + deposition  
- Ant-specific pheromone update rules  
- No revisits — each ant visits all stations before returning  
- Clean Streamlit UI  
- Expanders/toggles for matrices & labels  
- Supports 3–10 stations  
- Interactive distance matrix input  

---

## 🧠 Algorithm Workflow
- Generate station labels (A, B, C, …)  
- User inputs distance matrix  
- Ant 1 travels all stations → applies **evaporation + deposit**  
- Pheromone matrix updated  
- Ant 2 runs on the updated matrix → **deposit only**  
- Routes, distances, иpheromone matrices displayed  

---

## 📊 Input Parameters
- Number of stations  
- Starting station  
- Distance matrix (NxN)  
- Auto-assigned station labels (A, B, C…)  

---

## 🛠 Tech Stack
- **Python**  
- **NumPy**  
- **Streamlit**  
- **Random module**  

