import pytest


class Spiral:
    def __init__(self):
        self.direction = (1, 0)
        self.x = 0
        self.y = 0
        self.steps_since_turn = 0
        self.straight_paths_of_same_lengths = 0
        self.steps_to_turn = 1
        self.number = 1
        self.fields = dict()
        self.total_steps = 0

    def turn(self):
        if self.direction == (1, 0):
            self.direction = (0, 1)
        elif self.direction == (0, 1):
            self.direction = (-1, 0)
        elif self.direction == (-1, 0):
            self.direction = (0, -1)
        elif self.direction == (0, -1):
            self.direction = (1, 0)

        self.steps_since_turn = 0
        self.straight_paths_of_same_lengths += 1
        if self.straight_paths_of_same_lengths == 2:
            self.straight_paths_of_same_lengths = 0
            self.steps_to_turn += 1

    def step(self, number=None):
        self.x += self.direction[0]
        self.y += self.direction[1]
        self.number += 1
        self.steps_since_turn += 1
        self.total_steps += 1

    def should_turn(self):
        return self.steps_since_turn == self.steps_to_turn

    def go_to(self, number):
        while self.number != number:
            self.step()
            if self.should_turn():
                self.turn()

    def clear_memory_to(self, limit):
        number = 0
        while number <= limit:
            number = 0
            for dx, dy in [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]:
                r = (self.x + dx, self.y + dy)
                number += self.fields.get(r, 0)
            if number == 0:
                number = 1
            self.fields[self.x, self.y] = number
            self.step(number)
            if self.should_turn():
                self.turn()
        return number


def distance(index):
    spiral = Spiral()
    spiral.go_to(index)
    return abs(spiral.x) + abs(spiral.y)


def clear_memory(input):
    spiral = Spiral()
    return spiral.clear_memory_to(input)


@pytest.mark.parametrize("index,expected_steps", [
    (1, 0),
    (12, 3),
    (23, 2),
    (1024, 31),
])
def test_distance(index, expected_steps):
    assert expected_steps == distance(index)


@pytest.mark.parametrize("limit,expected_first_number_larger", [
    (0, 1),
    (1, 2),
    (2, 4),
    (4, 5),
    (5, 10),
    (10, 11),
    (11, 23)
])
def test_clear_memory(limit, expected_first_number_larger):
    assert expected_first_number_larger == clear_memory(limit)


def main():
    print('Steps required for %d:' % 289326, distance(289326))
    print('Memory clearing value larger than %d:' % 289326, clear_memory(289326))


if __name__ == '__main__':
    main()