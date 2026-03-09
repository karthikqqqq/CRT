import math

def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    avg = (n1 + n2 + n3) / 3

    # Truncate to 2 decimal places
    avg = math.floor(avg * 100) / 100

    # Format average safely
    if round(avg, 2) == int(avg):
        avg_str = f"{int(avg):.1f}"
    else:
        avg_str = f"{avg:.2f}"

    status = "Pass" if avg >= 35 else "fail"

    return f"Average grade: {avg_str}, Status: {status}"


if __name__ == '__main__':
    name = input()
    n1, n2, n3 = list(map(int, input().split()))
    print(Student_Grade_System(name, n1, n2, n3))