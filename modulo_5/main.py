"""
# PROJETO — SIMPLE VECTOR STORE

## Objetivo:
Criar uma estrutura orientada a objeto que armazena vetores numéricos em memória
e permite realizar buscas matemáticas por similaridade.

## O programa deve:
- Definir uma classe responsável por gerenciar documentos vetoriais
- Armazenar documentos e seus vetores associados em memória
- Expor um método de busca (query) que:
  - Recebe um vetor de consulta (NumPy array)
  - Recebe um parâmetro K
  - Retorna os K documentos mais similares matematicamente
- Expor um método para adicionar documentos e seus vetores associados

## Formato do documento:
{
"page_content": "...",
"metadata": {"source": "...", "page": 3}
}

## Formato do vetor:
np.array([0.0, 0.2, ...])

## Regras obrigatórias:
- Os vetores devem ser representados com NumPy arrays
- A similaridade deve ser calculada usando distância de cosseno
- A função de similaridade deve ser implementada manualmente com NumPy
- O método query deve ordenar os resultados por similaridade (maior → menor)
- Não é permitido o uso de bibliotecas prontas de busca ou similaridade

## Estruturas que devem ser utilizadas:
- Classe com atributos para armazenar os dados
- Dicionário ou lista para armazenar documentos e vetores
- NumPy para operações vetoriais

## Estrutura mínima esperada:
- src/
  - vector_store.py
  - main.py

## Esse projeto deve retornar:
- Uma lista com os K documentos mais similares
- O valor de similaridade associado a cada documento
"""

import numpy as np

from modulo_5.vector_store import VectorStore

vector_store = VectorStore()

# Documentos
document1 = {
    "page_content": "A inteligência artificial transformou a indústria de tecnologia. Modelos de linguagem grandes (LLMs) estão na vanguarda dessa revolução, permitindo novas aplicações em processamento de linguagem natural e geração de conteúdo.",
    "metadata": {"page": 1, "author": "Alice"}
}

document2 = {
    "page_content": "NumPy é a biblioteca fundamental para computação numérica em Python, oferecendo arrays multidimensionais eficientes e ferramentas para álgebra linear. É essencial para a ciência de dados e machine learning.",
    "metadata": {"page": 2, "author": "Bob"}
}

document3 = {
    "page_content": "O conceito de Recuperação Aumentada por Geração (RAG) combina a capacidade de LLMs de gerar texto com sistemas de recuperação de informação, garantindo que as respostas sejam baseadas em dados factuais.",
    "metadata": {"page": 3, "author": "Charlie"}
}

document4 = {
    "page_content": "Vetores de embeddings são representações numéricas de texto, imagens ou outros dados, onde a similaridade semântica se traduz em proximidade vetorial. A similaridade de cosseno é uma métrica comum para isso.",
    "metadata": {"page": 4, "author": "David"}
}

document5 = {
    "page_content": "Google Colab oferece um ambiente de notebook Jupyter baseado em nuvem, ideal para desenvolvimento e experimentação com modelos de IA e computação intensiva, utilizando GPUs e TPUs gratuitamente.",
    "metadata": {"page": 5, "author": "Eve"}
}

# Adding Documents
vector_store.add_document(document1)
vector_store.add_document(document2)
vector_store.add_document(document3)
vector_store.add_document(document4)
vector_store.add_document(document5)

# Buscar por similaridade
query = np.random.rand(768)
most_similar_vectors = vector_store.query(query, 2)

print(most_similar_vectors)