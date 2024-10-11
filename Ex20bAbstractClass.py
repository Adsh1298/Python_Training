from abc import ABC, abstractmethod


class FatherClass(ABC):
    def __init__(self, title):
        self.company = title

    def make_payment(self, mode, amount):
        if mode == 'cash' or mode == 'cheque':
            print(f'A payment of Rs. {amount:.2f} is made through {mode}')
        else:
            print('other mode of payment not accepted')

    @abstractmethod
    def receive_payment(self, mode, amount):
        pass

class SonClass(FatherClass):
    def receive_payment(self, mode, amount):
        if mode == 'cash' or mode == 'upi':
            print(f'A payment of Rs. {amount:.2f} is made through {mode}')
        else:
            print('Other mode of payments not accepted')

    def __init__(self, title):
        super().__init__(title)
        self.company = title

    def make_payment(self, mode, amount):
        if mode == 'cash' or mode == 'upi':
            print(f'A payment of Rs. {amount:.2f} is made through {mode}')
        else:
            print('Cheque payments not accepted')

business = SonClass('SBC Provision')
print(business.company)
business.receive_payment('upi', 6000)