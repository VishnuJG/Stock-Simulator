class AccountManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self, username, initial_balance):
        if username in self.accounts:
            raise ValueError('Account already exists.')
        self.accounts[username] = initial_balance

    def get_balance(self, username):
        if username not in self.accounts:
            raise ValueError('Account does not exist.')
        return self.accounts[username]

    def update_balance(self, username, amount):
        if username not in self.accounts:
            raise ValueError('Account does not exist.')
        self.accounts[username] += amount

    def delete_account(self, username):
        if username in self.accounts:
            del self.accounts[username]

class Account:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def __str__(self):
        return f'Account({self.username}, Balance: {self.balance})'
