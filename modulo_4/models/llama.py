
from modulo_4.models.base import ModeloBase

class LlamaModel(ModeloBase):

    def __init__(self, nome: str, temperatura: float = 0.2):
        super().__init__(nome=nome, temperatura=temperatura)

    def invoke(self, prompt: str, api_key: str) -> dict:
        if api_key.startswith("sk-"):
            return  {"model": self.nome, "output": "Resposta do Llama", "temperatura": self.temperatura}
        
        raise ValueError("Chave API inválida: deve começar com 'sk-'")