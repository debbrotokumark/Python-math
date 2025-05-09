import math

def show_menu():
    print("\n=== Scientific Calculator ===")
    print("1. Square root")
    print("2. Power")
    print("3. Factorial")
    print("4. Trigonometry (sin, cos, tan)")
    print("5. Logarithm (log, log10)")
    print("6. GCD & LCM")
    print("7. Combinations / Permutations")
    print("8. Hypotenuse (Pythagorean)")
    print("9. Distance between 2D points")
    print("0. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose option: ")

        if choice == "1":
            x = float(input("Enter number: "))
            print("√", x, "=", math.sqrt(x))

        elif choice == "2":
            base = float(input("Base: "))
            exp = float(input("Exponent: "))
            print(f"{base}^{exp} =", math.pow(base, exp))

        elif choice == "3":
            n = int(input("Enter a non-negative integer: "))
            print(f"{n}! =", math.factorial(n))

        elif choice == "4":
            angle = float(input("Enter angle (degrees): "))
            rad = math.radians(angle)
            print(f"sin({angle}) = {math.sin(rad)}")
            print(f"cos({angle}) = {math.cos(rad)}")
            print(f"tan({angle}) = {math.tan(rad)}")

        elif choice == "5":
            x = float(input("Enter number: "))
            print(f"log({x}) =", math.log(x))
            print(f"log10({x}) =", math.log10(x))

        elif choice == "6":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(f"GCD({a}, {b}) =", math.gcd(a, b))
            print(f"LCM({a}, {b}) =", math.lcm(a, b))

        elif choice == "7":
            n = int(input("Enter n: "))
            r = int(input("Enter r: "))
            print(f"Combinations C({n},{r}) =", math.comb(n, r))
            print(f"Permutations P({n},{r}) =", math.perm(n, r))

        elif choice == "8":
            a = float(input("Side A: "))
            b = float(input("Side B: "))
            print(f"Hypotenuse = {math.hypot(a, b)}")

        elif choice == "9":
            x1, y1 = map(float, input("Point 1 (x y): ").split())
            x2, y2 = map(float, input("Point 2 (x y): ").split())
            print(f"Distance = {math.dist([x1, y1], [x2, y2])}")

        elif choice == "0":
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

