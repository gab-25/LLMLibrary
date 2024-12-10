from abc import ABC


class LLMClient(ABC):
    def load(self):
        pass

    def config(self):
        pass
