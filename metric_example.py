from metric_module.metric import coverage_percent

code = '''
def find_even_not_divisible_by_5(lst):
    result = []
    for num in lst:
        if num % 2 == 0 and num % 5 != 0:
            result.append(num)
    if not result:
        return None
    return result
'''

test = '''
def test_find_even_not_divisible_by_5():
    assert find_even_not_divisible_by_5([10, 20, 30, 40, 50]) is None
    assert find_even_not_divisible_by_5([1, 2, 3, 4, 5]) == [2, 4]
    assert find_even_not_divisible_by_5([6, 12, 18, 24, 30]) == [6, 12, 18, 24]
    assert find_even_not_divisible_by_5([-10, -20, -30, -40, -50]) is None
    assert find_even_not_divisible_by_5([-1, -2, -3, -4, -5]) == [-2, -4]
    assert find_even_not_divisible_by_5([15, 25, 35, 45]) is None
    assert find_even_not_divisible_by_5([0, 1, 2, 3, 4, 5]) == [2, 4]
    assert find_even_not_divisible_by_5([6, 7, 8, 9, 10]) == [6, 8]
    assert find_even_not_divisible_by_5([15, 20, 25, 30, 35]) is None
'''

print(coverage_percent(code, test))
