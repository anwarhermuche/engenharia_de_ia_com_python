from modulo_4.models.base import ModeloBase
import time

class LlamaModel(ModeloBase):

    def __init__(self, name: str, temperature: float = 0.2):
        super().__init__(name, temperature)

    def invoke(self, prompt: str, api_key: str) -> dict:
        if not api_key.startswith("sk-"):
            raise ValueError("API Key inválida")
        
        time.sleep(4)
        return {"model": self.name, "output": "Output do Llama", "temperature": self.temperature}