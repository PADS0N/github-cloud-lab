import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from calculator import add, divide
import pytest
def test_add(): assert add(2, 3) == 5
def test_divide_by_zero():
    with pytest.raises(ValueError): divide(5, 0)
