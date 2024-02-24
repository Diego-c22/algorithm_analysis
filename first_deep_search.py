from collections import defaultdict
from data import edges, nodes


class DeepFirstSearch:
    def __init__(self, edges: list[tuple[int, int]], nodes: list[int]):
        self.adjacency_list = defaultdict(list)
        self.edges = edges
        self.nodes = nodes
        self.components: list[int] = []
        self.visited = set()

    def fill_adjacency_list(self):
        for edge in self.edges:
            a, b = edge
            self.adjacency_list[a].append(b)
            self.adjacency_list[b].append(a)

    def dfs(self, start: int):
        nodes = self.adjacency_list[start]
        for node in nodes:
            if node not in self.visited:
                self.visited.add(node)
                self.dfs(node)

    def get_connected_components(self):
        for node in self.nodes:
            if node not in [i for component in self.components for i in component]:
                self.dfs(node)
                self.components.append(self.visited)
                self.visited = set()
        return self.components


if __name__ == '__main__':
    dfs = DeepFirstSearch(edges, nodes)
    dfs.fill_adjacency_list()
    components = dfs.get_connected_components()

    for i, component in enumerate(components):
        print(f'\n Component {i + 1}: {component} \n')
