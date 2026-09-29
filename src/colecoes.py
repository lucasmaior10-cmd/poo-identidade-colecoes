from dataclasses import dataclass
from typing import Generic, TypeVar
from identidade import IdSensor


@dataclass(frozen=True)
class Medicao:
    valor: float
    unidade: str


T = TypeVar("T")


class Catalogo(Generic[T]):
    def __init__(self):
        self._itens: dict[IdSensor, T] = {}

    def inserir(self, id_sensor, item) -> bool:
        if id_sensor in self._itens:
            return False
        self._itens[id_sensor] = item
        return True

    def buscar(self, id_sensor):
        return self._itens.get(id_sensor, None)

    def remover(self, id_sensor) -> bool:
        if id_sensor in self._itens:
            del self._itens[id_sensor]
            return True
        return False

    def quantidade(self):
        return len(self._itens)

    def ids(self):
        return set(self._itens)
