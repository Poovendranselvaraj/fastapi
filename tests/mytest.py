
from app.calculations import add
def test_add():
    print("testing_add function")
    sum=add(5, 3)
    # sum==8
    assert sum == 8

  