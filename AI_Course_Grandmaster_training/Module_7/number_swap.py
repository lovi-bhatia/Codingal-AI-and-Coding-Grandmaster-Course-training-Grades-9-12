"""
=======================================================
  PYTHON: NUMBER SWAPPING
=======================================================
In Python, swapping two variables takes just ONE line of code 
using tuple unpacking, requiring NO temporary variables!
=======================================================
"""

# ============================================================
# 1. THE PYTHONIC WAY (1-LINE SWAP) - RECOMMENDED
# ============================================================
print("=" * 60)
print("1. PYTHONIC WAY (1 LINE)")
print("=" * 60)

a, b = 5, 10
print(f"Before: a = {a}, b = {b}")

# ONE LINE SWAP
a, b = b, a

print(f"After : a = {a}, b = {b}")


# ============================================================
# 2. ALTERNATIVE METHODS (FOR REFERENCE)
# ============================================================
print("\n" + "=" * 60)
print("2. ALTERNATIVE METHODS")
print("=" * 60)

# Method A: Using XOR (Bitwise - No extra memory)
x, y = 5, 10
x ^= y; y ^= x; x ^= y
print(f"XOR Swap        : x = {x}, y = {y}")

# Method B: Using Arithmetic (+ / -)
x, y = 5, 10
x = x + y; y = x - y; x = x - y
print(f"Arithmetic Swap : x = {x}, y = {y}")

# Method C: Using Temp Variable (Traditional)
x, y = 5, 10
temp = x; x = y; y = temp
print(f"Temp Var Swap   : x = {x}, y = {y}")


# ============================================================
# 3. QUICK REFERENCE SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("3. QUICK REFERENCE SUMMARY")
print("=" * 60)

summary_table = """
METHOD            CODE EXAMPLE            LINES   TEMP VAR?
------------------------------------------------------------
Tuple Unpacking   a, b = b, a             1 Line  No (Best)
Bitwise XOR       x^=y; y^=x; x^=y        1 Line  No
Arithmetic        x=x+y; y=x-y; x=x-y     3 Lines No
Temporary Var     t=x; x=y; y=t           3 Lines Yes
"""
print(summary_table.strip())