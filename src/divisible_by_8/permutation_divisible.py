from itertools import permutations
from collections import defaultdict

def to_int(nums):
    result = 0
    n = len(nums)
    for i in xrange(n):
        result += int(nums[i]) * pow(10, n - i - 1)
    return result


def is_divisible_naive(num):
    """
        Naive implementation that check all possible permutation for num and mod 8, at least O(n^2) solution depending on how python            implements the permutation function, also result in a lot of waste in generating all permutations
    :param num: num with permutations
    :return: true or false
    """
    for perm in permutations(num):
        perm_int = to_int(perm)
        if perm_int % 8 == 0:
            return True
    return False

def _find_digit(digits_discovered, digit_counts, last_digit):
    if last_digit in digits_discovered:
        digits_discovered[last_digit] -= 1
        if digits_discovered[last_digit] < 0:
            return False
    elif last_digit in digit_counts:
        digits_discovered[last_digit] = digit_counts[last_digit] - 1
    else:
        return False
    return True

def _last_three_digits_divisible(divisible_num, digit_counts):
    """
        Check if the digit_counts map contains all the last 3 digits from divisible_num
    :param divisible_num: a number that is divisible by 8
    :param digit_counts:
    :return: true or false
    """

    digits_discovered = defaultdict(int)

    last_digit = divisible_num % 10
    divisible_num /= 10
    second_to_last_digit = divisible_num % 10
    divisible_num /= 10
    third_to_last_digit = divisible_num % 10

    return _find_digit(digits_discovered, digit_counts, last_digit) \
           and _find_digit(digits_discovered, digit_counts, second_to_last_digit) \
           and _find_digit(digits_discovered, digit_counts, third_to_last_digit)


def is_divisible(num):
    """
        Efficient solution realizes on the fact that if last 3 digit of any perm is divisible by 8 then we the entire number is divisible by 8, explanation below.
        The theory is that, let's start with base case to find any number that is divisible by 2, if the last digit is divisible by 2 then the number itself is divisible; extrapolate that to find number divisible by 4, last 2 digits would need to be checked and  divisible by 8 numbers require checking the last 3 digits.
        This is O(n) running time bounded by [104-1000] with interval of +8, and O(n) space for allocating the hashmap
    :param num:
    :return: true or false
    """
    # base cases
    if len(num) <= 0:
        return False
    elif len(num) == 1:
        return int(num) % 8 == 0
    elif len(num) == 2:
        return int(num) % 8 == 0 or int(num[1] + num[0]) % 8 == 0

    digit_counts = defaultdict(int)
    for i in num:
        digit_counts[int(i)] += 1

    # traverse all number with >= 3 digits that is divisible by 8, lower bound is 104 to upper bound 1000
    for divisible_num in xrange(104, 1000, 8):
        if _last_three_digits_divisible(divisible_num, digit_counts):
            return True

    return False


def print_result(numbers, algo):
    for n in numbers:
        print "Permutations of {} is divisible by 8: {}".format(n, algo(n))


if __name__ == "__main__":
    numbers = ["31462708", "75", "1", "0", "401", "123456789111"]
    print "-----Naive-----"
    print_result(numbers, is_divisible_naive)

    print "-----Efficient-----"
    print_result(numbers, is_divisible)
