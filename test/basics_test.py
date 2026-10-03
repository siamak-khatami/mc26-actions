# The file to try different synatax of the testing framework
import pytest

def test_example():
    """
    A simple successful test example.
    """
    # assert checks to see if an statement is True. If it is not, the test will fail.
    # So in this example, if 1+1 is not equal to 2, the test will fail.
    # you can try to change it to anything else like 3 to see the test fail.
    assert 1 + 1 == 2

def test_failure_example():
    """
    A simple failing test example.
    """
    # This test is designed to fail. Change the assertion to see the test pass.
    assert 1 + 1 == 2


# Test with parameters
# Sometimes you need to receive files from some test engineers as the test cases. 
# In this light, you can define a parameterized test using the @pytest.mark.parametrize decorator.

@pytest.mark.parametrize("x, y, sum", [
    (1, 1, 2),
    (2, 3, 5),
    (10, 5, 15)
])
def test_sum(x, y, sum):
    """
    First you need a string in the paramter called the paramter string. 
    This is a string in which each parameter is represented by a variable name and devided by commas.
    The order of the variables in this string should match the order of the values in each tuple provided to the decorator.
    Then you can have a list of scnearios per in tuple format corresponsing to the parameters defined in the parameter string.
    For example the first scenario (1, 1, 2) corresponds to x=1, y=1, and sum=2.
    Based on this paramter, this test will run 3 times, once for each tuple of values provided.
    """
    assert x + y == sum, f"Expected {x} + {y} to equal {sum}"


# Fixtures
## Another option in the testing framework is to use fixtures.
# Fixtures are acting like a dependency injection system for your tests.
# This to say, it runs the fixture function before executing the test that depends on it.
# and returns the value to the test function that requested it.

@pytest.fixture
def sample_data():
    return {1: {"name": "Alice"}, 2: {"name": "Bob"}, 3: {"name": "Charlie"}}

def test_using_fixture(sample_data):
    """
    A test that uses the sample_data fixture.
    Sample_data, eventhough referes to the fixture function, is actually a variable holding the
    returned value and data type. A better syntax would be to use a differnt variable name
    like data = sample_data not to confuse the concept of funtion declaration and the actual data being used.
    """
    assert sample_data[1]["name"] == "Alice"
    assert sample_data[2]["name"] == "Bob"
    assert sample_data[3]["name"] == "Charlie"

# mixing fixtures and parameterized tests
@pytest.mark.parametrize("user_id, expected_name", [
    (1, "Alice"),
    (2, "Bob"),
    (3, "Charlie")
])
def test_user_names(sample_data, user_id, expected_name):
    """
    A test that combines fixtures and parameterized tests.
    It checks if the name for a given user_id matches the expected_name.
    """
    assert sample_data[user_id]["name"] == expected_name, f"Expected name for user_id {user_id} to be {expected_name}"


# Expectations and expected failuers
# Sometimes in tests, we are designing scenarios to test whether failuers are working 
# as expected. For exmaple, in a reistration scenario, we might want to test
# The duplicated email scenario. We might expected the system raise an specific error type. 
# In pytest, you can use the pytest.raises context manager to test for expected exceptions.

def test_converting_string_to_int():
    """
    A test that checks if converting a string to an integer works correctly.
    """
    assert int("2") == 2

def test_exception():

    # A general exception
    # This will raise the Exception("An error occurred"),
    # but since it is wrapped in pytest.raises, the test will pass if the exception is raised.
    with pytest.raises(Exception):
        raise Exception("An error occurred")

    # Another example with a specific exception type
    with pytest.raises(ValueError):
        int("This should be an integer")  # This will raise a ValueError

    # ZeroDivisionError example
    with pytest.raises(ZeroDivisionError):
        1 / 0  # This will raise a ZeroDivisionError

    # KeyError example
    with pytest.raises(KeyError):
        d = {"a": 1}
        value = d["b"]  # This will raise a KeyError

    # IndexError example
    with pytest.raises(IndexError):
        lst = [1, 2, 3]
        value = lst[5]  # This will raise an IndexError

    # AttributeError example
    with pytest.raises(AttributeError):
        obj = 42
        obj.non_existent_method()  # This will raise an AttributeError

    # ImportError example
    with pytest.raises(ImportError):
        import non_existent_module  # This will raise an ImportError

    # FileNotFoundError example
    with pytest.raises(FileNotFoundError):
        open("non_existent_file.txt")  # This will raise a FileNotFoundError

    # StopIteration example
    with pytest.raises(StopIteration):
        it = iter([])
        next(it)  # This will raise a StopIteration

    # MemoryError example
    with pytest.raises(MemoryError):
        raise MemoryError("This is a simulated MemoryError")

    # RecursionError example
    with pytest.raises(RecursionError):
        def recursive():
            return recursive()
        recursive()  # This will raise a RecursionError

    # AssertionError example
    with pytest.raises(AssertionError):
        assert False, "This is a simulated AssertionError"

    