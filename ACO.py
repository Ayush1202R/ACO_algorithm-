import numpy as np
import random


def get_station_labels(n_stations):
    return [chr(65 + i) for i in range(n_stations)]  # A, B, C, ...


def get_input():
    # Get number of stations
    n_stations = int(input("Enter the number of stations: "))

    # Get station labels
    station_labels = get_station_labels(n_stations)

    # Get starting station
    start_label = input(f"Enter the starting station ({', '.join(station_labels)}): ").upper()
    start_pos = station_labels.index(start_label)

    # Get distance matrix from user
    distance_matrix = np.zeros((n_stations, n_stations))
    print(f"Enter the distances between stations:")
    for i in range(n_stations):
        for j in range(n_stations):
            distance = float(input(f"Distance from {station_labels[i]} to {station_labels[j]}: "))
            distance_matrix[i][j] = distance

    return n_stations, distance_matrix, start_pos, station_labels


def calculate_efficiency_matrix(n_stations, distance_matrix, current_station):
    efficiency_matrix = np.zeros((n_stations, n_stations))
    for i in range(n_stations):
        for j in range(n_stations):
            if i != j and distance_matrix[current_station][j] > 0:
                efficiency_matrix[i][j] = 1 / distance_matrix[current_station][j]
    return efficiency_matrix


def initialize_pheromone_matrix(n_stations):
    return np.ones((n_stations, n_stations))


def calculate_probability_matrix(efficiency_matrix, pheromone_matrix, visited_stations):
    n_stations = efficiency_matrix.shape[0]
    actual_probabilities = np.zeros(n_stations)

    for i in range(n_stations):
        if i not in visited_stations:
            actual_probabilities[i] = (efficiency_matrix[0][i] ** 2) * pheromone_matrix[0][i]

    total_probability = np.sum(actual_probabilities)
    normalized_probabilities = (
        actual_probabilities / total_probability if total_probability > 0 else np.zeros(n_stations)
    )

    cumulative_probabilities = np.zeros(n_stations)
    cumulative_probabilities[0] = normalized_probabilities[0]

    for i in range(1, n_stations):
        cumulative_probabilities[i] = cumulative_probabilities[i - 1] + normalized_probabilities[i]

    return actual_probabilities, normalized_probabilities, cumulative_probabilities


def select_next_station(cumulative_probabilities, visited_stations):
    rand_num = random.random()
    for i in range(len(cumulative_probabilities)):
        if i not in visited_stations and rand_num <= cumulative_probabilities[i]:
            return i
    return -1  # Safety fallback


def update_pheromone_matrix_after_ant(pheromone_matrix, visited_stations, pheromone_deposit):
    # Update ONLY the paths visited by the ant
    for i in range(1, len(visited_stations)):
        current_station = visited_stations[i - 1]
        next_station = visited_stations[i]
        pheromone_matrix[current_station][next_station] += pheromone_deposit

    return pheromone_matrix


def ant_travel(n_stations, distance_matrix, pheromone_matrix, start_pos, station_labels):
    current_station = start_pos
    visited_stations = [current_station]
    total_distance = 0

    while len(visited_stations) < n_stations:
        efficiency_matrix = calculate_efficiency_matrix(n_stations, distance_matrix, current_station)
        actual_probabilities, normalized_probabilities, cumulative_probabilities = calculate_probability_matrix(
            efficiency_matrix, pheromone_matrix, visited_stations
        )

        next_station = select_next_station(cumulative_probabilities, visited_stations)
        if next_station == -1:
            break

        total_distance += distance_matrix[current_station][next_station]
        visited_stations.append(next_station)
        current_station = next_station

    # Return to start
    total_distance += distance_matrix[current_station][start_pos]
    visited_stations.append(start_pos)

    # Pheromone formula
    pheromone_deposit = 1 / total_distance

    # Convert indices to labels
    visited_route = [station_labels[station] for station in visited_stations]

    return visited_stations, visited_route, total_distance, pheromone_deposit


def run_ants(n_ants, n_stations, distance_matrix, start_pos, station_labels):
    pheromone_matrix = initialize_pheromone_matrix(n_stations)

    for ant in range(n_ants):
        print(f"\nAnt {ant + 1} is traveling...")

        visited_stations, visited_route, total_distance, pheromone_deposit = ant_travel(
            n_stations, distance_matrix, pheromone_matrix, start_pos, station_labels
        )

        print(f"Ant {ant + 1} followed route: {'-'.join(visited_route)}, "
              f"total distance traveled: {total_distance:.2f}")
        print(f"Pheromone deposited by Ant {ant + 1}: {pheromone_deposit:.4f}")

        # Store pheromone matrix after Ant 1
        pheromone_matrix_ant_1 = np.copy(0.5 * pheromone_matrix)

        # Ant 2 uses Ant 1 matrix, Ant 1 uses its own
        if ant == 1:
            pheromone_matrix = update_pheromone_matrix_after_ant(
                pheromone_matrix, visited_stations, pheromone_deposit
            )
        else:
            pheromone_matrix = update_pheromone_matrix_after_ant(
                pheromone_matrix_ant_1, visited_stations, pheromone_deposit
            )

        print(f"Updated Pheromone Matrix after Ant {ant + 1}:\n", pheromone_matrix)


if __name__ == "__main__":
    n_stations, distance_matrix, start_pos, station_labels = get_input()
    n_ants = 2
    run_ants(n_ants, n_stations, distance_matrix, start_pos, station_labels)
