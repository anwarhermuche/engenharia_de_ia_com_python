import numpy as np

class VectorStore:

    def __init__(self):
        self.documents = np.array([])
        np.random.seed(42)

    def __text_to_embedding(self, text: str) -> np.ndarray:
        return np.random.rand(768)

    def add_document(self, doc: dict) -> None:
        embeddings = self.__text_to_embedding(doc['page_content'])

        doc['embedding'] = embeddings

        self.documents = np.append(self.documents, doc)

        return None

    def query(self, vector: np.ndarray, k: int = 4) -> np.ndarray:
        embeddings = np.array([doc['embedding'] for doc in self.documents])
        norms = np.linalg.norm(embeddings, axis = 1)
        norm_query = np.linalg.norm(vector)
        dot_prods = np.dot(embeddings, vector)

        similarity_vector = np.array([{"cosine_distance": 1 - dot_prods[i]/(norms[i]*norm_query),
        "page_content": self.documents[i]['page_content'],
        "metadata": self.documents[i]['metadata']} for i in range(len(self.documents))])

        similarity_vector = sorted(similarity_vector.tolist(), key = lambda x: x['cosine_distance'], reverse=False)

        return similarity_vector[:k]