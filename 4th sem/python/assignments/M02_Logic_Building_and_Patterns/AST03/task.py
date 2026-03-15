def sum_of_digits(n: int) -> int:
    n = str(n)
    total = 0

    for i in n:
        total += int(i)

    return total


if __name__ == "__main__":
    n = int(input())
    print(sum_of_digits(n))
