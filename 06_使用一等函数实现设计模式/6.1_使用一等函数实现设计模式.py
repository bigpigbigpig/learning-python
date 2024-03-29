# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: li zhang
@file: 6.1_使用一等函数实现设计模式.py
@time: 2019/09/26 22:42:25
"""

# 在一等语言中重新审视 策略 命令 模板方法 访问者 模式
# 使用函数重构代码来有效减少代码行数

# 1. 经典的策略模式
# 有 1000 或以上积分的顾客， 每个订单享 5% 折扣。
# 同一订单中， 单个商品的数量达到 20 个或以上， 享 10% 折扣。
# 订单中的不同商品达到 10 个或以上， 享 7% 折扣。

from abc import ABC, abstractclassmethod
from collections import namedtuple
Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price