"""
=======================================================
  PYTHON: OPERATORS & EXPRESSIONS
=======================================================

WHAT ARE OPERATORS?
Operators are special symbols and keywords in Python used to perform 
computations, assignments, comparisons, and logical evaluations on 
variables and values (operands).

-------------------------------------------------------
1. CATEGORIES OF OPERATORS
-------------------------------------------------------
- Arithmetic   : Basic mathematical operations (+, -, *, /, //, %, **)
- Assignment   : Assigning and modifying variable values (=, +=, -=, etc.)
- Comparison   : Comparing values to return boolean results (==, !=, >, <, >=, <=)
- Logical      : Combining logical expressions (and, or, not)
- Identity     : Checking if two variables reference the same object (is, is not)
- Membership   : Checking if a value exists within a sequence (in, not in)
- Bitwise      : Performing bit-level operations (&, |, ^, ~, <<, >>)

-------------------------------------------------------
2. OPERATOR PRECEDENCE (Highest to Lowest)
-------------------------------------------------------
  1. Parentheses          : ()
  2. Exponentiation       : **
  3. Unary Sign & NOT     : +x, -x, ~x
  4. Multiplication & Div : *, /, //, %
  5. Addition & Subtraction: +, -
  6. Bitwise Shifts       : <<, >>
  7. Bitwise AND          : &
  8. Bitwise XOR & OR     : ^, |
  9. Comparison & Identity: ==, !=, >, <, >=, <=, is, is not, in, not in
 10. Logical NOT          : not
 11. Logical AND          : and
 12. Logical OR           : or
 13. Assignment           : =, +=, -=, *=, /=, :=, etc.

Memory Trick:
  == checks VALUE equality   |  is checks MEMORY identity
  / always produces float    |  // drops remainder (floor)
  and requires BOTH True     |  or requires AT LEAST ONE True

=======================================================
"""

# ============================================================
# 1. ARITHMETIC OPERATORS
# ============================================================
print("=" * 60)
print("1. ARITHMETIC OPERATORS")
print("=" * 60)

a = 15
b = 4

