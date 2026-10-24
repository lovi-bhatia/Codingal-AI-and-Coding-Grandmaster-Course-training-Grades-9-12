"""
=======================================================
  PYTHON: CHECK ODD OR EVEN
=======================================================
In Python, checking if a number is odd or even requires 
just a simple modulus operation (% 2) or a bitwise check (& 1).
=======================================================
"""

# ============================================================
# 1. ONE-LINER TERNARY EXPRESSION (RECOMMENDED)
# ============================================================
print("=" * 60)
print("1. ONE-LINER TERNARY EXPRESSION")
print("=" * 60)

n = 7

# One line check
result = "Even" if n % 2 == 0 else "Odd"
print(f"Number {n} is: {result}")


# ============================================================
# 2. BITWISE AND METHOD (& 1) - FASTEST & MINIMAL
# ============================================================
print("\n" + "=" * 60)
print("2. BITWISE AND METHOD")
print("=" * 60)

num = 12

# Odd numbers always have the last binary bit set to 1
print(f"{num} is: {('Even', 'Odd')[num & 1]}")


# ============================================================
# 3. LAMBDA ONE-LINER FUNCTIONS
# ============================================================
print("\n" + "=" * 60)
print("3. LAMBDA FUNCTIONS")
print("=" * 60)

is_even = lambda x: x % 2 == 0
is_odd  = lambda x: x % 2 != 0

print("is_even(10) :", is_even(10))
print("is_odd(10)  :", is_odd(10))


# ============================================================
# 4. QUICK REFERENCE SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("4. QUICK REFERENCE SUMMARY")
print("=" * 60)

summary_table = """
METHOD            CODE EXAMPLE                     DESCRIPTION
------------------------------------------------------------------
Modulus (%)       "Even" if n % 2 == 0 else "Odd"  Standard ternary
Bitwise (&)       ("Even", "Odd")[n & 1]           Fastest index lookup
Lambda Func       is_even = lambda x: x % 2 == 0   Compact function
Boolean Expression n % 2 == 0                      Returns True/False
"""
print(summary_table.strip())