from colecoes import Medicao


class Historico:
    """Histórico de um sensor; preserva cada ocorrência, inclusive repetida."""

    def __init__(self):
        self._leituras: list[Medicao] = []

    def registrar(self, leitura: Medicao):
        self._leituras.append(leitura)

    def quantidade(self):
        return len(self._leituras)

    def ultimas(self, limite: int) -> list:
        if limite < 0:
            raise ValueError()
        if limite == 0 or not self._leituras:
            return []
        return self._leituras[-limite:]
