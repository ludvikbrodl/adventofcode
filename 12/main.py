from collections import defaultdict
from pathlib import Path
from copy import deepcopy

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"
INPUT_EXAMPLE_EZI = "input_example_ezi.txt"
INPUT_EXAMPLE_MEDIUM = "input_example_medium.txt"


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").readlines()]


def get_data(path) -> list[int]:
    return [tuple(locations.split("-")) for locations in get_lines(path)]


def calc_paths(node_map):
    master_list = []
    calc_paths_recursive("start", node_map, master_list, prev_nodes=["start"])
    return master_list


def calc_paths_recursive(
    current_node: str, node_map: dict, master_list: list, prev_nodes: list
):
    if current_node == "end":
        master_list.append(prev_nodes)
        return
    next_nodes = node_map[current_node]
    visited_small_nodes = list(filter(lambda node: node.islower(), prev_nodes))

    no_visited_small_nodes = list(
        filter(lambda node: node not in visited_small_nodes, next_nodes)
    )
    for node in no_visited_small_nodes:
        new_nodes_list: list = deepcopy(prev_nodes)
        new_nodes_list.append(node)
        calc_paths_recursive(node, node_map, master_list, new_nodes_list)


def calc_paths_recursive_double_small_visits(
    current_node: str,
    node_map: dict,
    master_list: list,
    prev_nodes: list,
):
    if current_node == "end":
        master_list.append(prev_nodes)
        return
    next_nodes = node_map[current_node]
    visited_small_nodes = list(filter(lambda node: node.islower(), prev_nodes))
    visited_small_nodes_bucket = defaultdict(int)
    for node in visited_small_nodes:
        visited_small_nodes_bucket[node] += 1

    if max(visited_small_nodes_bucket.values()) < 2:
        no_visited_small_nodes = next_nodes
    else:
        no_visited_small_nodes = list(
            filter(lambda node: node not in visited_small_nodes, next_nodes)
        )
    for node in no_visited_small_nodes:
        new_nodes_list: list = deepcopy(prev_nodes)
        new_nodes_list.append(node)
        calc_paths_recursive_double_small_visits(
            node, node_map, master_list, new_nodes_list
        )


def calc_paths_double_small_visits(node_map):
    master_list = []
    calc_paths_recursive_double_small_visits(
        "start", node_map, master_list, prev_nodes=["start"]
    )
    return master_list


def part1_example():
    edges = get_data(INPUT_EXAMPLE_EZI)
    node_map = get_node_map(edges)
    paths = calc_paths(node_map)
    assert len(paths) == 10

    edges = get_data(INPUT_EXAMPLE_MEDIUM)
    node_map = get_node_map(edges)
    paths = calc_paths(node_map)
    assert len(paths) == 19

    edges = get_data(INPUT_EXAMPLE)
    node_map = get_node_map(edges)
    paths = calc_paths(node_map)
    assert len(paths) == 226

    return len(paths)


def part1():
    edges = get_data(INPUT)
    node_map = get_node_map(edges)
    paths = calc_paths(node_map)
    return len(paths)


def part2_example():
    edges = get_data(INPUT_EXAMPLE_EZI)
    node_map = get_node_map(edges)
    paths = calc_paths_double_small_visits(node_map)
    assert len(paths) == 36

    edges = get_data(INPUT_EXAMPLE_MEDIUM)
    node_map = get_node_map(edges)
    paths = calc_paths_double_small_visits(node_map)
    assert len(paths) == 103

    edges = get_data(INPUT_EXAMPLE)
    node_map = get_node_map(edges)
    paths = calc_paths_double_small_visits(node_map)
    assert len(paths) == 3509

    return len(paths)


def get_node_map(edges):
    node_map = defaultdict(list)
    for from_node, to_node in edges:
        if to_node != "start":
            node_map[from_node].append(to_node)
        if from_node != "start":
            node_map[to_node].append(from_node)
    return node_map


def part2():
    edges = get_data(INPUT)
    node_map = get_node_map(edges)
    paths = calc_paths_double_small_visits(node_map)
    return len(paths)


def main():
    ex1 = part1_example()
    ex2 = part2_example()
    p1 = part1()
    p2 = part2()
    print(f"example part 1: {ex1}")
    print(f"part 1: {p1}")
    print(f"example part 2: {ex2}")
    print(f"part 2: {p2}")


if __name__ == "__main__":
    main()
