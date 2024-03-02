
value: list[int] = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59]
weight: list[int] = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52]

class Knapsack:
    def __init__(self, value: list[int], weight: list[int], capacity: int) -> None:
        self.value = value
        self.weight = weight
        self.capacity = capacity
        self.n = len(value)
        self.matrix = [[0] * (capacity + 1) for _ in range(self.n + 1)]

    def solve(self) -> list[int]:
        for i in range(1, self.n + 1):
            for w in range(1, self.capacity + 1):
                if self.weight[i - 1] > w:
                    self.matrix[i][w] = self.matrix[i - 1][w]
                else:
                    self.matrix[i][w] = max(
                        self.matrix[i - 1][w],
                        self.matrix[i - 1][w - self.weight[i - 1]] + self.value[i - 1]
                    )
        return self._get_items()
    
    def _get_items(self) -> list[int]:
        i, w = self.n, self.capacity
        items = []
        while i > 0 and w > 0:
            if self.matrix[i][w] != self.matrix[i - 1][w]:
                items.append(i - 1)
                w -= self.weight[i - 1]
            i -= 1
        return items
    
    def print_matrix(self) -> None:
        for row in self.matrix:
            print(row)

if __name__ == "__main__":
    knapsack = Knapsack(value, weight, 100)
    result = knapsack.solve()
    print(
        "Items(indexes):",
        ", ".join(str(i) for i in result),
    )
    
