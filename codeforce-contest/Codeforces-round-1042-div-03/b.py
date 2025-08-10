# Alternating Series

def process_case(n: int) -> None:
    result = []
    for i in range(n):
        val = -1 if i % 2 == 0 else 3
        if n % 2 == 0 and i == n - 1:
            val = 2
        result.append(str(val))
    print(" ".join(result))

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        process_case(n)

if __name__ == "__main__":
    main()