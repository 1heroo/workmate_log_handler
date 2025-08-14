from abc import ABC, abstractmethod


class Report(ABC):

    @abstractmethod
    def name(self) -> str:
        ...
    
    @abstractmethod
    def generate(self) -> str:
        ...
    
