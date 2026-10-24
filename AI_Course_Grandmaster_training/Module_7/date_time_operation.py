"""
=======================================================
  PYTHON: DATE & TIME OPERATIONS
=======================================================

WHAT IS DATETIME?
Python's built-in `datetime` module provides efficient 
classes for working with dates, times, formatting, and time deltas.

-------------------------------------------------------
1. CORE CLASSES
-------------------------------------------------------
- datetime.date     : Dates only (Year, Month, Day)
- datetime.time     : Time only (Hour, Minute, Second, Microsecond)
- datetime.datetime : Both Date and Time combined
- datetime.timedelta: Duration / difference between dates or times

=======================================================
"""

from datetime import datetime, date, timedelta

# ============================================================
# 1. GET CURRENT DATE & TIME
# ============================================================
print("=" * 60)
print("1. CURRENT DATE & TIME")
print("=" * 60)

now = datetime.now()
today = date.today()

print("Current Datetime :", now)
print("Current Date     :", today)
print("Components       :", f"{now.year}-{now.month:02d}-{now.day:02d} {now.hour}:{now.minute}")


# ============================================================
# 2. FORMATTING & PARSING (strftime / strptime)
# ============================================================
print("\n" + "=" * 60)
print("2. FORMATTING & PARSING")
print("=" * 60)

# Datetime -> String (strftime)
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Str    :", formatted)

# String -> Datetime (strptime)
date_str = "2026-10-24 15:30:00"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Parsed Datetime  :", parsed_date, "| Type:", type(parsed_date))


# ============================================================
# 3. DATE ARITHMETIC (timedelta)
# ============================================================
print("\n" + "=" * 60)
print("3. DATE ARITHMETIC (timedelta)")
print("=" * 60)

# Adding / Subtracting time
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
past_date = now - timedelta(days=3, hours=5)

print("Tomorrow         :", tomorrow)
print("In 1 Week        :", next_week)

# Difference between two dates
new_year = date(2027, 1, 1)
days_left = (new_year - today).days
print(f"Days to New Year : {days_left} days")


# ============================================================
# 4. UNIX TIMESTAMPS & ISO FORMAT
# ============================================================
print("\n" + "=" * 60)
print("4. UNIX TIMESTAMPS & ISO FORMAT")
print("=" * 60)

# Timestamp conversion
ts = now.timestamp()
dt_from_ts = datetime.fromtimestamp(ts)

print("Unix Timestamp   :", ts)
print("From Timestamp   :", dt_from_ts)
print("ISO 8601 Format  :", now.isoformat())


# ============================================================
# 5. QUICK REFERENCE SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("5. QUICK REFERENCE SUMMARY")
print("=" * 60)

summary_table = """
OPERATION            CODE EXAMPLE                         RESULT
------------------------------------------------------------------
Current Datetime     datetime.now()                       datetime object
Current Date         date.today()                         date object
Format to String     dt.strftime("%Y-%m-%d")              "2026-10-24"
Parse from String    datetime.strptime(s, "%Y-%m-%d")    datetime object
Add/Subtract Time    dt + timedelta(days=7)               datetime object
Date Difference      (d2 - d1).days                       Integer (days)
Unix Timestamp       dt.timestamp()                       Float (seconds)
"""
print(summary_table.strip())