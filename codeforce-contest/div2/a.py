def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        total_sum = sum(a)

        cnt = [0] * 101
        for num in a:
            cnt[num] += 1

        freq = cnt[:]
        mex1 = mex2 = 0

        for i in range(101):
            if freq[i] > 0:
                freq[i] -= 1
            else:
                mex1 = i
                break

        for i in range(101):
            if freq[i] > 0:
                freq[i] -= 1
            else:
                mex2 = i
                break

        print(max(total_sum, mex1 + mex2))

solve()
 