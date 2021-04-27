import tkinter as tk
import keyboard
from src import Gear_class


class Clicker:
    def __init__(self, parent):
        self.parent = parent
        self.purchase_buttons = {}
        self.the_button = tk.Button(parent, text='Click the button!', width=20, height=5, command=self.increment)
        self.gear = {}
        self.current_clicks = 0
        self.gear['auto clicker'] = Gear_class.Gear('auto clicker', 15, per_second=1)
        self.gear['clicker'] = Gear_class.Gear('clicker', 10, quantity=1)
        self.purchase_buttons['clicker'] = tk.Button(parent, text='Extra click. Initial cost is %d: 1' % self.gear[
            'clicker'].cost,
                                                     command=lambda: self.purchase('clicker'))
        self.purchase_buttons['auto clicker'] = tk.Button(parent,
                                                          text='Auto clicker. Initial cost is {}: 0'.format(self.gear[
                                                              'auto clicker'].cost),
                                                          command=lambda: self.purchase('auto clicker'))
        self.current_click_label = tk.Label(parent, text='0')
        self.current_click_label.grid(row=1, column=0)
        self.the_button.grid(row=0, column=0)
        for name in self.gear:
            if self.gear[name].per_second:
                column = 2
                row = 0  # row of button in window (place) row must be in centre (-1 - down, 1 - up)
            else:
                column = 1
                row = 0  # row of button in window (place) row must be in centre (-1 - down, 1 - up)
            self.purchase_buttons[name].grid(row=row, column=column)
        self.update()

    def update(self):
        for gear in self.gear.values():
            self.current_clicks += gear.per_second * gear.quantity
        if keyboard.is_pressed('space'):
            self.increment()
        self.parent.after(1000, self.update)
        self.current_click_label.config(text='%d' % self.current_clicks)

    def increment(self):
        self.current_clicks += self.gear['clicker'].quantity
        self.current_click_label.config(text='%d' % self.current_clicks)

    def purchase(self, name):
        if self.current_clicks >= self.gear[name].cost:
            self.gear[name].quantity += 1
            self.current_clicks -= self.gear[name].cost
            self.gear[name].cost *= 1.2
            self.current_click_label.config(text='%d' % self.current_clicks)
            self.purchase_buttons[name].config(
                text=self.purchase_buttons[name]['text'].split(': ')[0] + ': {:.1f}: {} clicks'.format(
                    self.gear[name].cost,
                    self.gear[name].quantity))
