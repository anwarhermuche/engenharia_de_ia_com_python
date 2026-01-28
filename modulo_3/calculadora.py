from modulo_3.salva_log import log


# Preços modelos (a cada um milhão de tokens)
PRECOS_MODELOS = {
    "gpt-4.1-mini": {"input": 0.8, "output": 4},
    "claude-4-opus": {"input": 8, "output": 25}
}


# Função que calcula os custos
def calcula_custo_tokens_mensal(
    modelo: str,
    tokens_system_prompt: int,
    media_tokens_input: float,
    media_tokens_output: float,
    media_inteira_mensagens_dia: int
    ) -> float:
    
    total_tokens_input = 0
    total_tokens_output = 0
    if type(media_inteira_mensagens_dia) != int:
        media_inteira_mensagens_dia = int(round(media_inteira_mensagens_dia, 0))

    for numero_da_mensagem in range(1, media_inteira_mensagens_dia + 1):
        total_tokens_input += tokens_system_prompt + min(numero_da_mensagem, 10)*media_tokens_input + min((numero_da_mensagem-1), 10)*media_tokens_output
        total_tokens_output += media_tokens_output
    
    custo_input_modelo = PRECOS_MODELOS.get(modelo).get("input")
    custo_output_modelo =  PRECOS_MODELOS.get(modelo).get("output")

    custo_total_input = (custo_input_modelo*total_tokens_input)/1_000_000
    custo_total_output = (custo_output_modelo*total_tokens_output)/1_000_000

    custo_total_geral = (custo_total_input + custo_total_output)*30

    log(modelo, tokens_system_prompt, media_tokens_input, media_tokens_output, custo_total_geral)

    return custo_total_geral
