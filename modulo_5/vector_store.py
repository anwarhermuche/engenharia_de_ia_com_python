import numpy as np

class VectorStore:

    def __init__(self):
        self.embeddings = np.array([])
        self.documents = np.array([])


    def __generate_embedding(self, page_content: str) -> np.ndarray:
        np.random.seed(40)
        vector = np.random.random(10)
        return vector


    def add_document(self, document: dict) -> None:
        if self.documents.size == 0:
            self.documents = np.array([document], dtype=object)
            self.embeddings = np.array([self.__generate_embedding(document.get('page_content', ''))])
        else:
            self.documents = np.append(self.documents, [document])
            self.embeddings = np.append(self.embeddings, [self.__generate_embedding(document.get('page_content', ''))], axis=0)
        return

    def __calc_similarity(self, v1: np.ndarray, v2: np.ndarray) -> float:
        dotprod = np.dot(v1, v2)
        norm_v1 = np.linalg.norm(v1, ord = 2)
        norm_v2 = np.linalg.norm(v2, ord = 2)
        return dotprod/(norm_v1*norm_v2)

    def query(self, query: np.ndarray, K: int = 4) -> list[dict]:
        similarities = [self.__calc_similarity(query, vec) for vec in self.embeddings]
        indices = np.argsort(similarities)[::-1]
        result = []
        similarities_k = np.array(similarities)[indices][:K]
        documents_k = self.documents[indices][:K]
        for sim, doc in zip(similarities_k, documents_k):
            result.append({
                'similarity': sim,
                'document': doc
            })
        return result
