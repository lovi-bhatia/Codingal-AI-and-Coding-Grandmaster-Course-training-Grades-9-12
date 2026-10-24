"""
=======================================================
  PYTHON: BASIC CALCULATOR
=======================================================

WHAT IS A BASIC CALCULATOR?
A program that performs fundamental arithmetic operations:
Addition (+), Subtraction (-), Multiplication (*), and Division (/).

-------------------------------------------------------
1. APPROACH COMPARISON
-------------------------------------------------------
- Dictionary Dispatch : Maps operator strings to functions cleanly
- Match-Case (3.10+)  : Modern, clean conditional structure
- Lambda Dictionary   : Ultra-compact functional approach
- eval() Expression   : Evaluates string expressions directly

=======================================================
"""

# ============================================================
# 1. DICTIONARY DISPATCH CALCULATOR (RECOMMENDED)
# ============================================================
print("=" * 60)
print("1. DICTIONARY DISPATCH CALCULATOR")
print("=" * 60)

ops = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Error: Division by zero"
}

def calculate(a, op, b):
    return ops.get(op, lambda a, b: "Invalid Operator")(a, b)

print("10 + 5  =", calculate(10, "+", 5))
print("10 / 0  =", calculate(10, "/", 0))
print("12 * 4  =", calculate(12, "*", 4))


# ============================================================
# 2. MATCH-CASE CALCULATOR (PYTHON 3.10+)
# ============================================================
print("\n" + "=" * 60)
print("2. MATCH-CASE CALCULATOR")
print("=" * 60)

def calc_match(a, op, b):
    match op:
        case '+': return a + b
        case '-': return a - b
        case '*': return a * b
        case '/': return a / b if b != 0 else "Error: Division by zero"
        case _:   return "Invalid Operator"

print("15 - 7  =", calc_match(15, "-", 7))
print("20 / 4  =", calc_match(20, "/", 4))


# ============================================================
# 3. ONE-LINER EXPRESSION CALCULATOR (EVAL)
# ============================================================
print("\n" + "=" * 60)
print("3. ONE-LINER EXPRESSION CALCULATOR")
print("=" * 60)

expr = "25 * 4 + 10"
print(f"Expression: '{expr}' -> Result:", eval(expr))


# ============================================================
# 4. QUICK REFERENCE SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("4. QUICK REFERENCE SUMMARY")
print("=" * 60)

summary_table = """
APPROACH             CODE EXAMPLE                                   ADVANTAGE
-------------------------------------------------------------------------------------
Dict Dispatch        ops[op](a, b)                                  Fast & extensible
Match-Case           match op: case '+': return a+b                 Clean syntax (3.10+)
Lambda Dict          {'+': lambda a,b: a+b}[op](a,b)                Compact functional
eval()               eval("10 + 5")                                 Parses full strings
"""
print(summary_table.strip())