import unittest
from onename import something_name
from twoname import second_something

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.ad = something_name
        self.subt = second_something
        can = self.ad().add()
        print(can)
        self.subt().subtract()



if __name__ == '__main__':
    unittest.main()
