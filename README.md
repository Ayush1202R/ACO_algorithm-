# 🐜 Ant Colony Optimization (ACO)

[![GitHub license](https://img.shields.io/github/license/Ayush1202R/ACO_algorithm-?style=flat-square)](https://github.com/Ayush1202R/ACO_algorithm-/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Ayush1202R/ACO_algorithm-?style=flat-square)](https://github.com/Ayush1202R/ACO_algorithm-/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/Ayush1202R/ACO_algorithm-/pulls)
[![Open in Streamlit](https://img.shields.io/badge/Run%20App-Streamlit-red?logo=streamlit&style=flat-square)](https://ant-colony-optimization.streamlit.app/)

An interactive **Ant Colony Optimization (ACO)** routing simulator implemented in Python and deployed using Streamlit. 

This simulator lets users visualize how multiple agents (ants) explore combinations of paths, dynamically deposit pheromones, and execute evaporation cycles to converge on optimal paths for TSP (Travelling Salesman Problem) network configurations.

---

## 🌟 Key Features

* **Custom Routing Matrix**: Input interactive distance matrices for $3$ to $10$ node stations.
* **Swarm Control Dashboard**: Configure the number of ants ($1$ to $20$), pheromone weights, and evaporation coefficients.
* **Ant-Specific Pheromone Rules**:
  - **Ant 1**: Triggers standard evaporation & deposit: $\tau_{\text{new}} = 0.5 \cdot \tau_{\text{old}} + \Delta\tau$.
  - **Subsequent Ants**: Triggers deposit-only updates on top of Ant 1's grid.
* **Granular Trace Logs**: Expansions showing the custom route, distance metrics, and updated pheromone matrices per ant.

---

## ⚙️ Mathematical Overview

The choice probability of an ant going from node $i$ to node $j$ is computed as:
$$P_{i,j} = \frac{(\eta_{i,j})^\beta \cdot (\tau_{i,j})^\alpha}{\sum_{k \in \text{allowed}} (\eta_{i,k})^\beta \cdot (\tau_{i,k})^\alpha}$$

Where:
- $\eta_{i,j} = \frac{1}{\text{Distance}_{i,j}}$ is the heuristic visibility/efficiency.
- $\tau_{i,j}$ represents the pheromone density level on edge $(i, j)$.
- $\alpha, \beta$ are user-controlled weight exponents (set to $2$ in this model).

The pheromone deposit quantity is inversely proportional to the path distance:
$$\Delta\tau = \frac{1}{\text{Total Distance Traveled}}$$

---

## 📂 Project Structure

```text
ACO_algorithm-/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── ACO.py                  # Core Ant Colony Optimization implementation
├── CONTRIBUTING.md
├── LICENSE
├── README.md               # Documentation
├── app.py                  # Streamlit entrypoint script
└── requirements.txt        # Dependencies
```

---

## 🛠️ Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Ayush1202R/ACO_algorithm-.git
cd ACO_algorithm-
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app
```bash
streamlit run app.py
```
