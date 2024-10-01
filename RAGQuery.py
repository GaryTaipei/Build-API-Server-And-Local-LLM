#For OpenAI to Run: pip install llama-index
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    ServiceContext,
    StorageContext,
    SQLDatabase,
    load_index_from_storage,
    Settings,
)
from llama_index.embeddings.huggingface import HuggingFaceEmbedding #pip install llama-index-embeddings-huggingface
from llama_index.llms.ollama import Ollama #pip install llama-index-llms-ollama
import os.path

class RAGQuery():
    def __init__(self):
        pass

    def query_vector(self, prompt: str):
        # Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
        Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5") # bge-base embedding model
        # ollamaitem: Query
        Settings.llm = Ollama(model="llama3.1:latest", request_timeout=360.0)
        # check if storage already exists
        PERSIST_DIR = "./storage"
        if not os.path.exists(PERSIST_DIR):
            # load the documents and create the index
            documents = SimpleDirectoryReader("data").load_data(show_progress=True)
            index = VectorStoreIndex.from_documents(documents)
            # store it for later
            index.storage_context.persist(persist_dir=PERSIST_DIR)
        else:
            # load the existing index
            storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
            index = load_index_from_storage(storage_context)
        query_engine = index.as_query_engine()
        response = query_engine.query(prompt)
        index.storage_context.persist()
        return response