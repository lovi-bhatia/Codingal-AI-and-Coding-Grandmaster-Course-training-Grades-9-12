"""
=======================================================
  PYTHON: BMI CALCULATOR (BODY MASS INDEX)
=======================================================

WHAT IS BMI?
Body Mass Index (BMI) is a simple calculation using a person's 
height and weight to estimate body fatness.

FORMULA:
  BMI = weight (kg) / (height (m))²
  or
  BMI = (weight (kg) / (height (cm))²) * 10,000

-------------------------------------------------------
1. WHO BMI CATEGORIES
-------------------------------------------------------
- Underweight : BMI < 18.5
- Normal      : 18.5 <= BMI < 25.0
- Overweight  : 25.0 <= BMI < 30.0
- Obese       : BMI >= 30.0

=======================================================
"""

# ============================================================
# 1. SIMPLE BMI CALCULATOR (CLEAN & SHORT)
# ============================================================
print("=" * 60)
print("1. SIMPLE BMI CALCULATOR")
print("=" * 60)

weight_kg = 70
height_m = 1.75

# Formula: weight / height^2
bmi = weight_kg / (height_m ** 2)

print(f"Weight: {weight_kg} kg | Height: {height_m} m")
print(f"Calculated BMI: {bmi:.2f}")


# ============================================================
# 2. BMI CALCULATOR WITH CATEGORY CLASSIFICATION
# ============================================================
print("\n" + "=" * 60)
print("2. BMI WITH CATEGORY CHECK")
print("=" * 60)

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    score = weight / (height_m ** 2)
    
    if score < 18.5:
        category = "Underweight"
    elif score < 25.0:
        category = "Normal"
    elif score < 30.0:
        category = "Overweight"
    else:
        category = "Obese"
        
    return score, category

score, category = calculate_bmi(70, 175)
print(f"BMI Score: {score:.1f} | Category: {category}")


# ============================================================
# 3. COMPACT ONE-LINER BMI (MINIMAL CODE)
# ============================================================
print("\n" + "=" * 60)
print("3. COMPACT ONE-LINER BMI")
print("=" * 60)

# Lambda function taking weight(kg) and height(cm)
bmi_one_liner = lambda w, h: w / ((h / 100) ** 2)

w, h = 85, 180
val = bmi_one_liner(w, h)
cat = "Underweight" if val < 18.5 else "Normal" if val < 25 else "Overweight" if val < 30 else "Obese"

print(f"{w}kg, {h}cm -> BMI: {val:.2f} ({cat})")


# ============================================================
# 4. QUICK REFERENCE SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("4. QUICK REFERENCE SUMMARY")
print("=" * 60)

summary_table = """
CATEGORY       BMI RANGE        HEALTH RISK
------------------------------------------------------------------
Underweight    < 18.5           Minimal / Malnutrition
Normal         18.5 - 24.9      Low Risk
Overweight     25.0 - 29.9      Increased Risk
Obese          >= 30.0          High Risk
"""
print(summary_table.strip())