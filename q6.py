import typing as t
import sqlite3
import random
import time


class Bank:
    """The main bank class"""

    def __init__(self):
        pass

    @property
    def name(self) -> str:
        return "Orientel Bank of BITS"
    
    def add_account(self, name: str) -> "Account":
        """Adds an account to the database."""
        acc_no = random.randint(10**5, 10**6 - 1)
        cur.execute("INSERT INTO users VALUES (?, ?, ?)", (acc_no, name, 0,))
        con.commit()
        return Account(acc_no)
    
    def get_account(self, id: int) -> t.Union["Account", None]:
        """Gets an account from the database."""
        cur.execute("SELECT * FROM users WHERE id = ?", (id,))
        acc = cur.fetchone()
        if not acc:
            print("\nAccount not found.")
            return None
        
        return Account(id)
    
    def transfer_funds(self, account1: "Account", account2: "Account", amount: int):
        """Transfers funds from `account1` to `account2`."""
        if account1.balance < money:
            print("\nInsufficient Funds!")
            return False
        
        a = account1.remove_money(amount)
        b = account2.add_money(amount)

        return (a and b)


class Account:
    """A bank account."""

    def __init__(self, account_number: int):
        self._id = account_number
        cur.execute("SELECT name, balance FROM users WHERE id = ?", (account_number,))
        self._name, self._balance = cur.fetchone()
    
    @property
    def id(self) -> int:
        return self._id

    @property
    def account_number(self) -> int:
        return self.id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def balance(self) -> int:
        return self._balance
    
    def add_money(self, money: int) -> bool:
        """Deposit money to the account."""
        if (money <= 0):
            print("\nCannot add 0 or negative money!")
            return False
        
        cur.execute("UPDATE users SET balance = ? WHERE id = ?", (self.balance + money, self.id,))
        self._balance += money
        return True
    

    def remove_money(self, money: int) -> bool:
        """Withdraw money from the account."""
        if (self.balance < money):
            print("\nInsufficient balance!")
            return False
        
        cur.execute("UPDATE users SET balance = ? WHERE id = ?", (self.balance - money, self.id,))
        self._balance -= money
        return True

    
    def show_summary(self):
        """Prints the name, account number and balance of the account."""
        print("="*30)
        print("Name:", self.name)
        print("Account No.:", self.id)
        print(f"Balance: Rs. {self.balance}/-")
        print("="*30)

def show_options():
    time.sleep(1)
    print("""
Choose:
(1) Create Account
(2) Deposit Money
(3) Withdraw Money
(4) Account Summary
(5) Transfer Money
(6) Exit
""")

if __name__ == "__main__":
    con = sqlite3.connect("bank.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
                id integer primary key,
                name varchar,
                balance integer
                )""")
    bank = Bank()
    print(f"\n\nWelcome to {bank.name}!")
    while True:
        show_options()
        inp = int(input("Enter your choice: "))

        if inp == 1:
            name = input("Enter your name: ")
            if name == "":
                print("Invalid name!")
            else:
                acc = bank.add_account(name)
                print("\nAccount created successfully!")
                acc.show_summary()

        elif inp == 2:
            acc_no = int(input("Enter Account Number: "))
            acc = bank.get_account(acc_no)
            if not acc:
                continue
            
            money = int(input("Enter money to deposit: "))
            if acc.add_money(money):
                print("\nMoney deposited!")


        elif inp == 3:
            acc_no = int(input("Enter Account Number: "))
            acc = bank.get_account(acc_no)
            if not acc:
                continue
            
            money = int(input("Enter money to withdraw: "))
            if acc.remove_money(money):
                print("\nMoney withdrawn!")


        elif inp == 4:
            acc_no = int(input("Enter Account Number: "))
            acc = bank.get_account(acc_no)
            if not acc:
                continue
            print()
            acc.show_summary()
        

        elif inp == 5:
            acc_no = int(input("Enter your Account Number: "))
            acc = bank.get_account(acc_no)
            if not acc:
                continue

            acc_no_payee = int(input("Enter Payee Account Number: "))
            acc_payee = bank.get_account(acc_no_payee)
            if not acc_payee:
                continue

            amount = int(input("Enter amount to transfer: "))
            if bank.transfer_funds(acc, acc_payee, amount):
                print("\nTransfer Successful!")
            else:
                print("\nSome error occured in transfer!")


        elif inp == 6:
            cur.close()
            con.close()
            print("\nThank You!")
            break


        else:
            print("\nInvalid Option!")
