from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self, id, name, initial_amount):
        self.account_no = id
        self.account_name = name
        self.balance = initial_amount
    @abstractmethod
    def calc_interest(self):
        pass

class SBAccount(Account):
    def __init__(self, id, name, initialAmount):
        super().__init__(id, name, initialAmount)

    def calc_interest(self):
        print('Calc interested implemented here')

acc = SBAccount(123, 'Phaniraj', 5000)


