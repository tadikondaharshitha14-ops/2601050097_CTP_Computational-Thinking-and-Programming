from app import add, multiply


def test_add() -> None:
    assert add(10, 20) == 30


def test_multiply() -> None:
    assert multiply(10, 20) == 200