from pytest import raises
from main import add, subtract, multiply

def test_add():
    val = add(5)
    assert val == 7
    assert isinstance(val, int)
    assert val > 0
    assert val % 2 == 1
    assert val != 10

def test_subtract():
    try:
        subtract(5)
    except NotImplementedError as e:
        assert str(e) == "This function is not yet implemented."
    else:
        assert False, "Expected NotImplementedError was not raised."

def test_subtract_with_raises():
    with raises(NotImplementedError) as exc_info:
        subtract(5)
    assert str(exc_info.value) == "This function is not yet implemented."

def test_multiply(mocker):
    mocker.patch('main.multiply_value', return_value=3)
    val = multiply(4)
    assert val == 12

# def test_multiply_with_spy(mocker):
#     spy = mocker.spy(main, 'multiply_value')
#     val = multiply(4)
#     assert val == 8
#     assert spy.call_count == 1
#     spy.assert_called_once()