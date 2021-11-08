import pytest
from my_first_python_module import *

def setup_module():
    pass


def teardown_module():
    pass

def test_my_first_class():
    obj = MyClass()
    assert(type(obj) == MyClass)

def test_my_second_class():
    obj = MyClass2()
    assert (type(obj) == MyClass2)
    print(" ")
    print([i for i in MyClass2.__dict__.keys() if i[:1] != '_'])

