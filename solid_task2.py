
# Задача 2. Принцип открытости/закрытости (OCP)
from abc import ABC, abstractmethod

class Customer(ABC):
    @abstractmethod
    def calculate_discount(self, order_total):
        pass


class RegularCustomer(Customer):
    def calculate_discount(self, order_total):
        return order_total * 0.05


class VIPCustomer(Customer):
    def calculate_discount(self, order_total):
        return order_total * 0.15


class NewCustomer(Customer):
    def calculate_discount(self, order_total):
        return order_total * 0.02


class DiscountCalculator:
    def calculate_discount(self, customer: Customer, order_total):
        return customer.calculate_discount(order_total)