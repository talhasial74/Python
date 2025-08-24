"""
bankcore.py
Handles customer id generation and authentication.
"""

branch_id = 8354   # changed as requested
_customer_counter = 0

# Users_Info maps customer_id -> {"name": str, "password": str}
Users_Info = {}


def _next_user_number():
    """Return next user number (int) and update internal counter."""
    global _customer_counter
    _customer_counter += 1
    return _customer_counter


def _make_customer_id(user_number: int) -> str:
    return f"{branch_id}-{user_number}"


def create_account(name: str, password: str = "") -> str:
    """Register a new user and return customer_id."""
    user_number = _next_user_number()
    customer_id = _make_customer_id(user_number)

    Users_Info[customer_id] = {"name": name, "password": str(password)}
    return customer_id


def login(customer_id: str, password: str) -> bool:
    """Return True if credentials match, else False."""
    if not customer_id or customer_id not in Users_Info:
        return False
    return Users_Info[customer_id]["password"] == str(password)


def get_name(customer_id: str) -> str:
    """Return stored name for customer_id or empty string if not found."""
    return Users_Info.get(customer_id, {}).get("name", "")
