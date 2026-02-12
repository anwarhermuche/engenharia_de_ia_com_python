"""
# PROJETO — MODEL PROVIDER SDK (SIMULADO)

## Objetivo:
Criar uma mini-SDK em Python que simula provedores de modelos de linguagem,
utilizando Programação Orientada a Objetos, herança, polimorfismo e variáveis de ambiente.

## O programa deve:
- Definir uma classe base genérica (ex: ModeloBase)
- Definir subclasses para provedores específicos (ex: OpenAIModel, LlamaModel)
- Cada classe deve:
  - Receber nome do modelo e temperatura no construtor
  - Expor um método comum chamado invoke() com parêmetro 'prompt' e 'api_key''
  - Verificar se api_key começa com "sk-" antes de dar uma resposta
    - Se começar, use o time.sleep() e dê a resposta
    - Se não começar, dê uma resposta de erro "API Key inválida"
- O comportamento deve ser intercambiável via polimorfismo

## Regras obrigatórias:
- A classe base não pode conhecer detalhes das subclasses
- As subclasses devem sobrescrever o método invoke()
- O método invoke() deve:
  - Simular latência usando time.sleep
  - Retornar um dicionário estruturado (ex: {"model": "...", "output": "...", "temperatura": ...})
- O programa deve ler duas variáveis de ambiente fictícias:
  - OPENAI_API_KEY
  - LLAMA_API_KEY
- As variáveis devem ser carregadas via python-dotenv
- O arquivo .env não pode ser versionado
- O main.py deve escolher dinamicamente qual modelo instanciar com base no input do usuário

## Estrutura mínima esperada:
- src/
  - models/
    - base.py
    - openai.py
    - llama.py
  - main.py

## Esse projeto deve retornar:
- A resposta estruturada do método invoke()
"""

from modulo_4.models.openai import OpenAIModel
from modulo_4.models.llama import LlamaModel
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLAMA_API_KEY = os.getenv("LLAMA_API_KEY")

modelo = input("Qual modelo quer usar (gpt ou llama)? ").strip().lower()

if modelo == 'gpt':
    openai = OpenAIModel("gpt-5.1")
    print(openai.invoke("Olá", api_key = OPENAI_API_KEY))
elif modelo == 'llama':
    llama = LlamaModel("llama-70b", temperatura=0.9)
    print(llama.invoke("Olá", api_key = LLAMA_API_KEY))