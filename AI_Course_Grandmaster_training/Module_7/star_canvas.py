"""
=======================================================
  PYTHON: DRAW A STAR USING TURTLE LIBRARY
=======================================================

DRAWING A 5-POINTED STAR:
A standard 5-pointed star is drawn by moving forward and 
turning 144 degrees at each vertex, repeated 5 times.

-------------------------------------------------------
1. GEOMETRY OF A 5-POINTED STAR
-------------------------------------------------------
- Total Rotation : 720 degrees (2 full turns: 2 * 360°)
- Turn Angle     : 720° / 5 = 144°
- Number of Sides: 5 equal straight lines

=======================================================
"""

import turtle

# ============================================================
# 1. STANDARD FOR LOOP (RECOMMENDED & CLEAN)
# ============================================================
print("=" * 60)
print("1. STANDARD FOR LOOP STAR")
print("=" * 60)

# Set up screen and turtle
screen = turtle.Screen()
screen.title("Star using Turtle")

t = turtle.Turtle()
t.speed(3)  # Speed: 1 (slow) to 10 (fast), 0 (instant)

# Draw 5-pointed star: 5 lines with 144-degree right turns
for _ in range(5):
    t.forward(100)
    t.right(144)

print("Star drawn successfully!")


# ============================================================
# 2. COMPACT SHORT VERSION (USING ALIASES)
# ============================================================
print("\n" + "=" * 60)
print("2. COMPACT SHORT VERSION")
print("=" * 60)

t2 = turtle.Turtle()
t2.color("orange")

# List comprehension one-liner for drawing
[t2.fd(80) or t2.rt(144) for _ in range(5)]


# ============================================================
# 3. REUSABLE FILLED STAR FUNCTION
# ============================================================
print("\n" + "=" * 60)
print("3. REUSABLE FILLED STAR FUNCTION")
print("=" * 60)

def draw_filled_star(t_obj, size, color):
    t_obj.color(color)
    t_obj.begin_fill()
    for _ in range(5):
        t_obj.fd(size)
        t_obj.rt(144)
    t_obj.end_fill()

t3 = turtle.Turtle()
t3.penup()
t3.goto(-150, 50)  # Move pen without drawing
t3.pendown()

draw_filled_star(t3, size=70, color="gold")


# ============================================================
# 4. QUICK REFERENCE SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("4. QUICK REFERENCE SUMMARY")
print("=" * 60)

summary_table = """
PARAMETER / COMMAND  VALUE / ALIAS  DESCRIPTION
------------------------------------------------------------------
Sides / Points       5              Standard 5-pointed star
Turn Angle           144 degrees    720° total turn / 5 vertices
t.forward(100)       t.fd(100)      Draws star line of length 100
t.right(144)         t.rt(144)      Rotates pen clockwise by 144°
t.begin_fill()       -              Starts filling shape with color
t.end_fill()         -              Completes color filling
turtle.done()        -              Keeps graphics window open
"""
print(summary_table.strip())

# Keep window open until closed manually
turtle.done()