class Owner:
    def __init__(self, name):
        self.balance = 0
        self.name = name

    def deposit(self, amount):
        self.balance += amount
        print(f"Your new balance is £{self.balance}.")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Your new balance is £{self.balance}.")
    
    def info(self):
        print(f"{self.name}'s account has £{self.balance}")

scott = Owner("Scott")

scott.deposit(100)
scott.info()
scott.withdraw(50)
scott.info()