print("a =", a, "| b =", b)
print("Addition (+):        ", a + b)
print("Subtraction (-):     ", a - b)
print("Multiplication (*):  ", a * b)
print("Float Division (/):  ", a / b)     # Always returns float (3.75)
print("Floor Division (//): ", a // b)    # Drops decimal portion (3)
print("Modulus (%):         ", a % b)     # Returns remainder (3)
print("Exponentiation (**): ", a ** b)    # 15 to the power 4 (50625)


# ============================================================
# 2. ASSIGNMENT OPERATORS
# ============================================================
print("\n" + "=" * 60)
print("2. ASSIGNMENT OPERATORS")
print("=" * 60)

x = 10
print("Initial x:", x)

x += 5;   print("x += 5  ->", x)   # Equivalent to x = x + 5
x -= 3;   print("x -= 3  ->", x)   # Equivalent to x = x - 3
x *= 2;   print("x *= 2  ->", x)   # Equivalent to x = x * 2
x /= 4;   print("x /= 4  ->", x)   # Equivalent to x = x / 4
x %= 3;   print("x %= 3  ->", x)   # Equivalent to x = x % 3
x **= 3;  print("x **= 3 ->", x)   # Equivalent to x = x ** 3

# Walrus Operator := (Assignment Expression)
if (n := len("Python")) > 3:
    print(f"String length is {n} (assigned inline via walrus operator :=)")


# ============================================================
# 3. COMPARISON OPERATORS
# ============================================================
print("\n" + "=" * 60)
print("3. COMPARISON OPERATORS")
print("=" * 60)

x, y = 20, 25

print("x =", x, "| y =", y)
print("Equal to (==):             ", x == y)
print("Not equal to (!=):         ", x != y)
print("Greater than (>):          ", x > y)
print("Less than (<):             ", x < y)
print("Greater than or equal (>=):", x >= y)
print("Less than or equal (<=):   ", x <= y)

# Chained comparisons
print("Chained comparison (10 < x < 30):", 10 < x < 30)


# ============================================================
# 4. LOGICAL OPERATORS
# ============================================================
print("\n" + "=" * 60)
print("4. LOGICAL OPERATORS")
print("=" * 60)

has_license = True
has_car = False
age = 22

# AND: Returns True only if BOTH conditions are True
can_drive = has_license and (age >= 18)
print("AND (has_license and age >= 18) :", can_drive)

# OR: Returns True if AT LEAST ONE condition is True
can_commute = has_car or has_license
print("OR (has_car or has_license)     :", can_commute)

# NOT: Inverts boolean value
print("NOT (not has_car)               :", not has_car)

# Short-circuit evaluation demonstration
print("Short-circuit (False and ...):  ", False and (10 / 0 == 0))  # Second condition skipped


# ============================================================
# 5. IDENTITY OPERATORS (is, is not)
# ============================================================
print("\n" + "=" * 60)
print("5. IDENTITY OPERATORS")
print("=" * 60)

list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print("list_a == list_b (Value equality) :", list_a == list_b)  # True (same data)
print("list_a is list_b (Memory identity):", list_a is list_b)  # False (different objects)
print("list_a is list_c (Memory identity):", list_a is list_c)  # True (same memory reference)
print("list_a is not list_b             :", list_a is not list_b)


# ============================================================
# 6. MEMBERSHIP OPERATORS (in, not in)
# ============================================================
print("\n" + "=" * 60)
print("6. MEMBERSHIP OPERATORS")
print("=" * 60)

frameworks = ["Django", "Flask", "FastAPI"]
sentence = "Python programming is fun"

print("'Flask' in frameworks    :", "Flask" in frameworks)
print("'Spring' not in frameworks:", "Spring" not in frameworks)
print("'Python' in sentence     :", "Python" in sentence)


# ============================================================
# 7. BITWISE OPERATORS
# ============================================================
print("\n" + "=" * 60)
print("7. BITWISE OPERATORS")
print("=" * 60)

# Binary: 6 = 0b0110, 3 = 0b0011
p, q = 6, 3

print(f"p = {p} (bin: {bin(p)}), q = {q} (bin: {bin(q)})")
print("Bitwise AND (&)  :", p & q,  f"| Binary: {bin(p & q)}")   # 0b0010 = 2
print("Bitwise OR (|)   :", p | q,  f"| Binary: {bin(p | q)}")   # 0b0111 = 7
print("Bitwise XOR (^)  :", p ^ q,  f"| Binary: {bin(p ^ q)}")   # 0b0101 = 5
print("Bitwise NOT (~)  :", ~p,     f"| Binary: {bin(~p)}")      # -7
print("Left Shift (<<)  :", p << 1, f"| Binary: {bin(p << 1)}") # 12 (0b1100)
print("Right Shift (>>) :", p >> 1, f"| Binary: {bin(p >> 1)}") # 3  (0b0011)


# ============================================================
# 8. QUICK REFERENCE SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("8. QUICK REFERENCE SUMMARY")
print("=" * 60)

summary_table = """
CATEGORY       OPERATORS                EXAMPLE             RETURNS
------------------------------------------------------------------
Arithmetic     +, -, *, /, //, %, **    10 // 3             Numeric value
Assignment     =, +=, -=, *=, :=, etc.  x += 5              Modifies variable
Comparison     ==, !=, >, <, >=, <=     x == y              bool (True/False)
Logical        and, or, not             x > 0 and y > 0     bool (True/False)
Identity       is, is not               a is b              bool (True/False)
Membership     in, not in               "a" in "cat"        bool (True/False)
Bitwise        &, |, ^, ~, <<, >>       6 & 3               Integer
"""
print(summary_table.strip())