

class ModeloBase:

    def __init__(self, name: str, temperature: float = 0.2):
        self.name = name
        self.temperature = temperature

    def invoke(self, prompt: str, api_key: str):
        raise NotImplementedError("Método 'invoke' é implementado apenas para as classes filhas")