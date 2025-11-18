import streamlit as st
import numpy as np
import random


# ----------------------------
# ACO Helper Functions
# ----------------------------

def get_station_labels(n):
    return [chr(65 + i) for i in range(n)]


def initialize_pheromone_matrix(n):
    return np.ones((n, n))


def calculate_efficiency(current, distance_matrix):
    n = len(distance_matrix)
    eff = np.zeros(n)
    for j in range(n):
        if j != current and distance_matrix[current][j] > 0:
            eff[j] = 1 / distance_matrix[current][j]
    return eff


def calculate_probability(current, pheromone_matrix, distance_matrix, visited):
    n = len(distance_matrix)
    eff = calculate_efficiency(current, distance_matrix)
    actual = np.zeros(n)

    for j in range(n):
        if j not in visited:
            actual[j] = (eff[j] ** 2) * (pheromone_matrix[current][j] ** 2)

    total = np.sum(actual)
    normalized = actual / total if total > 0 else actual
    cumulative = np.cumsum(normalized)

    return normalized, cumulative


def select_next_station(cumulative, visited):
    r = random.random()
    for i in range(len(cumulative)):
        if i not in visited and r <= cumulative[i]:
            return i
    return -1


def ant_travel(n, distance_matrix, pheromone_matrix, start_pos, labels):
    current = start_pos
    visited = [current]
    total_distance = 0

    while len(visited) < n:
        _, cumulative = calculate_probability(current, pheromone_matrix, distance_matrix, visited)
        next_station = select_next_station(cumulative, visited)

        if next_station == -1:
            break

        total_distance += distance_matrix[current][next_station]
        visited.append(next_station)
        current = next_station

    # return to start
    total_distance += distance_matrix[current][start_pos]
    visited.append(start_pos)

    deposit = 1 / total_distance
    route = [labels[s] for s in visited]

    return visited, route, total_distance, deposit


def update_pheromone(pheromone_matrix, visited, deposit, evaporate=False):
    """
    evaporate=True → evaporation (for ant 1)
    evaporate=False → no evaporation (for subsequent ants)
    """
    if evaporate:
        pheromone_matrix = 0.5 * pheromone_matrix  # evaporation

    new_matrix = np.copy(pheromone_matrix)
    for i in range(1, len(visited)):
        a, b = visited[i - 1], visited[i]
        new_matrix[a][b] += deposit

    return new_matrix


# ----------------------------
# STREAMLIT APP
# ----------------------------

st.title("🐜 Ant Colony Optimization (Custom ACO)")

n = st.number_input("Enter number of stations", min_value=3, max_value=10, step=1)

if n:
    labels = get_station_labels(n)

    with st.expander("🔤 Show Station Labels"):
        st.write(labels)

    start_label = st.selectbox("Select starting station", labels)
    start_pos = labels.index(start_label)

    with st.expander("📘 Enter Distance Matrix"):
        distance_matrix = np.zeros((n, n))
        cols = st.columns(n)
        for i in range(n):
            for j in range(n):
                distance_matrix[i][j] = cols[j].number_input(
                    f"{labels[i]} → {labels[j]}", min_value=0.0, value=0.0
                )

    # NEW: USER CAN ENTER NUMBER OF ANTS
    num_ants = st.number_input("Enter number of ants", min_value=1, max_value=20, step=1)

    if st.button("Run ACO"):
        st.header("🚀 Running ACO")

        pheromone_matrix = initialize_pheromone_matrix(n)

        for ant in range(num_ants):
            st.subheader(f"🐜 Ant {ant + 1}")

            visited, route, dist, deposit = ant_travel(
                n, distance_matrix, pheromone_matrix, start_pos, labels
            )

            st.write("Route:", " → ".join(route))
            st.write("Total Distance:", dist)
            st.write("Pheromone Deposited:", deposit)

            # Ant 1 → evaporation + deposit
            # Ant 2,3,4... → only deposit
            if ant == 0:
                pheromone_matrix = update_pheromone(pheromone_matrix, visited, deposit, evaporate=True)
            else:
                pheromone_matrix = update_pheromone(pheromone_matrix, visited, deposit, evaporate=False)

            with st.expander(f"📊 Pheromone Matrix After Ant {ant + 1}"):
                st.write(pheromone_matrix)
