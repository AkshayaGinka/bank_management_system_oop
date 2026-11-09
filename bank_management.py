from abc import ABC,abstractmethod


# CLASS 1: CUSTOMER
class Customer:
    def __init__(self,customer_id, name):
        self.customer_id=customer_id
        self.name=name


# CLASS 2: ACCOUNT
class Account:
    def __init__(self,account_number, customer,balance):
        self.account_number = account_number
        self.customer = customer
        self.__balance = balance

    def get_balance(self):
        return self.__balance

 
    def deposit(self, amount):
        if amount <= 0:
            print("Enter a valid amount!")
            return False
        
        self.__balance += amount
        print("Amount Deposited Successfully!")
        return True

    def withdraw(self, amount):

        if amount <= 0:
            print("Enter a valid amount!")
            return False

        if amount > self.__balance:
            print("Insufficient Balance!")
            return False

        self.__balance -= amount
        print("Amount Withdrawn Successfully!")
        return True


    def check_balance(self):

        print("-" * 40)
        print("Account Number:", self.account_number)
        print("Customer Name:", self.customer.name)
        print("Available Balance:", self.__balance)
        print("-" * 40)


# CLASS 3: TRANSACTION


# Abstraction
class Transaction(ABC):
    def __init__(self, account_number, amount):
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.amount = amount
    
    @abstractmethod
    def transaction_details(self):
        pass

# Inheritance and Polymorphism

class Deposit(Transaction):

    def transaction_details(self):
        print("Transaction Type: Deposit")
        print("Account Number:", self.account_number)
        print("Amount:", self.amount)


class Withdrawal(Transaction):

    def transaction_details(self):
        print("Transaction Type: Withdrawal")
        print("Account Number:", self.account_number)
        print("Amount:", self.amount)


# CLASS 4: BANK
class Bank:

    def __init__(self):
        self.customers = []
        self.accounts = []
        self.transactions = []

    # Create Account

    def create_account(self):

        customer_id = int(input("Enter Customer ID: "))

        for c in self.customers:
            if c.customer_id == customer_id:
                print("Customer Already Exists!")
                return

        name = input("Enter Customer Name: ")

        account_number = int(input("Enter Account Number: "))

        for a in self.accounts:
            if a.account_number == account_number:
                print("Account Already Exists!")
                return

        balance = float(input("Enter Initial Balance: "))

        if balance < 0:
            print("Initial Balance Cannot Be Negative!")
            return

        customer = Customer(customer_id, name)

        account = Account(account_number, customer, balance)

        self.customers.append(customer)
        self.accounts.append(account)

        print("Account Created Successfully!")

    # Search Account

    def search_account(self):

        if len(self.accounts) == 0:
            print("No Accounts Available!")
            return None

        account_number = int(input("Enter Account Number: "))

        for a in self.accounts:
            if a.account_number == account_number:
                return a

        print("Account Not Found!")
        return None

    # Deposit Money

    def deposit_money(self):

        account = self.search_account()

        if account is not None:

            amount = float(input("Enter Deposit Amount: "))

            if account.deposit(amount):

                transaction = Deposit(
                    account.account_number, "Deposit", amount
                )

                self.transactions.append(transaction)

                print("Transaction Recorded Successfully!")

    # Withdraw Money

    def withdraw_money(self):

        account = self.search_account()

        if account is not None:

            amount = float(input("Enter Withdrawal Amount: "))

            if account.withdraw(amount):

                transaction = Withdrawal(
                    account.account_number, "Withdrawal", amount
                )

                self.transactions.append(transaction)

                print("Transaction Recorded Successfully!")

    # Check Balance

    def check_balance(self):

        account = self.search_account()

        if account is not None:
            account.check_balance()

    # Transaction History

    def transaction_history(self):

        account = self.search_account()

        if account is None:
            return

        found = False

        print("-" * 45)
        print("TRANSACTION HISTORY")
        print("-" * 45)

        for t in self.transactions:

            if t.account_number == account.account_number:

                # Polymorphism
                t.transaction_details()

                found = True
                print("-" * 45)

        if not found:
            print("No Transactions Found!")

    # View All Accounts

    def view_all_accounts(self):

        if len(self.accounts) == 0:
            print("No Accounts Available!")
            return

        print("-" * 60)
        print("| Account No | Customer ID | Customer Name | Balance |")
        print("-" * 60)

        for a in self.accounts:

            print(
                f"| {a.account_number} | "
                f"{a.customer.customer_id} | "
                f"{a.customer.name} | "
                f"{a.get_balance()} |"
            )

        print("-" * 60)


# MAIN PROGRAM
print("=" * 25)
print("WELCOME TO BANK MANAGEMENT SYSTEM")
print("=" * 25)

bank = Bank()

while True:

    print("\nEnter Options to Perform")

    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. View All Accounts")
    print("7. Exit")

    choice = int(input("Enter Your Choice: "))

    match choice:

        case 1:
            bank.create_account()

        case 2:
            bank.deposit_money()

        case 3:
            bank.withdraw_money()

        case 4:
            bank.check_balance()

        case 5:
            bank.transaction_history()

        case 6:
            bank.view_all_accounts()

        case 7:
            print("THANK YOU, VISIT AGAIN!")
            break

        case _:
            print("Invalid Choice, Try Again!")
