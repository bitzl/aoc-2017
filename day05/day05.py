def read_message(source_file):
    with open(source_file) as source:
        return [int(line) for line in source]


def process_part1(message):
    steps = 0
    index = 0

    # print(index, message)

    while 0 <= index < len(message):
        jump = message[index]
        message[index] += 1
        index += jump
        steps += 1
    return steps


def process_part2(message):
    steps = 0
    index = 0

    # print(index, message)

    while 0 <= index < len(message):
        jump = message[index]
        if message[index] >= 3:
            message[index] -= 1
        else:
            message[index] += 1
        index += jump
        steps += 1

    return steps


def test_process_part1():
    assert 5 == process_part1([0, 3, 0, 1, -3])


def test_process_part2():
    assert 10 == process_part2([0, 3, 0, 1, -3])


def main():
    message = read_message('input')
    print('Jumps to exit (Part 1):', process_part1(message))
    message = read_message('input')
    print('Jumps to exit (Part 2):', process_part2(message))


if __name__ == '__main__':
    main()
