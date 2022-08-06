# Problem 5: Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all the numbers from 1 to n?
import math


def smallest_mult(n):
    factors = []
    for number in range(1, n+1):
        p = 2
        prime_factors = []
        while number >= p ** 2:
            if number % p == 0:
                prime_factors.append(p)
                number = number / p
            else:
                p += 1
        prime_factors.append(int(number))
        for p_factor in prime_factors:
            while factors.count(p_factor) < prime_factors.count(p_factor):
                factors.append(p_factor)
    return math.prod(factors)


def main():
    n = int(input("Enter the final number: "))
    print(f"the smallest positive number that is evenly divisible by all of the numbers"
          f" from 1 to {n} is: {smallest_mult(n)}")


if __name__ == "__main__":
    main()
