"""
=======================================================
  PYTHON: STRING OPERATIONS & METHODS
=======================================================

WHAT ARE STRING OPERATIONS?
Strings in Python are immutable sequences of Unicode characters.
Python provides a rich set of built-in operations and methods 
for manipulating, slicing, formatting, and inspecting text data.

-------------------------------------------------------
1. KEY STRING CONCEPTS
-------------------------------------------------------
- Immutability   : Strings cannot be modified in place; string methods
                   always return a new string.
- Indexing       : Zero-based indexing (`s[0]`), supports negative indices (`s[-1]`).
- Slicing Syntax : `sequence[start : stop : step]`
- Escape Sequences: `\n` (newline), `\t` (tab), `\\` (backslash), `\"` (quote)

-------------------------------------------------------
2. COMMON STRING METHOD CATEGORIES
-------------------------------------------------------
- Case Conversion : upper(), lower(), title(), capitalize(), swapcase()
- Searching       : find(), index(), count(), startswith(), endswith()
- Modification    : replace(), strip(), lstrip(), rstrip()
- Splitting/Join  : split(), rsplit(), splitlines(), join()
- Inspection      : isalpha(), isdigit(), isalnum(), isspace(), islower()

Memory Trick:
  s[start:stop:step]  -> stop index is EXCLUDED (up to, but not including)
  'delimiter'.join(L) -> Joins list L into a single string
  s.strip()           -> Trims whitespace from BOTH ends

=======================================================
"""

# ============================================================
# 1. STRING INDEXING & SLICING
# ============================================================
print("=" * 60)
print("1. STRING INDEXING & SLICING")
print("=" * 60)

text = "Python Programming"

print("Original Text:", text)
print("First character (text[0])   :", text[0])
print("Last character (text[-1])   :", text[-1])

# Slicing [start:stop:step]
print("Slice [0:6]                 :", text[0:6])       # 'Python'
print("Slice [7:]                  :", text[7:])        # 'Programming'
print("Slice [:6]                  :", text[:6])        # 'Python'
print("Slice [::2] (every 2nd char):", text[::2])       # 'Pto ~'
print("Reversed string [::-1]      :", text[::-1])      # 'gnimmargorP nohtyP'


# ============================================================
# 2. STRING CONCATENATION & REPETITION
# ============================================================
print("\n" + "=" * 60)
print("2. STRING CONCATENATION & REPETITION")
print("=" * 60)

first_name = "Guido"
last_name = "van Rossum"

# Concatenation (+)
full_name = first_name + " " + last_name
print("Concatenation (+) :", full_name)

# Repetition (*)
banner = "-" * 30
print("Repetition (*)    :", banner)

# Efficient Joining (.join())
words = ["Python", "is", "awesome"]
joined_str = " ".join(words)
print("Joining List      :", joined_str)


# ============================================================
# 3. CASE CONVERSION & MODIFICATION
# ============================================================
print("\n" + "=" * 60)
print("3. CASE CONVERSION & MODIFICATION")
print("=" * 60)

sample = "hElLo, PyThOn WOrlD!"

print("Original    :", sample)
print("upper()     :", sample.upper())
print("lower()     :", sample.lower())
print("title()     :", sample.title())
print("capitalize():", sample.capitalize())
print("swapcase()  :", sample.swapcase())


# ============================================================
# 4. SEARCHING & COUNTING
# ============================================================
print("\n" + "=" * 60)
print("4. SEARCHING & COUNTING")
print("=" * 60)

quote = "To be or not to be, that is the question."

print("quote:", quote)
print("count('be')        :", quote.count("be"))
print("find('to')         :", quote.find("to"))        # Index of first occurrence (case-sensitive)
print("rfind('be')        :", quote.rfind("be"))       # Index of last occurrence
print("startswith('To')   :", quote.startswith("To"))
print("endswith('question.'):", quote.endswith("question."))

# find() vs index()
print("find() missing item:", quote.find("python"))    # Returns -1
# quote.index("python")  # Raises ValueError if not found


# ============================================================
# 5. STRIPPING, REPLACING & SPLITTING
# ============================================================
print("\n" + "=" * 60)
print("5. STRIPPING, REPLACING & SPLITTING")
print("=" * 60)

# Stripping Whitespace / Characters
padded = "  ---Data Science---  "
print("Padded String      :", repr(padded))
print("strip()            :", repr(padded.strip()))
print("lstrip()           :", repr(padded.lstrip()))
print("rstrip()           :", repr(padded.rstrip()))
print("strip(' -')        :", repr(padded.strip(" -")))

# Replacing
raw_text = "I like Java. Java is cool."
updated = raw_text.replace("Java", "Python")
print("replace()          :", updated)

# Splitting
data_line = "apple,banana,cherry,date"
fruit_list = data_line.split(",")
print("split(',')         :", fruit_list)


# ============================================================
# 6. INSPECTION & VALIDATION METHODS
# ============================================================
print("\n" + "=" * 60)
print("6. INSPECTION & VALIDATION METHODS")
print("=" * 60)

# All inspection methods return boolean (True / False)
print("'Python'.isalpha()   :", "Python".isalpha())    # Letters only
print("'12345'.isdigit()    :", "12345".isdigit())     # Digits only
print("'Py3000'.isalnum()   :", "Py3000".isalnum())    # Alphanumeric
print("'   '.isspace()      :", "   ".isspace())       # Whitespace only
print("'hello'.islower()    :", "hello".islower())     # Lowercase check
print("'HELLO'.isupper()    :", "HELLO".isupper())     # Uppercase check


# ============================================================
# 7. FORMATTED STRINGS (F-STRINGS & FORMAT)
# ============================================================
print("\n" + "=" * 60)
print("7. FORMATTED STRINGS")
print("=" * 60)

item = "Laptop"
price = 1299.9876
quantity = 3

# F-Strings (Python 3.6+)
f_string = f"Item: {item} | Total: ${price * quantity:.2f}"
print("F-String           :", f_string)

# str.format() method
formatted = "Item: {} | Total: ${:.2f}".format(item, price * quantity)
print("str.format()       :", formatted)

# Aligning and Padding in F-Strings
print(f"Left Aligned   : |{item:<15}|")
print(f"Right Aligned  : |{item:>15}|")
print(f"Centered       : |{item:^15}|")


# ============================================================
# 8. QUICK REFERENCE SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("8. QUICK REFERENCE SUMMARY")
print("=" * 60)

summary_table = """
METHOD         EXAMPLE                     DESCRIPTION
------------------------------------------------------------------
s[a:b]         "Python"[0:2] -> "Py"       Slice from index a to b-1
s[::-1]        "abc"[::-1] -> "cba"        Reverse a string
s.upper()      "a".upper() -> "A"          Convert to uppercase
s.lower()      "A".lower() -> "a"          Convert to lowercase
s.strip()      " x ".strip() -> "x"        Remove leading/trailing whitespace
s.replace()    "a".replace("a","b") -> "b" Replace substring
s.split(sep)   "a,b".split(",") -> ['a','b'] Split string into list
s.join(seq)    "-".join(['a','b']) -> "a-b" Join iterable elements
s.find(sub)    "abc".find("b") -> 1        Find index (-1 if missing)
s.isdigit()    "123".isdigit() -> True     Check if all chars are digits
"""
print(summary_table.strip())