import dataclasses
from typing import Optional


class Account:
    owner: str
    amount:float

    def __init__(self, id: Optional[int], owner: str, amount: float) -> None:
        if amount < 0:
            raise Exception('Amount could not be less than 0')
        
        self.id = id
        self.owner = owner
        self.amount = amount


    def deposit(self, money: float):
        self.amount += money