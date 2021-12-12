import fileinput

adj: dict[str, list[str]] = {}
paths: set[list[str]] = set()


def main() -> None:
    global adj

    nodes: dict[str, int] = {}

    line: str
    for line in fileinput.input():
        line: list[str] = line.strip().split("-")
        if line[0] not in adj:
            adj[line[0]] = []
        adj[line[0]].append(line[1])
        nodes[line[0]] = 0

        if line[1] not in adj:
            adj[line[1]] = []
        adj[line[1]].append(line[0])
        nodes[line[1]] = 0

    visit(nodes, [], "start")

    print(len(paths))


def visit(nodes: dict[str, int], path: list[str], node: str) -> None:
    global paths

    path = path.copy()
    path.append(node)

    if node == "end":
        paths.add(",".join(path))
        return

    if node.islower():
        nodes = nodes.copy()
        nodes[node] += 1

    for d in adj.get(node):
        if (d != "start") and (nodes[d] < 1 or 2 not in nodes.values()):
            visit(nodes, path, d)


if __name__ == "__main__":
    main()
