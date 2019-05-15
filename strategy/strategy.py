from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def suggest(self):
        pass

    @abstractmethod
    def train(self):
        pass
