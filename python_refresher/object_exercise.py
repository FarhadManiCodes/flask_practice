"""exercise for object oriented python"""
from typing import Dict, List
import copy


class Store:
    """class store for exercise 38"""

    def __init__(self, name: str):
        """Constructor"""
        self.name = name
        self.items: List[Dict] = []

    def __str__(self) -> str:
        """Return a string representation of store"""
        return self.name

    def add_item(self, name: str, value: float):
        """Add an item to the store"""
        self.items.append({
            'name': name,
            'price': value})

    def stoke_price(self) -> float:
        """Return the stoke price of the store"""
        return sum([item['price'] for item in self.items])

    @classmethod
    def franchise(cls, store):
        """print with the franchise in it"""
        store_copy = copy.copy(store)
        store_copy.name = store.name + " - franchise"
        return store_copy

    @staticmethod
    def store_details(store) -> str:
        """print the details of the store"""
        return store.name + " total stock price:" + str(store.stoke_price())
