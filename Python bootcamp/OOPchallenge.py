class Account:

        def __init__(self,owner,balance):
                self.owner = owner
                self.balance = balance

        def __str__(self):
                return f"Account owner: {self.owner} \nAccount balance: {self.balance}"

        def deposit(self,amnt):
                self.balance = self.balance + amnt
                print("Deposit Accepted")

        def withdraw(self,amnt):
                new_bal = self.balance - amnt
                if new_bal < 0:
                        print("Funds Unavailable!")
                else:
                        self.balance = new_bal
                        print("Withdrawal Accepted")

def main():
        acct = Account('Jose',100)
        print(acct)
        print(acct.owner)
        print(acct.balance)
        acct.deposit(50)
        acct.withdraw(75)
        acct.withdraw(500)

if __name__ == "__main__":
        main()