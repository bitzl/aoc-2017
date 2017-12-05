import pytest


def inverse_captcha_part1(code):
    digits = [int(digit) for digit in code]
    repeated_digits = []
    for i in range(len(code)):
        previous = digits[i - 1]
        current = digits[i]
        if previous == current:
            repeated_digits.append(current)
    return sum(repeated_digits)


def inverse_captcha_part2(code):
    digits = [int(digit) for digit in code]
    repeated_digits = []
    offset = int(len(code) / 2)
    for i in range(len(code)):
        previous = digits[i - offset]
        current = digits[i]
        if previous == current:
            repeated_digits.append(current)
    return sum(repeated_digits)


def main():
    with open('input', 'r') as code_file:
        code = code_file.readline().rstrip()
    print('Code:', code)
    print('Answer Part 1:', inverse_captcha_part1(code))
    print('Answer Part 2:', inverse_captcha_part2(code))


@pytest.mark.parametrize("code,expected", [
    ("1122", 3),
    ("1111", 4),
    ("1234", 0),
    ("91212129", 9),
])
def test_inverse_captcha_part1(code, expected):
    assert inverse_captcha_part1(code) == expected, 'Code was %s' % code


@pytest.mark.parametrize("code,expected", [
    ("1212", 6),
    ("1221", 0),
    ("123425", 4),
    ("123123", 12),
    ("12131415", 4),
])
def test_inverse_captcha_part2(code, expected):
    assert inverse_captcha_part2(code) == expected, 'Code was %s' % code


if __name__ == '__main__':
    main()
