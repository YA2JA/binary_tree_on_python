#!/usr/bin/python3
from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    @abstractmethod
    def set_value(self,  *args, **kwargs):
        pass
    
    @abstractmethod
    def create_child(self,  *args, **kwargs):
        pass
    
    def __iter__(self, *args, **kwargs):
        if self.left is not None:
            yield self.left
            yield from self.left

        if self.right is not None:
            yield self.right
            yield from self.right
    
    def __str__(self):
        return f"value = {self.value}"
    
    def __repr__(self):
        res = f"{repr(self.left)} --- {repr(self.right)}"
        return f"{res}\n{self.value}"
    
class Binnary_Tree(Node):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
    
    def set_value(self, value):
        self.value = value
    
    def create_child(self, value):
        return Binnary_Tree(value)

    def insert(self, value, force_left=False, force_right=False):
        if self.value is None:
            self.value = value
            return

        if self.left is None and not force_right:
            self.left = self.create_child(value)
            return

        if self.right is None and not force_left:
            self.right = self.create_child(value)
            return

if __name__ == "__main__":
    root = Binnary_Tree(1)
    root.insert(2)
    root.insert(3)