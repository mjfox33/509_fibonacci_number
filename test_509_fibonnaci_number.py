from code_509_fibonacci_number import Solution

def test_example_1():
    s = Solution()
    n = 4
    output = 3
    assert s.fib_dp(n) == output

def test_example_2():
    s = Solution()
    n = 10
    output = 55
    assert s.fib_dp(n) == output

def test_example_3():
    s = Solution()
    n = 20
    output = 6765
    assert s.fib_dp(n) == output

def test_example_4():
    s = Solution()
    n = 100
    output = 354224848179261915075
    assert s.fib_dp(n) == output 