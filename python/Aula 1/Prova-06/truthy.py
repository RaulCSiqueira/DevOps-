class Account:
    def __init__(self, name, active=True):
        self.name = name
        self.active = active

class Accounts:
    def __init__(self, *accounts):
        self.accs = list(accounts)
    def __len__(self):
        print('called the __len__ method.')
        return len(self.accs)
    def __bool__(self):
        print('called the __bool__ method.')
        return any(a for a in self.accs if a.active)

def demonstrate():
    accs = Accounts(
        Account('primary'),
        Account('secondary', False),
    )

    print(f'accs is {bool(accs)}')
    print(f'accs contains {len(accs)} accounts')
    if accs:
        print('at least one account is active')

if __name__ == '__main__':
    demonstrate()