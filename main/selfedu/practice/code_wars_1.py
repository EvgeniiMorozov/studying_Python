# Task_1
# Write a function that takes an integer as input, and returns the number of bits that are equal to one in
# the binary representation of that number. You can guarantee that input is non-negative.
#
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def count_bits(n: int):
    result = []
    while n:
        result.append(n % 2)
        n //= 2

    result.reverse()
    result = [str(el) for el in result]
    return int(''.join(result))


def main():
    # Task_1
    print(count_bits(1234))


if __name__ == '__main__':
    main()
