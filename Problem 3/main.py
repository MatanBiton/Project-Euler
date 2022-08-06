# Problem 3: Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the given number?

def largest_prime_factor(number):
    p = 2
    prime_factors = []
    while number >= p ** 2:
        if number % p == 0:
            prime_factors.append(p)
            number = number / p
        else:
            p += 1
    prime_factors.append(int(number))
    return max(prime_factors)


def main():
    number = int(input("enter a number: "))
    print(f"The largest prime factor of {number} is: {largest_prime_factor(number)}")


if __name__ == "__main__":
    main()
