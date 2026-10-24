"""
=======================================================
  PYTHON: STAR PATTERNS
=======================================================

WHY STAR PATTERNS?
Star patterns build logical thinking for loops and string formatting.

-------------------------------------------------------
1. THE PYTHONIC PATTERN TRICK
-------------------------------------------------------
In Python, string multiplication eliminates the need for 
nested inner loops!
  "*" * 5   -> "*****"
  " " * 3   -> "   "

=======================================================
"""

# ============================================================
# 1. RIGHT-ANGLED TRIANGLE
# ============================================================
print("=" * 60)
print("1. RIGHT-ANGLED TRIANGLE")
print("=" * 60)

n = 5
for i in range(1, n + 1):
    print("*" * i)


# ============================================================
# 2. INVERTED RIGHT-ANGLED TRIANGLE
# ============================================================
print("\n" + "=" * 60)
print("2. INVERTED RIGHT-ANGLED TRIANGLE")
print("=" * 60)

n = 5
for i in range(n, 0, -1):
    print("*" * i)


# ============================================================
# 3. FULL PYRAMID & DIAMOND PATTERN
# ============================================================
print("\n" + "=" * 60)
print("3. FULL PYRAMID & DIAMOND")
print("=" * 60)

n = 5

print("--- Pyramid ---")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

print("\n--- Diamond ---")
# Top half
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# Bottom half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# ============================================================
# 4. ONE-LINER PATTERN GENERATORS
# ============================================================
print("\n" + "=" * 60)
print("4. ONE-LINER PATTERN GENERATORS")
print("=" * 60)

print("Right Triangle (One-Liner):")
print("\n".join("*" * i for i in range(1, 6)))

print("\nPyramid (One-Liner):")
print("\n".join(" " * (5 - i) + "*" * (2 * i - 1) for i in range(1, 6)))


# ============================================================
# 5. QUICK REFERENCE SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("5. QUICK REFERENCE SUMMARY")
print("=" * 60)

summary_table = """
PATTERN           PRINT EXPRESSION                                 LOGIC
---------------------------------------------------------------------------------
Right Triangle    print("*" * i)                                   i stars per row
Inverted Triangle print("*" * i) [range(n, 0, -1)]               Decreasing stars
Right-Aligned     print(" " * (n - i) + "*" * i)                   Spaces + stars
Full Pyramid      print(" " * (n - i) + "*" * (2 * i - 1))       Centered odd stars
Hollow Square     print("*" * n if i in (1, n) else "*" + " "*(n-2) + "*") Edges only
"""
print(summary_table.strip())