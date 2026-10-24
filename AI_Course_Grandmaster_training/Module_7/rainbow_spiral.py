"""
=======================================================
  PYTHON: RAINBOW SPIRAL USING TURTLE LIBRARY
=======================================================

WHAT IS A RAINBOW SPIRAL?
A rainbow spiral is created by repeatedly drawing expanding 
line segments while turning at a fixed angle and cycling 
through rainbow colors.

-------------------------------------------------------
1. KEY TECHNIQUES
-------------------------------------------------------
- Color Cycling  : Use list modulus (`colors[x % 6]`) or HSV hue shift
- Expanding Size : Increase forward step distance each iteration
- Angle Offset   : Turn angles (e.g., 59°, 61°, 91°) create spiraling shapes
- Contrast       : Black background makes rainbow colors pop

=======================================================
"""

import turtle
import colorsys

# ============================================================
# 1. HEXAGONAL RAINBOW SPIRAL (LIST OF COLORS)
# ============================================================
print("=" * 60)
print("1. HEXAGONAL RAINBOW SPIRAL")
print("=" * 60)

# Set up screen
screen = turtle.Screen()
screen.title("Rainbow Spiral using Turtle")
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)  # Fastest drawing speed (0)

colors = ["red", "purple", "blue", "green", "orange", "yellow"]

# Draw hexagonal spiral (59° turn creates a spinning 6-sided spiral)
for x in range(120):
    t.pencolor(colors[x % 6])
    t.width(x // 25 + 1)  # Gradually increase pen thickness
    t.forward(x)
    t.left(59)

print("Hexagonal rainbow spiral drawn successfully!")


# ============================================================
# 2. CONTINUOUS GRADIENT RAINBOW SPIRAL (USING HSV)
# ============================================================
print("\n" + "=" * 60)
print("2. CONTINUOUS GRADIENT RAINBOW SPIRAL")
print("=" * 60)

t2 = turtle.Turtle()
t2.speed(0)
t2.penup()
t2.goto(-200, 0)  # Offset position on screen
t2.pendown()

screen.colormode(1.0)  # Standard RGB float mode (0.0 to 1.0)

# Draw continuous hue-shifted spiral (91° turn creates a square spiral)
for i in range(100):
    color = colorsys.hsv_to_rgb(i / 100, 1.0, 1.0)  # Cycle hue from 0.0 to 1.0
    t2.pencolor(color)
    t2.forward(i * 1.5)
    t2.right(91)

print("Gradient rainbow spiral drawn successfully!")


# ============================================================
# 3. QUICK REFERENCE SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("3. QUICK REFERENCE SUMMARY")
print("=" * 60)

summary_table = """
PARAMETER / FUNCTION   VALUE / EXAMPLE              DESCRIPTION
------------------------------------------------------------------
screen.bgcolor()       screen.bgcolor("black")      Sets background color
colorsys.hsv_to_rgb()  hsv_to_rgb(h, s, v)          Generates smooth gradient RGB
t.width()              t.width(x // 25 + 1)         Dynamic line thickness
Angle (59°)            t.left(59)                   6-sided spinning spiral
Angle (91°)            t.right(91)                  4-sided square spiral
t.speed(0)             t.speed(0)                   Disables delay for instant drawing
turtle.done()          -                            Keeps graphics window open
"""
print(summary_table.strip())

# Keep graphics window open
turtle.done()