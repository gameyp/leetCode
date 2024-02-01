from leetcode import is_palindrome, fibonacci

def test_is_palindrome_true():
    assert is_palindrome("racecar") is True
    # Add more test cases for True scenarios

def test_is_palindrome_false():
    assert is_palindrome("hello") is False
    # Add more test cases for False scenarios

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(6) == 8
    # Add more test cases for different Fibonacci numbers
