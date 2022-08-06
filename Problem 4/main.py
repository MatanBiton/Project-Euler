# Problem 4: Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two n-digit numbers.

def largest_palindrome_product(n):
    max_pal = 0
    for i in range(1, 10 ** n):
        for j in range(1, 10 ** n):
            num = str(i * j)
            if num == num[::-1]:
                max_pal = int(num) if int(num) > max_pal else max_pal

    return max_pal


def main():
    n = int(input("Enter the number of digits: "))
    print(f"the largest palindrome made from the product of two {n}-digit numbers is:\n{largest_palindrome_product(n)}")


if __name__ == "__main__":
    main()
