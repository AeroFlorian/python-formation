class MyClass:
    def __init__(self):
        pass


class MyClass2:
    test1 = None

    def __init__(self):
        self.test1 = "test"

    def test_function(self):
        print(self.test1)
