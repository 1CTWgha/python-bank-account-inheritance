class BankAccount():
    def __init__(self):
        self.balance = 0;
        self.interest_rate = 1.02;

    def deposit(self, amount):
        if (amount < 0):
            return False
        else:
            self.balance += amount
            return self.balance

    def withdraw(self, amount):
        if (amount < 0):
            return False
        else:
            self.balance -= amount
            return amount


    def accumulate_interest(self):
        self.balance *= self.interest_rate
        return self.balance


class ChildrensAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.interest_rate = 0;

    def accumulate_interest(self):
        self.balance += 10
        return self.balance


class OverdraftAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.overdraft_penalty = 40

    def withdraw(self, amount):
        if (amount < 0):
            return False
        elif (amount > self.balance):
            self.balance -= self.overdraft_penalty
            return False
        else:
            self.balance -= amount
            return amount

    def accumulate_interest(self):
        if (self.balance >= 0):
            self.balance *= self.interest_rate
            return self.balance

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
