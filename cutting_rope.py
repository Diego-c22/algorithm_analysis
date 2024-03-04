size: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
price: list[int] = [1, 4, 10, 12, 15, 20, 21, 32, 31, 41, 51]

def cutting_rope(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return price[0]
    max_price: int = 0
    for i in range(n):
        max_price = max(max_price, price[i] + cutting_rope(n - i - 1))
    return max_price


if __name__ == '__main__':
    print(cutting_rope(4))