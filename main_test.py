from main import apply_transforms


def add_one(x):
    return x + 1


def double(x):
    return x * 2


def square(x):
    return x * x


def cap_at_50(x):
    if x > 50:
        return 50
    return x


run_cases = [
    # Simple pipeline: add_one then double
    ([1, 2, 3], [add_one, double], [4, 6, 8]),
    # No transformers: copy input
    ([5, 10, 15], [], [5, 10, 15]),
    # Empty numbers list
    ([], [add_one, double], []),
]

submit_cases = run_cases + [
    # Mix of named functions and lambdas
    (
        [3, 4],
        [add_one, square, lambda x: x - 2],
        [14, 23],
    ),
    # Capping values
    (
        [10, 30, 100],
        [double, add_one, cap_at_50],
        [21, 50, 50],
    ),
]


def test(numbers, transformers, expected_output):
    print("---------------------------------")
    print(f"Input numbers:       {numbers}")
    print(f"Number of transforms: {len(transformers)}")
    result = apply_transforms(numbers, transformers)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
