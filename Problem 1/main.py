# Problem 1: Multiples of 3 and 5:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,
# 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below the provided parameter value number.

def multiples(number):
    return sum([x for x in range(number) if x % 3 == 0 or x % 5 == 0])


def main():
    number = int(input("Enter a number: "))
    print(f"The sum of al multiples of 3 and 5 up to {number} is: {multiples(number)}")


if __name__ == "__main__":
    main()
