# Função que salva no arquivo os logs
def log(
    modelo: str,
    tokens_system_prompt: int,
    tokens_input: float,
    tokens_output: float,
    custo: float) -> None:
    """
    Salva logs no arquivo "logs.txt"
    """
    log_texto = f"Modelo: {modelo} | Tokens System Prompt: {tokens_system_prompt}\
 | Tokens Input: {tokens_input} | Tokens Output: {tokens_output} | Custo: {custo}\n"
    
    with open("./modulo_3/logs.txt", "a") as arquivo:
        arquivo.write(log_texto)