# Цель: Создать систему управления банковскими счетами с использованием ООП для моделирования различных типов счетов и операций с ними.
# Шаги для выполнения:
# Определение базового класса BankAccount:
# Атрибуты: owner (владелец счета, строка), __balance (баланс счета, изначально 0, приватный).
# Методы:
# Конструктор __init__(self, owner, balance=0)
# deposit(self, amount): добавляет сумму к балансу, если сумма положительная, иначе выбрасывает ValueError
# withdraw(self, amount): снимает сумму с баланса, если на счету достаточно средств, иначе выбрасывает ValueError
# get_balance(self): возвращает текущий баланс.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError(f"Сумма не достаточна для пополнения баланса.")


    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Сумма для снятия должна быть положительной.")
        if amount <= self.__balance:
            self.__balance-=amount
            print(f"Вывод совершен {amount} успешно совершен. {self.__balance} остаток.")
        else:
            raise ValueError(f"Денег нет, но вы держитесь.")


    def get_balance(self):
        return self.__balance


    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.__balance})"

# Создание класса SavingsAccount (наследуется от BankAccount):
# Дополнительный атрибут: interest_rate (процентная ставка 0.05).
# Метод apply_interest(self): начисляет проценты на остаток по счету.


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate= interest_rate

    def apply_interest(self):
        interest=self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Начислены проценты: {interest:.2f}")
        return interest


# Создание класса CheckingAccount (наследуется от BankAccount):
# Переопределение метода withdraw(self, amount):
# позволяет снимать средства без ограничений по балансу.


class CheckingAccount(BankAccount):
    def __init__(self,owner, balance=0):
        super().__init__(owner,balance)

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError(f"Сумма для снятия должна быть положительной.")

        self._BankAccount__balance -=amount


# После создания структуры необходимо:
# создать экземпляр класса SavingsAccount
# внести депозит 500
# списать с него 100
# применить начисление процентов
# написать тест с использованием pytest, что сумма > 0

account = SavingsAccount("Donold", 1000)
account.deposit(500)
print(account.get_balance())
account.withdraw(100)
print(account.get_balance())
account.apply_interest()
print(account.get_balance())


#test_account.py
from BankAccount import SavingsAccount

def test_interest_positive():
    account = SavingsAccount("TestUser", 1000)
    account.deposit(500)
    account.withdraw(100)
    interest = account.apply_interest()

    assert account.get_balance() > 0
    assert interest > 0# Commit 36
# Commit 37
# Commit 45
# Commit 50
# Commit 59
# Commit 9
# Commit 27
# Commit 50
# Commit 53
# Commit 83
# Commit 85
# Commit 91
