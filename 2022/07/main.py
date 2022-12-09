from pathlib import Path

INPUT = "input.txt"
INPUT_EXAMPLE = "input_example.txt"
INPUT_EXAMPLE_EZI = "input_example_ezi.txt"
INPUT_EXAMPLE_MEDIUM = "input_example_medium.txt"

INDENT = "  "


class Node:
    def __init__(self, data, name, parent):  # for root only
        self.data = data  # size or "dir"
        self.name = name
        self.parent: Node = parent
        self.children: list[Node] = []

    def isDir(self):
        return len(self.children) > 0

    def isFile(self):
        return not self.isDir()

    def addChild(self, console_log_line):
        size, name = console_log_line.split(" ")
        self.children.append(Node(size, name, self))

    def getChild(self, name):
        return next(x for x in self.children if name == x.name)

    def getParent(self):
        return self.parent

    def __str__(self):
        return "\n" + self.str_with_tabs(0)

    def str_with_tabs(self, depth):
        if self.isFile():
            return INDENT * depth + f"- {self.name} (file, size={self.data})"
        else:
            dir_str = INDENT * depth + f"- {self.name} ({self.data})"
            return (
                dir_str
                + "\n"
                + f"\n".join(
                    [child.str_with_tabs(depth + 1) for child in self.children]
                )
            )

    def get_size(self):
        if self.isFile():
            return int(self.data)
        return sum([c.get_size() for c in self.children])

    def find_all_dirs(self):
        dirs = []
        find_all_dirs_recursive(self, dirs)
        return dirs


def find_all_dirs_recursive(current: Node, dir_list: list[Node]):
    if current.isFile():
        return
    else:
        dir_list.append(current)
        for c in current.children:
            find_all_dirs_recursive(c, dir_list)


def get_lines(path: str) -> list[str]:
    script_location = Path(__file__).absolute().parent
    file_location = script_location / path
    return [l.strip() for l in open(file_location, "r").readlines()]


def get_data(path) -> list[str]:
    return get_lines(path)


def build_tree(console_log_lines: list[str]):
    root = Node("dir", "/", None)
    current = root
    for line in console_log_lines:
        if line[0] == "$":
            cmd = line[2:].split(" ")
            if len(cmd) > 1:  # is cd cmd
                dest = cmd[1]
                if dest == "/":
                    current = root
                elif dest == "..":
                    current = current.getParent()
                else:
                    current = current.getChild(dest)
        else:
            current.addChild(line)
    return root


def part1_example():
    data = get_data(INPUT_EXAMPLE)
    root = build_tree(data)
    all_dirs = root.find_all_dirs()
    sizes = []
    for d in all_dirs:
        size = d.get_size()
        if size <= 100_000:
            sizes.append(size)
    return sizes


def part1():
    # naive solution, doesnt save the size of children
    # O(x^n)
    # where
    # x = depth
    # n = number of dirs
    data = get_data(INPUT)
    root = build_tree(data)
    all_dirs = root.find_all_dirs()
    sizes = []
    for d in all_dirs:
        size = d.get_size()
        if size <= 100_000:
            sizes.append(size)
    return sum(sizes)


FILE_SYSTEM_SIZE = 70_000_000
REQUIRED_SIZE = 30_000_000


def part2_example():
    data = get_data(INPUT_EXAMPLE)
    root = build_tree(data)
    all_dirs = root.find_all_dirs()
    sizes = []
    for d in all_dirs:
        size = d.get_size()
        sizes.append(size)
    used_space = root.get_size()
    for x in sorted(sizes):
        if (FILE_SYSTEM_SIZE - used_space + x) >= REQUIRED_SIZE:
            return x


def part2():
    data = get_data(INPUT)
    root = build_tree(data)
    all_dirs = root.find_all_dirs()
    sizes = []
    for d in all_dirs:
        size = d.get_size()
        sizes.append(size)
    used_space = root.get_size()
    for x in sorted(sizes):
        if (FILE_SYSTEM_SIZE - used_space + x) >= REQUIRED_SIZE:
            return x


def main():
    ex1 = part1_example()
    ex2 = part2_example()
    p1 = part1()
    assert p1 == 1743217
    p2 = part2()
    print(f"example part 1: {ex1}")
    print(f"part 1: {p1}")
    print(f"example part 2: {ex2}")
    print(f"part 2: {p2}")


if __name__ == "__main__":
    main()
