from hw2.BankAccount import SavingsAccount

def test_interest_positive():
    account = SavingsAccount("TestUser", 1000)
    account.deposit(500)
    account.withdraw(100)
    interest = account.apply_interest()

    assert account.get_balance() > 0
    assert interest > 0
# Commit 8
# Commit 14
# Commit 16
# Commit 23
# Commit 51
# Commit 23
# Commit 30
# Commit 33
# Commit 40
# Commit 57
# Commit 64
