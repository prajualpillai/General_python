# Code to calculate gcd between two numbers
try:

    m = int(input("Enter First Number - "))
    n = int(input("Enter second number - "))
    ans = 1
    if m < n:
        (m, n) = (n, m)

    while (m % n) != 0:
        diff = m - n
        if n % diff == 0:
            ans = diff
            break
        else:
            (m, n) = (max(diff, n), min(diff, n))

    print(f"GCD is {ans}")

except Exception as err:
    print(f"Exception found: {err}")
