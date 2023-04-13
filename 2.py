from abc import ABC, abstractmethod
from typing import Any
class AbstractClothes(ABC):
    @property
    @abstractmethod
    def tissue_required(self):
        pass

    @property
    @abstractmethod
    def measuring(self):
        pass

    @abstractmethod
    def _calc_tissue_required(self):
        pass
class Clothes(AbstractClothes):
    _clothes = []
    def __init__(self, name: str, measuring: Any):
        self.name = name
        self._measuring = measuring
        self._tissue_required = None

        self._clothes.append(self)

    def _calc_tissue_required(self):
        raise NotImplemented
    @property
    def tissue_required(self) -> float:
        if not self._tissue_required:
            self._calc_tissue_required()

        return self._tissue_required
    @property
    def measuring(self) -> Any:
        return self._measuring

    @measuring.setter
    def measuring(self, measuring: Any):
        self._measuring = measuring
        self._tissue_required = None

    @property
    def total_tissue_required(self):
        return sum([item.tissue_required for item in self._clothes])


class Coat(Clothes):
    def _calc_tissue_required(self):
        self._tissue_required = round(self.measuring / 6.5 + 0.5, 2)

    def V(self) -> Any:
        return self.measuring

    def V(self, size: Any):
        self.measuring = size

    def __str__(self):
        return f"Для пошива пальто {self.measuring} размера " \
               f"требуется {self.tissue_required} кв. метров ткани"

class Suit(Clothes):
    def _calc_tissue_required(self):
        self._tissue_required = round(2 * self.measuring * 0.01 + 0.3, 2)

    def H(self) -> Any:
        return self.measuring

    def H(self, height: Any):
        self.measuring = height

    def __str__(self):
        return f"Для пошива костюма на рост {self.measuring} см. " \
               f"требуется {self.tissue_required} кв. метров ткани"

if __name__ == '__main__':
    coat = Coat('Пальто', 8)
    print(coat)
    coat.V = 10
    print(coat)

    suit = Suit('Костюм', 200)
    print(suit)
    suit.H = 400
    print(suit)
