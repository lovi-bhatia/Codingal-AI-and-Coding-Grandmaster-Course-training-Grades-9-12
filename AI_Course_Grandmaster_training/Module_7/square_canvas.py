"""
=======================================================
  PYTHON: DRAW A SQUARE USING TURTLE LIBRARY
=======================================================

WHAT IS TURTLE?
`turtle` is a built-in Python graphics module used for visual 
programming. It provides an on-screen pen ("turtle") that draws 
lines as it moves.

-------------------------------------------------------
1. CORE TURTLE COMMANDS FOR A SQUARE
-------------------------------------------------------
- forward(d) / fd(d) : Move forward by d units
- right(a)   / rt(a) : Turn right by a degrees (90° for square)
- left(a)    / lt(a) : Turn left by a degrees

=======================================================
"""

import turtle

# ============================================================
# 1. STANDARD FOR LOOP (RECOMMENDED & CLEAN)
# ============================================================
print("=" * 60)
print("1. STANDARD FOR LOOP SQUARE")
print("=" * 60)

# Set up screen and turtle
screen = turtle.Screen()
screen.title("Square using Turtle")

t = turtle.Turtle()
t.speed(2)  # Drawing speed (1: slow, 10: fast, 0: instant)

# Draw square: 4 equal sides with 90-degree right turns
for _ in range(4):
    t.forward(100)
    t.right(90)

print("Square drawn successfully!")


# ============================================================
# 2. COMPACT SHORT VERSION (USING ALIASES)
# ============================================================
print("\n" + "=" * 60)
print("2. COMPACT SHORT VERSION")
print("=" * 60)

t2 = turtle.Turtle()
t2.color("red")

# List comprehension one-liner for drawing
[t2.fd(80) or t2.rt(90) for _ in range(4)]


# ============================================================
# 3. REUSABLE FILLED SQUARE FUNCTION
# ============================================================
print("\n" + "=" * 60)
print("3. REUSABLE FILLED SQUARE FUNCTION")
print("=" * 60)

def draw_filled_square(t_obj, size, color):
    t_obj.color(color)
    t_obj.begin_fill()
    for _ in range(4):
        t_obj.fd(size)
        t_obj.rt(90)
    t_obj.end_fill()

t3 = turtle.Turtle()
t3.penup()
t3.goto(-150, 50)  # Move pen without drawing
t3.pendown()

draw_filled_square(t3, size=60, color="blue")


# ============================================================
# 4. QUICK REFERENCE SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("4. QUICK REFERENCE SUMMARY")
print("=" * 60)

summary_table = """
COMMAND              ALIAS       DESCRIPTION
------------------------------------------------------------------
turtle.Turtle()      -           Creates a new turtle object
t.forward(100)       t.fd(100)   Moves forward by 100 pixels
t.right(90)          t.rt(90)    Turns right by 90 degrees
t.color("blue")      -           Sets line/fill color
t.begin_fill()       -           Starts color filling
t.end_fill()         -           Completes color filling
turtle.done()        -           Keeps graphics window open
"""
print(summary_table.strip())

# Keep window open until closed manually
turtle.done()