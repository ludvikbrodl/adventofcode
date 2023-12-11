from pathlib import Path
import pprint
import heapq

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"
INPUT_EXAMPLE_EZI = "input_example_ezi.txt"
INPUT_EXAMPLE_MEDIUM = "input_example_medium.txt"

pp = pprint.PrettyPrinter(indent=4)


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").readlines()]


def get_data(path, inc_cost=2) -> list[str]:
    # Create a matrix by mapping '.' to 0 and '#' to 1
    matrix = [[0 if char == "." else 1 for char in line] for line in get_lines(path)]

    # Extract coordinates with "#" to a list
    coordinates_list = []
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == 1:
                coordinates_list.append((i, j))

    # Create an expanded matrix
    expanded_matrix = []
    for i in range(len(matrix)):
        if any(matrix[i]):
            expanded_matrix.append(matrix[i])
        else:
            expanded_matrix.extend([matrix[i], matrix[i]])
    graph = Graph(matrix)
    graph.generate_graph(inc_cost)
    return graph


class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.graph = {}

    def add_edge(self, node1, node2, cost, direction):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = {"cost": cost, "direction": direction}

    def get_neighbors(self, node):
        x, y = node
        neighbors = []
        directions = [
            (0, 1, "horizontal"),
            (1, 0, "vertical"),
            (0, -1, "horizontal"),
            (-1, 0, "vertical"),
        ]

        for dx, dy, direction in directions:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < self.rows and 0 <= new_y < self.cols:
                neighbors.append(((new_x, new_y), direction))

        return neighbors

    def generate_graph(self, inc_cost=2):
        for i in range(self.rows):
            for j in range(self.cols):
                current_node = (i, j)
                neighbors = self.get_neighbors(current_node)

                for neighbor, direction in neighbors:
                    cost = 1  # Default cost
                    if direction == "horizontal" and not any(
                        self.matrix[row][j] == 1 for row in range(self.rows)
                    ):
                        cost = (
                            inc_cost  # Double cost for horizontal traversal without '#'
                        )
                    elif direction == "vertical" and not any(
                        self.matrix[i][col] == 1 for col in range(self.cols)
                    ):
                        cost = (
                            inc_cost  # Double cost for vertical traversal without '#'
                        )
                    self.add_edge(current_node, neighbor, cost, direction)

    def dijkstra(self, start):
        distances = {node: float("infinity") for node in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            if current_node not in self.graph:
                continue

            for neighbor, edge_info in self.graph[current_node].items():
                cost = edge_info["cost"]
                distance = current_distance + cost
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def shortest_paths(self):
        all_shortest_paths = {}
        nodes_with_hash = [
            (i, j)
            for i in range(self.rows)
            for j in range(self.cols)
            if self.matrix[i][j] == 1
        ]

        for start_node in nodes_with_hash:
            shortest_paths = {}
            distances = self.dijkstra(start_node)
            for end_node, distance in distances.items():
                if (
                    distance != float("infinity")
                    and self.matrix[end_node[0]][end_node[1]] == 1
                ):
                    shortest_paths[end_node] = distance
            all_shortest_paths[start_node] = shortest_paths

        return all_shortest_paths

    def sum_unique_paths_cost(self):
        unique_paths = set()
        total_cost = 0

        all_shortest_paths = self.shortest_paths()

        for start_node, paths in all_shortest_paths.items():
            for end_node, distance in paths.items():
                path_pair = tuple(sorted([start_node, end_node]))
                if path_pair not in unique_paths:
                    unique_paths.add(path_pair)
                    total_cost += distance

        return total_cost

    def __str__(self):
        result = "Generated Graph:\n"
        for node in self.graph.keys():
            result += f"{node} -> {self.graph[node]}\n"

        return result


def x(y):
    return y


def part1_example():
    graph = get_data(INPUT_EXAMPLE)
    print(graph)
    all_shortest_paths = graph.shortest_paths()
    for start_node, paths in all_shortest_paths.items():
        for end_node, distance in paths.items():
            print(f"Shortest path from {start_node} to {end_node}: {distance}")
    # Calculate and print the sum of costs for all unique shortest paths
    total_cost = graph.sum_unique_paths_cost()
    assert total_cost == 374

    return total_cost


def part1():
    graph = get_data(INPUT)
    # Calculate and print the sum of costs for all unique shortest paths
    total_cost = graph.sum_unique_paths_cost()
    return total_cost


def part2_example():
    return
    data = get_data(INPUT_EXAMPLE_EZI)
    answer = x(data)
    assert answer == 1

    data = get_data(INPUT_EXAMPLE_MEDIUM)
    answer = x(data)
    assert answer == 2

    data = get_data(INPUT_EXAMPLE)
    answer = x(data)
    assert answer == 3

    return answer


def part2():
    graph = get_data(INPUT, inc_cost=1000000)
    # Calculate and print the sum of costs for all unique shortest paths
    total_cost = graph.sum_unique_paths_cost()
    return total_cost


def main():
    ex1 = part1_example()
    ex2 = part2_example()
    # p1 = part1()
    p2 = part2()
    print(f"example part 1: {ex1}")
    # print(f"part 1: {p1}")
    print(f"example part 2: {ex2}")
    print(f"part 2: {p2}")


if __name__ == "__main__":
    main()
