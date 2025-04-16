from main import get_weather, divide, is_prime
import pytest

def test_get_weather():
    assert get_weather(21) == 'hot'

def test_cold_get_weather():
    assert get_weather(15) == 'cold'

def test_divide():
    assert divide(4, 2) == 2
    
    ErrorHandle(ValueError, 'It is not possible divide for zero.', divide, 4, 0)

def ErrorHandle(error_type, message, function, *args):
    with pytest.raises(error_type, match=message):
        function(*args)

@pytest.mark.parametrize('num, expected', [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (13, True),
    (14, False),
    (15, False),
    (17, True),
])
def test_is_prime(num, expected):
    assert is_prime(num) == expected