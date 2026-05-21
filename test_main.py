from main import add, multiply


def test_add_correct():
    assert add(2, 3) == 5


def test_add_intentionally_wrong():
    # ABSICHTLICHER FEHLER: 1 + 1 = 2, nicht 3
    assert add(1, 1) == 3


def test_multiply_correct():
    assert multiply(3, 4) == 12


def test_multiply_intentionally_wrong():
    # ABSICHTLICHER FEHLER: 2 * 5 = 10, nicht 99
    assert multiply(2, 5) == 99
