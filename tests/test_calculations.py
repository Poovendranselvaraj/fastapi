import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(100)

@pytest.mark.parametrize("num1,num2,expected", [(5,3,8),(6,0,6),(3,0,3)])
def test_add(num1,num2,expected):
    print("testing add function")
    assert add(num1,num2) == expected

   
def test_subtract():
    print("testing subtract function")
    assert subtract(9,4) == 5

def test_multiply():
    print("testing multiply function")
    assert multiply(4,3) == 12  


def test_divide():
    print("testing divide function")
    assert divide(20,5) == 4  

def test_bank_set_initial_amount(zero_bank_account):
    bank_account = BankAccount(100)
    assert bank_account.balance == 100   

def test_bank_default_amount():
    account = BankAccount()
    assert account.balance == 0      

def test_withdraw():
    account = BankAccount(100)
    account.withdraw(10)
    assert account.balance == 90   

def test_deposit():
    account = BankAccount(100)
    account.deposit(20)
    assert account.balance == 120   

def test_collect_interest():
    account = BankAccount(100)
    account.collect_interest()
    assert round(account.balance,6) == 110     