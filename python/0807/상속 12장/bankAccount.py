class BankAccount:
    def __init__(self, name, number, balance):
        self.balance = balance
        self.name = name
        self.number = number
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance

class CheckingAccount(BankAccount):
    def __init__(self, name, number, balance):
        super().__init__(name, number, balance)
        self.withdraw_charge = 10000  #수표 발행 수수료 
    def withdraw(self, amount):
        return BankAccount.withdraw(self,amount+self.withdraw_charge)
    
class SavingAccount(BankAccount):
    def __init__(self,name, number, balance,interest_rate):
        super().__init__(name, number, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        return BankAccount.deposit(self, self.balance*self.interest_rate)
    
a1 =SavingAccount("홍길도", 123456, 10000, 0.05)
a1.add_interest()
print("저축에금 금액읜 잔액 = ", a1.balance)
a2 = CheckingAccount("김철수", 123457, 20000000)
a2.withdraw(100000)
print("당좌예금의 잔액 =", a2.balance)