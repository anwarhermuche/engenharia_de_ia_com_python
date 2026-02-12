from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("CHAVE_API", "Chave não encontrada"))