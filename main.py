class BankAccount:
    accounts=[]
    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate=int_rate
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance+= amount
        return self
    def withdraw(self, amount):
        if amount<= self.balance:
            self.balance-= amount
        else :
            print("Fonds insuffisants : frais de 5 $ facturés")
            self.balance-=5
        return self
    def display_account_info(self):
        return f"{self.balance}"
    def yield_interest(self):
        if self.balance>0 :
            self.balance*=self.int_rate
        return self
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()
class User:
    def __init__(self,name):
        self.name = name
        self.account = {
                    "compte_1":BankAccount(0.03,1000),
                    "compte_2":BankAccount(0.01,3000)
                        } 
   
    def display_user_balance(self):
        print(f"User: {self.name}, compte_1 Balance: {self.account['compte_1'].display_account_info()}")
        print(f"User: {self.name}, compte_2 Balance: {self.account['compte_2'].display_account_info()}")
        return self
    def transfer_money(self, amount,user):
        self.account_balance-=amount
        user.account_balance+=amount
        self.display_user_balance()
        user.display_user_balance()
        return self
    
adrien = User("Adrien")

adrien.account['compte_1'].deposit(100)
adrien.display_user_balance()
