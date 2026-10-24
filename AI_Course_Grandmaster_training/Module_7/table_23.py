"""
=======================================================
  PYTHON: MULTIPLICATION TABLE OF 23
=======================================================

GENERATING TABLES IN PYTHON:
Multiplication tables can be easily generated using simple 
loops, list comprehensions, or string formatting.

-------------------------------------------------------
1. COMMON APPROACHES
-------------------------------------------------------
- Standard For Loop : Clean, readable, and explicit
- List Comprehension : One-liner compact generation
- F-String Formatting: Aligned output for easy reading

=======================================================
"""

# ============================================================
# 1. STANDARD FOR LOOP (RECOMMENDED & READABLE)
# ============================================================
print("=" * 60)
print("1. STANDARD FOR LOOP")
print("=" * 60)

num = 23
for i in range(1, 11):
    print(f"{num} x {i:2d} = {num * i}")


# ============================================================
# 2. ONE-LINER (LIST COMPREHENSION & JOIN)
# ============================================================
print("\n" + "=" * 60)
print("2. ONE-LINER (LIST COMPREHENSION)")
print("=" * 60)

# Single line table generation
print("\n".join(f"23 x {i:2d} = {23 * i}" for i in range(1, 11)))


# ============================================================
# 3. REUSABLE FUNCTION FOR ANY TABLE
# ============================================================
print("\n" + "=" * 60)
print("3. REUSABLE TABLE FUNCTION")
print("=" * 60)

table = lambda n, limit=10: [f"{n} x {i} = {n*i}" for i in range(1, limit + 1)]

print("\n".join(table(23)))


# ============================================================
# 4. QUICK REFERENCE SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("4. QUICK REFERENCE SUMMARY")
print("=" * 60)

summary_table = """
APPROACH            CODE EXAMPLE                                     DESCRIPTION
----------------------------------------------------------------------------------
For Loop            for i in range(1,11): print(f"23 x {i} = {23*i}") Clean & simple
List Comprehension  print("\\n".join(f"23 x {i} = {23*i}" for i in range(1,11))) One-liner
Lambda Function     table = lambda n: [f"{n} x {i} = {n*i}" for i in range(1,11)] Reusable
"""
print(summary_table.strip())