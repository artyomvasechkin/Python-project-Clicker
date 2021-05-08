import unittest

from src import Clicker_class


class MyTestCase(unittest.TestCase):
    def setUp(self):
        root = Clicker_class.tk.Tk()
        self.clicker = Clicker_class.Clicker(root)

    def test_update(self):
        self.clicker.gear['clicker'].cost = 10
        self.clicker.gear['clicker'].quantity = 4
        self.clicker.gear['clicker'].per_second = 7
        self.clicker.current_clicks = 0
        self.clicker.update()
        self.assertEqual(self.clicker.current_clicks, 28)

    def test_increment(self):
        self.clicker.gear['clicker'].cost = 2
        self.clicker.gear['clicker'].quantity = 1
        self.clicker.gear['clicker'].per_second = 4
        self.clicker.increment()
        self.assertEqual(self.clicker.current_clicks, 1)

    def test_purchase(self):
        self.clicker.gear['clicker'].cost = 5
        self.clicker.gear['clicker'].quantity = 8
        self.clicker.gear['clicker'].per_second = 3
        self.clicker.current_clicks = 9
        self.clicker.purchase('clicker')
        self.assertEqual(self.clicker.current_clicks, 4)
        self.assertEqual(self.clicker.gear['clicker'].cost, 6)
        self.assertEqual(self.clicker.gear['clicker'].quantity, 9)


if __name__ == '__main__':
    unittest.main()
