from uuid import uuid4
from langchain_core.documents import Document
from app.pinecone_db_services.config import vector_store


def add_docs_into_vector_store(documents: list[Document]) -> bool:
    try:
        if not documents:
            print("Warning: Empty documents list - nothing to add")
            return False

        uuids = [str(uuid4()) for _ in range(len(documents))]
        vector_store.add_documents(documents=documents, ids=uuids)
        print("Docs added")
        return True

    except Exception as e:
        print(f"Error adding documents to vector store: {str(e)}")
        return False
