"""
=======================================================
  PYTHON: FACTORIAL CALCULATOR
=======================================================

WHAT IS A FACTORIAL?
The factorial of a non-negative integer n, denoted by n!, 
is the product of all positive integers less than or equal to n.

DEFINITION:
  n! = n * (n - 1) * (n - 2) * ... * 1
  0! = 1 (by definition)

-------------------------------------------------------
1. APPROACH COMPARISON
-------------------------------------------------------
- math.factorial(n) : Built-in C-optimized function (Fastest & Best)
- Iterative Loop    : Simple loop accumulating product
- Recursion         : Classic functional approach (f(n) = n * f(n-1))
- math.prod()       : Modern one-liner using range

=======================================================
"""

import math
from functools import reduce

# ============================================================
# 1. BUILT-IN math.factorial() (FASTEST & RECOMMENDED)
# ============================================================
print("=" * 60)
print("1. BUILT-IN math.factorial()")
print("=" * 60)

n = 5
print(f"Factorial of {n} (math.factorial) : {math.factorial(n)}")


# ============================================================
# 2. ITERATIVE APPROACH (STANDARD LOOP)
# ============================================================
print("\n" + "=" * 60)
print("2. ITERATIVE APPROACH")
print("=" * 60)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"Factorial of {n} (Iterative)      : {factorial_iterative(n)}")


# ============================================================
# 3. RECURSIVE & ONE-LINER APPROACHES
# ============================================================
print("\n" + "=" * 60)
print("3. RECURSIVE & ONE-LINER APPROACHES")
print("=" * 60)

# Recursive Function
fact_rec = lambda n: 1 if n <= 1 else n * fact_rec(n - 1)

# Using math.prod (Python 3.8+)
fact_prod = lambda n: math.prod(range(1, n + 1))

# Using reduce
fact_reduce = lambda n: reduce(lambda x, y: x * y, range(1, n + 1), 1)

print("Recursive One-Liner fact_rec(5)   :", fact_rec(5))
print("math.prod One-Liner fact_prod(5)  :", fact_prod(5))
print("reduce One-Liner fact_reduce(5)   :", fact_reduce(5))


# ============================================================
# 4. QUICK REFERENCE SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("4. QUICK REFERENCE SUMMARY")
print("=" * 60)

summary_table = """
APPROACH             CODE EXAMPLE                                   TIME COMPLEXITY
-------------------------------------------------------------------------------------
Built-in             math.factorial(n)                              O(n) (C-optimized)
Iterative Loop       r = 1; for i in range(2, n+1): r *= i          O(n)
Recursive            f = lambda n: 1 if n<=1 else n * f(n-1)        O(n)
math.prod()          math.prod(range(1, n + 1))                    O(n)
"""
print(summary_table.strip())