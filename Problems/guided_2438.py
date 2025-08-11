"""
Guided Coding Practice: Build up to LeetCode 2438 (Product of Two Powers)

How to use:
- Fill each TODO step-by-step.
- Run this file:  python guided_2438_practice.py
- All tests should PASS at each stage before moving on.
"""

MOD = 1_000_000_007

# =========================
# Stage 1 — Bit Basics
# =========================

def list_powers_of_two(n: int) -> list[int]:
    """
    Return the minimal non-decreasing list of powers of two that sum to n.
    Example: n=13 (1101b) -> [1, 4, 8]
    Hints:
      - Scan bits from LSB to MSB using a loop while n > 0
      - If current bit is 1 -> append (1 << i)
      - Move to next bit (i += 1) and shift n or use a separate copy
    """
    # TODO: implement
    raise NotImplementedError

def count_set_bits(n: int) -> int:
    """
    Return the number of 1-bits in n.
    Hints:
      - Use n & 1 and shift, OR use Brian Kernighan trick: while n: n &= n-1; count += 1
    """
    # TODO: implement
    raise NotImplementedError

def largest_power_of_two_leq(n: int) -> int:
    """
    Return the largest power of two <= n.
    Examples: n=1->1, n=5->4, n=8->8, n=13->8
    Hints:
      - One way: keep doubling from 1 until > n, then step back
      - Or use bit_length: 1 << (n.bit_length()-1)
    """
    # TODO: implement
    raise NotImplementedError


# =========================
# Stage 2 — Prefix Sums
# =========================

def prefix_sums(arr: list[int]) -> list[int]:
    """
    Return prefix sums with a leading 0.
    Example: [1,4,8] -> [0,1,5,13]
    """
    # TODO: implement
    raise NotImplementedError

def range_sum(pref: list[int], L: int, R: int) -> int:
    """
    Return sum(arr[L:R+1]) given a prefix array "pref".
    By definition: sum(L..R) = pref[R+1] - pref[L].
    """
    # TODO: implement
    raise NotImplementedError

def exponents_from_n(n: int) -> list[int]:
    """
    Return the exponent list (positions of set bits) in ascending order.
    Example: n=13(1101b) -> [0,2,3] because 2^0, 2^2, 2^3
    """
    # TODO: implement
    raise NotImplementedError

def exponents_prefix_sums(n: int) -> list[int]:
    """
    Return prefix sums (with leading 0) of the exponent list.
    Example: n=13 -> exps=[0,2,3], pref=[0,0,2,5]
    """
    # TODO: implement
    raise NotImplementedError


# =========================
# Stage 3 — Modular Exponentiation
# =========================

def mod_pow2(exp: int, mod: int = MOD) -> int:
    """
    Compute (2^exp) % mod using Python's built-in fast pow.
    """
    # TODO: implement
    raise NotImplementedError

def product_by_range_exponents(exps: list[int], L: int, R: int, mod: int = MOD) -> int:
    """
    Given exponents array (e.g., [0,2,3] meaning values [1,4,8]),
    return product over exps[L..R] as 2^(sum exps[L..R]) % mod.
    Use a prefix-sum trick internally.
    """
    # TODO: implement
    raise NotImplementedError


# =========================
# Final — Combine Everything
# =========================

def productQueries(n: int, queries: list[list[int]], mod: int = MOD) -> list[int]:
    """
    For each [L,R], compute product of the minimal powers-of-two array slice.
    Strategy:
      1) exps = exponents_from_n(n)
      2) Build prefix sums of exps
      3) For each query, compute s = pref[R+1]-pref[L]
      4) Answer = pow(2, s, mod)
    """
    # TODO: implement
    raise NotImplementedError


# =========================
# Tests (run progressively)
# =========================

def _stage1_tests():
    # list_powers_of_two
    assert list_powers_of_two(1) == [1]
    assert list_powers_of_two(2) == [2]
    assert list_powers_of_two(3) == [1,2]
    assert list_powers_of_two(5) == [1,4]
    assert list_powers_of_two(13) == [1,4,8]

    # count_set_bits
    assert count_set_bits(0) == 0
    assert count_set_bits(1) == 1
    assert count_set_bits(5) == 2     # 101b
    assert count_set_bits(15) == 4    # 1111b
    assert count_set_bits(1023) == 10

    # largest_power_of_two_leq
    assert largest_power_of_two_leq(1) == 1
    assert largest_power_of_two_leq(2) == 2
    assert largest_power_of_two_leq(3) == 2
    assert largest_power_of_two_leq(5) == 4
    assert largest_power_of_two_leq(8) == 8
    assert largest_power_of_two_leq(13) == 8

def _stage2_tests():
    # prefix_sums & range_sum
    pref = prefix_sums([1,4,8])
    assert pref == [0,1,5,13]
    assert range_sum(pref, 0, 0) == 1
    assert range_sum(pref, 0, 1) == 5
    assert range_sum(pref, 1, 2) == 12
    assert range_sum(pref, 0, 2) == 13

    # exponents_from_n & exponents_prefix_sums
    exps = exponents_from_n(13)  # 1101b
    assert exps == [0,2,3]
    pref_e = exponents_prefix_sums(13)
    assert pref_e == [0,0,2,5]

def _stage3_tests():
    # mod_pow2
    assert mod_pow2(0) == 1 % MOD
    assert mod_pow2(5) == pow(2,5,MOD)
    assert mod_pow2(1000) == pow(2,1000,MOD)

    # product_by_range_exponents
    exps = [0,2,3]  # [1,4,8]
    assert product_by_range_exponents(exps, 0, 0) == 1
    assert product_by_range_exponents(exps, 0, 1) == 4
    assert product_by_range_exponents(exps, 1, 2) == 32
    assert product_by_range_exponents(exps, 0, 2) == 32

def _final_tests():
    # From examples similar to LC style
    # n=15 -> exps=[0,1,2,3], powers=[1,2,4,8]
    assert productQueries(15, [[0,1],[2,2],[0,3]]) == [2,4,64]
    # another
    assert productQueries(13, [[0,0],[0,1],[1,2]]) == [1,4,32]

if __name__ == "__main__":
    # Run staged tests progressively.
    # Uncomment the next lines one stage at a time as you implement functions.

    try:
        _stage1_tests()
        print("Stage 1 ✅ Passed")
    except NotImplementedError:
        print("Stage 1 ⏳ Pending (fill TODOs)")
        raise

    try:
        _stage2_tests()
        print("Stage 2 ✅ Passed")
    except NotImplementedError:
        print("Stage 2 ⏳ Pending (fill TODOs)")
        raise

    try:
        _stage3_tests()
        print("Stage 3 ✅ Passed")
    except NotImplementedError:
        print("Stage 3 ⏳ Pending (fill TODOs)")
        raise

    try:
        _final_tests()
        print("Final ✅ Passed — You're ready for LC 2438!")
    except NotImplementedError:
        print("Final ⏳ Pending (fill TODOs)")
        raise
