import math

print("\n--- Basic Math Functions ---")
print("ceil(2.3):", math.ceil(2.3))  # Smallest integer >= 2.3 → 3
print("floor(2.9):", math.floor(2.9))  # Largest integer <= 2.9 → 2
print("trunc(3.8):", math.trunc(3.8))  # Truncate decimal → 3
print("fabs(-5):", math.fabs(-5))  # Absolute value → 5.0
# Copy sign of -1 to 3 → -3.0 .its copy the sign last element and set it fist element -5,-3=>-5
print("copysign(3, -1):", math.copysign(3, -1))

# Modulo like C → 1.0 simple remainder 20%3=2
print("fmod(10, 3):", math.fmod(10, 3))
# IEEE 754 remainder → 1.0 nearest value
print("remainder(10, 3):", math.remainder(10, 3))  # 20%3=-1

print("\n--- Powers and Logs ---")
print("pow(2, 3):", math.pow(2, 3))  # 2^3 → 8.0
print("sqrt(16.6):", math.sqrt(16.6))  # Square root → 4.0743097574926725
print("exp(1):", math.exp(1))  # e^1 → 2.718...
print("log(10):", math.log(10))  # Natural log → ~2.30
print("log10(1000):", math.log10(1000))  # Base 10 log → 3.0
print("log2(8):", math.log2(8))  # Base 2 log → 3.0
# Break 8 into mantissa and exponent
frexp_result = math.frexp(8)
print("frexp(8):", frexp_result)  # ➜ (0.5, 4), because 0.5 * 2^4 = 8.0

# Rebuild the original number
ldexp_result = math.ldexp(0.5, 4)
print("ldexp(0.5, 4):", ldexp_result)  # ➜ 8.0

print("\n--- Trigonometry ---")
print("sin(pi/2):", math.sin(math.pi/2))  # sin(90°) → 1.0

print("cos(0):", math.cos(0))  # cos(0°) → 1.0
# not correct because we need to covert it radians formet
print("cos(30):", math.cos(30))
angle_rad = math.radians(30)  # Convert to radians
print("cos(30):", math.cos(angle_rad))  # ➜ √3/2 ≈ 0.866
print("cos(30) use pi:", math.cos(math.pi/6))


print("tan(pi/4):", math.tan(math.pi/4))  # tan(45°) → 1.0
print("asin(1):", math.asin(1))  # arcsin(1) → pi/2
print("acos(0):", math.acos(0))  # arccos(0) → pi/2
print("atan(1):", math.atan(1))  # arctan(1) → pi/4
# atan(y/x) quadrant-aware → pi/4 radians
# atan(y/x) quadrant-aware →  0.7853981633974483 radians
print("atan2(1, 1):", math.atan2(1, 1))
# atan(y/x) quadrant-aware → pi/4 degrees
print("atan2(1, 1):", math.degrees(math.atan2(1, 1)))

print("\n--- Angle Conversion ---")

print("radians(180):", math.radians(180))  # Degrees to radians → pi
print("degrees(pi):", math.degrees(math.pi))  # Radians to degrees → 180

print("\n--- Special Functions ---")

print("factorial(5):", math.factorial(5))  # 5! → 120
print("gcd(12, 18):", math.gcd(12, 18))  # Greatest common divisor → 6
# Least common multiple → 36 (Python 3.9+)
print("lcm(12, 18):", math.lcm(12, 18))
print("isqrt(17):", math.isqrt(17))  # Integer square root → 4 (Python 3.8+)
print("comb(5, 2):", math.comb(5, 2))  # Combinations C(5,2) → 10
print("perm(5, 2):", math.perm(5, 2))  # Permutations P(5,2) → 20
print("hypot(3, 4):", math.hypot(3, 4))  # √(3²+4²) → 5.0
print("dist([1, 2], [4, 6]):", math.dist([1, 2], [4, 6]))  # Distance → 5.0
# Compare floating point → True
print("isclose(0.1+0.2, 0.3):", math.isclose(0.1+0.2, 0.3))


print("\n--- Constants ---")
print("pi:", math.pi)  # 3.141592653589793
print("e:", math.e)  # 2.718281828459045
print("tau:", math.tau)  # 6.283185307179586 (2π)
print("inf:", math.inf)  # Infinity
print("nan:", math.nan)  # Not a Number


print("\n--- Floating Point Helpers ---")
print("modf(3.14):", math.modf(3.14))  # Split into (frac, int) → (0.14, 3.0)
print("isnan(nan):", math.isnan(float('nan')))  # Is NaN? → True
print("isinf(inf):", math.isinf(float('inf')))  # Is infinity? → True
print("isfinite(5.0):", math.isfinite(5.0))  # Is finite? → True
print("nextafter(1.0, 2.0):", math.nextafter(1.0, 2.0))  # Smallest float > 1.0
print("nextafter(1.0, 0.0):", math.nextafter(1.0, 0.0))  # Smallest float < 1.0
# Unit in the Last Place for 1.0 ######## i did't understand it
print("ulp(1.0):", math.ulp(1.0))
