from . import display

class Account:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
    def __str__(self):
        return f'account: {self.name} balance: {self.balance}'
    def __float__(self):
        return self.balance
    def __int__(self):
        return int(self.balance)
    def __repr__(self):
        return f'{self.__class__.__name__}({self.balance})'
    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance


def demonstrate():
    account_a = Account('savings', 200.42)
    account_b = Account('checking', 400.42)

    display('str(account_a)', str(account_a))
    display('int(account_a)', int(account_a))
    display('float(account_a)', float(account_a), indent=1)
    display('repr(account_a)', repr(account_a))
    display('account_a > account_b', account_a > account_b, indent=1)
    display('account_a < account_b', account_a < account_b, indent=1)
    display('account_a >= account_b', account_a >= account_b, indent=1)
    display('account_a <= account_b', account_a <= account_b, indent=1)
    display('account_a == account_b', account_a == account_b, indent=1)
    display('account_a != account_b', account_a != account_b, indent=1)


if __name__ == '__main__':
    demonstrate()