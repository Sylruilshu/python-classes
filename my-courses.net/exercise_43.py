
class BankAccount():

    def __init__(self, account_num, name, balance):
        self.account_num = account_num
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdrawal(self, amount):
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount

    def bank_fees(self):
        fee = self.balance * 0.05
        self.balance = self.balance - fee
    
    def display(self):
        return f"Account number: {self.account_num} \nName: {self.name} \nBalance: ${self.balance}"


bank = BankAccount(7, "Bar", 500)

bank.deposit(50)
bank.deposit(0)
bank.deposit(200)

bank.withdrawal(200)

bank.bank_fees()

print(bank.display())