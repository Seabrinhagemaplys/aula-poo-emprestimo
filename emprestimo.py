from abc import ABC, abstractmethod

class Emprestimo(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def registrar(self):
        pass