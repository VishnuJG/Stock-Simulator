class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.now()

    def __str__(self):
        return f'{self.timestamp}: {self.transaction_type} of {self.amount}'

class TransactionManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_all_transactions(self):
        return self.transactions

    def get_balance_change(self):
        return sum(t.amount if t.transaction_type == 'deposit' else -t.amount for t in self.transactions)
