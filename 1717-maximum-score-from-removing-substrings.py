def maximumGain(s: str, x: int, y: int) -> int:
    def remove_substring(s: str, first: str, second: str, score: int):
        stack = []
        total = 0
        for ch in s:
            if stack and stack[-1] == first and ch == second:
                stack.pop()
                total += score
            else:
                stack.append(ch)
        return ''.join(stack), total

    total_score = 0

    # Step 1: Remove the higher scoring substring first
    if x >= y:
        s, score1 = remove_substring(s, 'a', 'b', x)
        _, score2 = remove_substring(s, 'b', 'a', y)
    else:
        s, score1 = remove_substring(s, 'b', 'a', y)
        _, score2 = remove_substring(s, 'a', 'b', x)

    total_score = score1 + score2
    return total_score



print(maximumGain("aabbaaxybbaabb", 4, 5)) 