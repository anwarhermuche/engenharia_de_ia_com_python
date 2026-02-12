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
from modulo_5.vector_store import VectorStore
import numpy as np

lista_documentos = [
    {
        "page_content": "Python é uma linguagem de programação versátil.",
        "metadata": {"source": "artigo1.txt", "page": 1}
    },
    {
        "page_content": "O NumPy facilita operações matemáticas com arrays.",
        "metadata": {"source": "artigo2.txt", "page": 2}
    },
    {
        "page_content": "A inteligência artificial está transformando indústrias.",
        "metadata": {"source": "artigo3.txt", "page": 5}
    },
    {
        "page_content": "Vetores são essenciais em machine learning.",
        "metadata": {"source": "apostila.pdf", "page": 10}
    },
    {
        "page_content": "Cosine similarity mede a semelhança entre dois vetores.",
        "metadata": {"source": "slide_apresentacao.ppt", "page": 3}
    },
    {
        "page_content": "A busca vetorial permite encontrar conteúdos similares.",
        "metadata": {"source": "relatorio.docx", "page": 7}
    },
    {
        "page_content": "Documentos podem ser indexados por seus embeddings vetoriais.",
        "metadata": {"source": "manual.doc", "page": 12}
    },
    {
        "page_content": "Machine learning depende de bons conjuntos de dados.",
        "metadata": {"source": "artigo4.txt", "page": 4}
    }
]

vector_store = VectorStore()

for doc in lista_documentos:
    vector_store.add_document(doc)


query = np.random.random(10)

print(vector_store.query(query, K = 5))