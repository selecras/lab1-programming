def factorial(n: int) -> int:
    """Вычисляет факториал числа n."""
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    for i in range(11):
        print(f"{i}! = {factorial(i)}")
