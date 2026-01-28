"""
# PROJETO — TOKEN COST CALCULATOR

## Objetivo:
Criar uma mini-biblioteca em Python para estimar custo mensal de uso de modelos de linguagem,
seguindo padrões profissionais de projeto (Poetry, modularização e tipagem).

## O programa deve:
- Receber do usuário:
  - nome do modelo (ex: "gpt-4", "claude-3-opus")
  - tokens no system prompt
  - média de tokens de input
  - média de tokens de output
  - média de mensagens por dia
- Calcular o custo mensal com base em uma tabela de preços definida no código
- Exibir o resultado de forma clara no terminal
- Registrar cada cálculo em um arquivo de log (.txt)

## Regras obrigatórias:
- Os preços dos modelos devem ser armazenados em um dicionário
- A lógica de cálculo deve estar isolada em funções tipadas
- A janela de contexto deve ser considerada
- O módulo de cálculo não pode conter input() nem print()
- O main.py deve apenas orquestrar entradas, saídas e chamadas de função
- Cada execução deve registrar:
  - modelo
  - tokens informados
  - custo calculado
- O log deve ser escrito utilizando context manager (with open)

## Estrutura mínima esperada:
- modulo_3/
  - calculadora.py
  - main.py

## Esse projeto deve retornar:
- custo total estimado (float)
"""
from modulo_3.calculadora import calcula_custo_tokens_mensal

# Inputs do usuário
modelo = input("Digite o nome do modelo: ").strip()
tokens_system_prompt = int(input("Digite o número de tokens do system prompt: ").strip())
tokens_input = float(input("Digite a média de tokens de input do usuário: "))
tokens_output = float(input("Digite a média de tokens de output da IA: "))
media_msgs_dia = int(input("Digite a média de mensagens enviadas pelo usuário por dia: "))

# Calculando o custo
custo = calcula_custo_tokens_mensal(modelo, tokens_system_prompt, tokens_input, tokens_output, media_msgs_dia)

# Exibindo o custo
print(f"Custo mensal estimado em: $ {custo:.2f}")