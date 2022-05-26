# Code to calculate gcd between two numbers
from datetime import datetime


def generic_euclid_gcd(m, n) -> None:
    """
    Euclid's theory is based on the fact that:
        if m = ad and n = bd, then;
            (m-n) = (a-b)d, thus d is also a factor of (a-d)
    :return:
    """
    try:
        st = datetime.now()
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

        print(f"GCD is {ans}, time taken: {datetime.now() - st}")

    except Exception as err:
        print(f"Exception found: {err}")


def optimised_euclid_gcd(m, n) -> None:
    """
    See m as:
        m = qn + r, where q = quotient and r = remainder
    If d divides m and d divides n then r must also be a multiple of d, i.e r = cd

    :return:
    """
    try:
        st = datetime.now()
        ans = 1
        if m < n:
            (m, n) = (n, m)

        while (m % n) >= 0:
            r = m % n
            if r == 0:
                ans = n
                break
            else:
                (m, n) = (n, r)

        print(f"GCD is {ans}, time taken: {datetime.now() - st}")

    except Exception as err:
        print(f"Exception found: {err}")


if __name__ == "__main__":
    m = int(input("Enter First Number - "))
    n = int(input("Enter second number - "))

    generic_euclid_gcd(m, n)
    optimised_euclid_gcd(m, n)
