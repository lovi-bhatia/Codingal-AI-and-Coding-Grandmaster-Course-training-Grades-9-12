"""
=======================================================
  PYTHON: PRIME NUMBERS
=======================================================

WHAT IS A PRIME NUMBER?
A prime number is a natural number greater than 1 that has 
no positive divisors other than 1 and itself (e.g., 2, 3, 5, 7, 11).

-------------------------------------------------------
1. OPTIMIZATION RULE
-------------------------------------------------------
To check if N is prime, you only need to test factors up to √N.
If N has a factor larger than √N, its pair factor must be smaller than √N.

=======================================================
"""

# ============================================================
# 1. OPTIMIZED PRIME CHECKER - O(√N) TIME
# ============================================================
print("=" * 60)
print("1. OPTIMIZED PRIME CHECKER - O(√N) TIME")
print("=" * 60)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = 29
print(f"Is {num} prime? : {is_prime(num)}")


# ============================================================
# 2. ONE-LINER PRIME CHECKER
# ============================================================
print("\n" + "=" * 60)
print("2. ONE-LINER PRIME CHECKER")
print("=" * 60)

# One-line lambda function checking divisibility up to sqrt(n)
is_prime_one_liner = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

print("is_prime_one_liner(17) :", is_prime_one_liner(17))
print("is_prime_one_liner(20) :", is_prime_one_liner(20))


# ============================================================
# 3. GENERATE ALL PRIMES UP TO N
# ============================================================
print("\n" + "=" * 60)
print("3. GENERATE ALL PRIMES UP TO N")
print("=" * 60)

limit = 50

# List comprehension filtering prime numbers
primes = [n for n in range(2, limit + 1) if is_prime(n)]
print(f"Primes up to {limit}:", primes)


# ============================================================
# 4. QUICK REFERENCE SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("4. QUICK REFERENCE SUMMARY")
print("=" * 60)

summary_table = """
APPROACH             CODE EXAMPLE                                   TIME COMPLEXITY
-------------------------------------------------------------------------------------
Standard Loop        for i in range(2, int(n**0.5)+1): ...           O(√N)
One-Liner (all)      n > 1 and all(n % i != 0 for i in range(...))  O(√N)
List Comprehension   [x for x in range(2, N) if is_prime(x)]         O(N√N)
Sieve of Eratosthenes (Best for range up to 10^7)                   O(N log log N)
"""
print(summary_table.strip())