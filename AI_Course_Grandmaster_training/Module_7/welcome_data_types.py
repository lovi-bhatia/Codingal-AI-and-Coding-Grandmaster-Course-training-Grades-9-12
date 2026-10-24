"""
=======================================================
  PYTHON: WELCOME TO PROGRAMMING & DATA TYPES
=======================================================

WHAT IS PYTHON?
Python is an interpreted, high-level, general-purpose programming 
language. It is designed for readability and simplicity, using 
clean syntax and significant whitespace (indentation) instead of 
curly braces or semicolons.

-------------------------------------------------------
1. CORE SYNTAX RULES
-------------------------------------------------------
- Indentation: Python uses indentation (4 spaces) to define code blocks.
- No Semicolons: Statements terminate at the end of the line.
- Case-Sensitive: `total`, `Total`, and `TOTAL` are three different identifiers.
- Dynamic Typing: Variable types are inferred automatically at runtime.

-------------------------------------------------------
2. BUILT-IN DATA TYPES
-------------------------------------------------------
A. NUMERIC TYPES:
   - int     : Whole numbers of arbitrary precision (e.g., 10, -500, 0)
   - float   : Real numbers with decimal points (e.g., 3.14, -0.01)
   - complex : Numbers with real and imaginary parts (e.g., 3 + 4j)

B. TEXT TYPE:
   - str     : Immutable sequence of characters ('text', "text", '''multiline''')

C. BOOLEAN TYPE:
   - bool    : Logical values: True or False (must be capitalized)

D. SEQUENCE TYPES:
   - list    : Ordered, mutable collection: [1, 2, 3]
   - tuple   : Ordered, immutable collection: (1, 2, 3)
   - range   : Immutable sequence of numbers: range(0, 10)

E. MAPPING TYPE:
   - dict    : Key-value pairs: {"key": "value"}

F. SET TYPES:
   - set     : Unordered collection of unique items: {1, 2, 3}
   - frozenset: Immutable version of a set

G. NULL TYPE:
   - NoneType: Represents absence of value (None)

-------------------------------------------------------
3. TYPE CHECKING & CONVERSION
-------------------------------------------------------
- type(x)        : Returns the type of x.
- isinstance(x, T): Returns True if x is an instance of type T.
- int(x), float(x), str(x), bool(x), list(x), tuple(x), set(x)

Memory Trick:
  list  = []  -> Changeable (mutable)
  tuple = ()  -> Locked (immutable)
  dict  = {}  -> Key: Value mappings
  set   = {}  -> Unique values only
  bool  = True / False (always Capitalized)

=======================================================
"""

# ============================================================
# 1. FIRST PROGRAM & COMMENTS
# ============================================================
print("=" * 60)
print("1. FIRST PROGRAM & COMMENTS")
print("=" * 60)

# Single-line comment starts with a hash symbol

"""
Multi-line comment or docstring
written using triple quotes.
"""

# Standard output
print("Hello, World!")

# Custom separators and endings
print("Python", "is", "readable", sep="-")
print("First line", end=" | ")
print("Second line on same output")


# ============================================================
# 2. NUMERIC DATA TYPES (int, float, complex)
# ============================================================
print("\n" + "=" * 60)
print("2. NUMERIC DATA TYPES")
print("=" * 60)

item_count = 42          # int
unit_price = 19.99       # float
coordinates = 3 + 4j     # complex

print("item_count :", item_count, "| Type:", type(item_count))
print("unit_price :", unit_price, "| Type:", type(unit_price))
print("coordinates:", coordinates, "| Type:", type(coordinates))

# Arithmetic operations
print("Float Division (/) :", 10 / 3)   # Always returns float
print("Floor Division (//):", 10 // 3)  # Drops decimal remainder
print("Modulus (%)        :", 10 % 3)   # Returns remainder
print("Exponentiation (**):", 2 ** 4)   # 2 to the power 4


# ============================================================
# 3. TEXT & BOOLEAN TYPES (str, bool)
# ============================================================
print("\n" + "=" * 60)
print("3. TEXT & BOOLEAN TYPES")
print("=" * 60)

username = "Alex"
course_name = 'Python Fundamentals'
is_active = True
has_passed = False

# Formatted strings (f-strings)
summary = f"User: {username} | Course: {course_name} | Active: {is_active}"
print(summary)

# Booleans in comparisons
print("10 > 5   :", 10 > 5)
print("Type check:", type(is_active))


# ============================================================
# 4. COLLECTION DATA TYPES (list, tuple, dict, set)
# ============================================================
print("\n" + "=" * 60)
print("4. COLLECTION DATA TYPES")
print("=" * 60)

# List (mutable, ordered)
skills = ["Python", "SQL", "Git"]
skills.append("Docker")
skills[0] = "Python 3"

# Tuple (immutable, ordered)
screen_dimensions = (1920, 1080)

# Dictionary (key-value mapping)
student_profile = {
    "name": "Sarah",
    "id": 1042,
    "enrolled": True
}

# Set (unique elements, unordered)
unique_numbers = {1, 2, 2, 3, 4, 4, 4}  # Duplicates automatically discarded

print("List (skills)       :", skills)
print("Tuple (dimensions)  :", screen_dimensions)
print("Dict (student name) :", student_profile["name"])
print("Set (unique values) :", unique_numbers)


# ============================================================
# 5. THE None TYPE (NoneType)
# ============================================================
print("\n" + "=" * 60)
print("5. THE None TYPE")
print("=" * 60)

database_connection = None

print("Value:", database_connection)
print("Type :", type(database_connection))

# Identity check using 'is'
if database_connection is None:
    print("Connection status: Not connected.")


# ============================================================
# 6. TYPE CHECKING & CONVERSION (CASTING)
# ============================================================
print("\n" + "=" * 60)
print("6. TYPE CHECKING & CONVERSION")
print("=" * 60)

# Type conversions
raw_input = "250"
converted_int = int(raw_input)
converted_float = float(raw_input)

print("Original str   :", raw_input, type(raw_input))
print("Converted int  :", converted_int, type(converted_int))
print("Converted float:", converted_float, type(converted_float))

# Truthy and Falsy evaluations
print("bool(0)    :", bool(0))        # False
print("bool(1)    :", bool(1))        # True
print("bool('')   :", bool(""))       # False (empty string)
print("bool('abc'):", bool("abc"))    # True (non-empty string)
print("bool([])   :", bool([]))       # False (empty list)
print("bool([1])  :", bool([1]))      # True (non-empty list)

# isinstance checks
print("Is 50 an int?        :", isinstance(50, int))
print("Is 'text' a str?     :", isinstance("text", str))
print("Is 3.14 an int/float?:", isinstance(3.14, (int, float)))


# ============================================================
# 7. QUICK REFERENCE SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("7. QUICK REFERENCE SUMMARY")
print("=" * 60)

summary_table = """
TYPE       SYNTAX EXAMPLE          MUTABLE?    DESCRIPTION
------------------------------------------------------------------
int        x = 10                  No          Whole integers
float      x = 3.14                No          Decimal numbers
str        x = "text"              No          Text sequence
bool       x = True                No          Boolean True / False
list       x = [1, 2, 3]           Yes         Ordered changeable list
tuple      x = (1, 2, 3)           No          Ordered unchangeable list
dict       x = {"k": "v"}          Yes         Key-value mappings
set        x = {1, 2, 3}           Yes         Unordered unique elements
NoneType   x = None                No          Absence of value
"""
print(summary_table.strip())