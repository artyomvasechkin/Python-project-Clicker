import unittest
import tkinter as tk
import main


class MyTestCase(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.clicker = main.Clicker(root)

    def test_update(self):
        self.clicker.gear = {}
        self.clicker.gear.cost = 10
        self.clicker.gear.quantity = 4
        self.clicker.gear.per_second = 7
        self.clicker.update()
        self.clicker.current_clicks = 0
        self.assertEqual(self.clicker.current_clicks, 28)

    def test_increment(self):
        self.clicker.gear = {}
        self.clicker.gear.cost = 2
        self.clicker.gear.quantity = 1
        self.clicker.gear.per_second = 4
        self.clicker.increment()
        self.clicker.current_clicks = 0
        self.assertEqual(self.clicker.current_clicks, 1)

    def test_purchase(self):
        self.clicker.gear = {}
        self.clicker.gear.cost = 5
        self.clicker.gear.quantity = 8
        self.clicker.gear.per_second = 3
        self.clicker.purchase('clicker')
        self.clicker.current_clicks = 9
        self.assertEqual(self.clicker.current_clicks, 3)
        self.assertEqual(self.clicker.gear.cost, 6)
        self.assertEqual(self.clicker.gear.quantity, 9)
