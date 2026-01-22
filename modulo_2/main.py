"""
# PROJETO 2 — CHAT COM MEMÓRIA PERSISTENTE

## Criar um programa que simula um chat via terminal entre o usuário e um sistema.

## O programa deve:
- Ler um histórico de mensagens salvo em arquivo `.txt` no início da execução
- Exibir todo o histórico no terminal antes de iniciar a nova conversa
- Entrar em um loop contínuo de conversa
- Receber mensagens do usuário
- Gerar uma resposta simples e determinística do sistema (sem uso de IA)
- Encerrar a conversa quando o usuário digitar "/stop"

## Regras obrigatórias:
- Cada mensagem do usuário e cada resposta do sistema devem ser salvas em uma nova linha do arquivo `.txt`
- O programa não pode perder o histórico ao ser encerrado
- O histórico deve ser reaproveitado em execuções futuras
- Dicionários para representar mensagens (ex: {"role": "human/ai", "content": "..."} )
"""
with open("./modulo_2/historico.txt", "r") as arquivo:
    historico = arquivo.read()

historico = [
    {
        "role": msg.split(': ')[0].lower(),
        "content": msg.split(": ")[1]
    }
    for msg in historico.split("\n")[:-1]
    ]

print(historico)


print("======== HISTÓRICO ========")
for msg in historico:
    role = msg.get("role")
    content = msg.get("content")
    print(f"{role.capitalize()}: {content}")
print("="*15)

novo_historico = []
entrada_usuario = input("Human: ")

while entrada_usuario.lower().strip() != "/sair":
    resposta_ia = entrada_usuario[:5]
    print(f"AI: {resposta_ia}")

    novo_historico.append({"role": "human", "content": entrada_usuario})
    novo_historico.append({"role": "ai", "content": resposta_ia})

    entrada_usuario = input("Human: ")

# Salvar o meu histórico
with open("./modulo_2/historico.txt", "a") as arquivo:
    for msg in novo_historico:
        role = msg.get("role")
        content = msg.get("content")
        arquivo.write(f"{role.capitalize()}: {content}\n")