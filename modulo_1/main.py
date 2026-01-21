"""
# PROJETO 1 — PROMPT PACKER (BÁSICO)

## Criar um programa que recebe (via terminal):
- role
- tom de voz
- tarefa
- número máximo de palavras

## Regras obrigatórias:
- O programa deve montar um prompt final usando f-strings, no formato:
  - Role: ...
  - Tom de voz: ...
  - Tarefa: ...
  - Instruções: ...
- O programa deve estimar a quantidade de palavras do prompt final usando a heurística:
  - 1 palavra ≈ 6.11 caracteres
- O programa deve checar se a quantidade estimada de palavras ficou dentro de uma faixa aceitável:
  - entre (máximo de palavras - 10) e (máximo de palavras + 10)

## Esse programa deve retornar:
- prompt final (string)
- quantidade de palavras estimada (float ou int)
- está dentro do intervalo aceitável? (bool)
"""

# Recebendo entradas do usuário (lá ele)
role = input("Digite o cargo: ")
tom_de_voz = input("Tom de voz: ")
tarefa = input("Digite a tarefa: ")
numero_maximo_palavras = int(input("Digite o número máximo de palavras: "))

# Montando o prompt
SYSTEM_PROMPT = f"""
# Cargo
Você é um {role} com mais de 10 anos de experiência

# Tom de voz
Você segue estritamente esse tom de voz: {tom_de_voz}

# Tarefa
Tarefa a ser executada: {tarefa}

# Instruções
Pense, sempre, passo a passo para resolver as tarefas solicitadas.
"""

# Quantidade de palavras estimada
numero_caracteres_prompt = len(SYSTEM_PROMPT)
numero_estimado_de_palavras = numero_caracteres_prompt//6.11

# Tá dentro do intervalo confiável?
dentro_intervalo = numero_maximo_palavras - 10 <= numero_estimado_de_palavras <= numero_maximo_palavras + 10

# Exibir resultados na tela
print(SYSTEM_PROMPT)
print("\n")
print(numero_estimado_de_palavras)
print("\n")
print(dentro_intervalo)