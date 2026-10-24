"""
=======================================================
  PYTHON: SUM OF NATURAL NUMBERS
=======================================================

NATURAL NUMBERS:
Positive integers starting from 1 (1, 2, 3, 4, 5, ...).

-------------------------------------------------------
1. APPROACH COMPARISON
-------------------------------------------------------
- Mathematical Formula : n * (n + 1) // 2  -> O(1) Constant Time (Fastest)
- Built-in sum()       : sum(range(1, n+1)) -> O(n) Linear Time (Pythonic)

=======================================================
"""

# ============================================================
# 1. MATHEMATICAL FORMULA - O(1) TIME (FASTEST & BEST)
# ============================================================
print("=" * 60)
print("1. MATHEMATICAL FORMULA - O(1) TIME")
print("=" * 60)

n = 100

# Formula: n * (n + 1) / 2
total = n * (n + 1) // 2

print(f"Sum of first {n} natural numbers: {total}")


# ============================================================
# 2. BUILT-IN sum() WITH range() (ONE-LINER)
# ============================================================
print("\n" + "=" * 60)
print("2. BUILT-IN sum() WITH range()")
print("=" * 60)

n = 100

# Generates range from 1 to n and sums all elements
print(f"Sum using sum(range(1, {n}+1)): {sum(range(1, n + 1))}")


# ============================================================
# 3. LAMBDA & RECURSIVE ONE-LINERS
# ============================================================
print("\n" + "=" * 60)
print("3. LAMBDA & RECURSIVE ONE-LINERS")
print("=" * 60)

# Lambda Function (O(1) formula)
sum_n = lambda n: n * (n + 1) // 2
print("Lambda Formula (n=50)  :", sum_n(50))

# Recursive One-Liner (O(n))
rec_sum = lambda n: n + rec_sum(n - 1) if n > 0 else 0
print("Recursive Sum (n=10)   :", rec_sum(10))


# ============================================================
# 4. QUICK REFERENCE SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("4. QUICK REFERENCE SUMMARY")
print("=" * 60)

summary_table = """
APPROACH            CODE EXAMPLE                     TIME COMPLEXITY
---------------------------------------------------------------------
Formula (Math)      n * (n + 1) // 2                 O(1) (Fastest)
Built-in sum()      sum(range(1, n + 1))             O(n)
Lambda Function     lambda n: n * (n + 1) // 2       O(1)
Recursion           n + rec_sum(n - 1) if n else 0   O(n)
"""
print(summary_table.strip())