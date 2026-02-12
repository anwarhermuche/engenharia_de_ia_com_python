class ModeloBase:

    def __init__(self, nome: str, temperatura: float = 0.2):
        self.nome = nome
        self.temperatura = temperatura

    def invoke(self, prompt: str, api_key: str) -> dict:
        raise NotImplementedError("Método invoke inválido para a classe 'ModeloBase'.")