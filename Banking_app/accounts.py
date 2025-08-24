"""
accounts.py
Manages balances and simple operations: check_balance, deposit, withdraw.
"""

balance_record = {}


def check_balance(customer_id: str) -> float:
    return float(balance_record.get(customer_id, 0.0))


def deposit(customer_id: str, amount: float) -> float:
    amt = float(amount)
    if amt <= 0:
        raise ValueError("Deposit amount must be positive.")
    current = check_balance(customer_id)
    new_bal = current + amt
    balance_record[customer_id] = new_bal
    return new_bal


def withdraw(customer_id: str, amount: float) -> float:
    amt = float(amount)
    if amt <= 0:
        raise ValueError("Withdrawal amount must be positive.")
    current = check_balance(customer_id)
    if amt > current:
        raise ValueError("Insufficient balance.")
    new_bal = current - amt
    balance_record[customer_id] = new_bal
    return new_bal
