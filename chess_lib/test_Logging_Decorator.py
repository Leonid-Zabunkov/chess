import unittest
from .Logging import log_get, log_set, log_call, logs

@log_call
def add(a, b):
    return a + b

class Dummy:
    @log_call
    def greet(self, name):
        return f"Hi {name}"

class Item:
    def __init__(self, price):
        self._price = price
    
    @property
    @log_get
    def price(self):
        return self._price
    
    @price.setter
    @log_set
    def price(self, val):
        self._price = val

class TestLogDecorators(unittest.TestCase):

    # Очищаем логи перед каждым тестом
    def setUp(self):
        logs.clear()

    def test_log_call_function(self):
        add(2, 3)
        self.assertEqual(logs[0], "add(2, 3)")

    def test_log_call_method(self):
        d = Dummy()
        d.greet("Alice")
        self.assertEqual(logs[0], "Dummy.greet('Alice')")

    def test_log_property_get_set(self):
        item = Item(100)
        p = item.price
        item.price = p + 100
        
        self.assertListEqual(logs, ['GET: Item.price', 'SET: Item.price = 200'])
        
    def test_complex_flow(self):
        item = Item(100)
        item.price += 50
        add(1, 1)
        
        self.assertListEqual(logs, ['GET: Item.price', 'SET: Item.price = 150', 'add(1, 1)'])

if __name__ == "__main__":
    unittest.main()
