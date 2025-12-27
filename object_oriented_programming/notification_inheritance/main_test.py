from main import Notification, EmailNotification, SMSNotification, format_notifications


run_cases = [
    (
        [Notification("Alice")],
        ["Notification for Alice"],
    ),
    (
        [EmailNotification("Bob", "Reset your password")],
        ["Email to Bob: Reset your password"],
    ),
    (
        [
            Notification("Alice"),
            EmailNotification("Bob", "Reset your password"),
            SMSNotification("Cara"),
        ],
        [
            "Notification for Alice",
            "Email to Bob: Reset your password",
            "SMS to Cara: short alert",
        ],
    ),
]

submit_cases = run_cases + [
    (
        [
            SMSNotification("Dave"),
            SMSNotification("Eve"),
        ],
        [
            "SMS to Dave: short alert",
            "SMS to Eve: short alert",
        ],
    ),
    (
        [
            EmailNotification("Frank", "Welcome!"),
            Notification("Grace"),
            SMSNotification("Heidi"),
        ],
        [
            "Email to Frank: Welcome!",
            "Notification for Grace",
            "SMS to Heidi: short alert",
        ],
    ),
    (
        [
            Notification("Ivan"),
            EmailNotification("Judy", "Weekly report"),
            EmailNotification("Karl", "Your order has shipped"),
            SMSNotification("Liam"),
        ],
        [
            "Notification for Ivan",
            "Email to Judy: Weekly report",
            "Email to Karl: Your order has shipped",
            "SMS to Liam: short alert",
        ],
    ),
]


def test(notifications, expected_output):
    print("---------------------------------")
    print("Input notifications:")
    for n in notifications:
        try:
            recipient = n.recipient
        except Exception:
            recipient = "<no recipient attribute>"
        print(f"  - {n.__class__.__name__} to {recipient}")
    print("")

    result = format_notifications(notifications)

    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")

    if result == expected_output:
        print("Pass")
        return True

    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1

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
