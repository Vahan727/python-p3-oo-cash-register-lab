#!/usr/bin/env python3

class CashRegister:
  total = 0
  def __init__(self, discount=0):
    self.discount = discount
    self.items = []
    self.newest_items = []
  
  def get_discount(self):
    return self.discount

  def add_item(self, title, price, quantity=1):
    self.newest_items.append({'title':title, 'price':price, 'quantity':quantity})
    self.price = price
    self.total += price * quantity
    self.items.extend([title] * quantity)
    return self.total
  
  def apply_discount(self):
    if self.discount > 0:
      self.discount_value = self.total * (self.discount / 100)
      self.total -= self.discount_value
      print(f'After the discount, the total comes to ${int(self.total)}.')
    else:
      print('There is no discount to apply.')
  
  def void_last_transaction(self):
    self.total -= self.newest_items[-1]["price"] * self.newest_items[-1]["quantity"]
    self.items = [self.items.pop(-1) for self.newest_items[-1]["quantity"] in self.newest_items[-1]]
    self.newest_items.pop()
    if len(self.items) <= 0:
      self.total = 0
    return self.total


