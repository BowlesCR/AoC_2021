import fileinput

adj: dict[str, list[str]] = {}
paths: set[list[str]] = set()


def main() -> None:
    global adj

    nodes: set[str] = set()

    line: str
    for line in fileinput.input():
        line: list[str] = line.strip().split("-")
        if line[0] not in adj:
            adj[line[0]] = []
        adj[line[0]].append(line[1])
        nodes.add(line[0])

        if line[1] not in adj:
            adj[line[1]] = []
        adj[line[1]].append(line[0])
        nodes.add(line[1])

    visit(nodes, [], "start")

    print(len(paths))


def visit(nodes: set[str], path: list[str], node: str) -> None:
    global paths

    path = path.copy()
    path.append(node)

    if node == "end":
        paths.add(",".join(path))
        return

    if node.islower():
        nodes = nodes.copy()
        nodes.remove(node)

    for d in adj.get(node):
        if d in nodes:
            visit(nodes, path, d)


if __name__ == "__main__":
    main()
