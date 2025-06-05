from pinecone import Pinecone, ServerlessSpec
import os
from dotenv import load_dotenv
import time
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()

pinecone_api_key = os.getenv("PINECONE_API_KEY")

pc = Pinecone(api_key=pinecone_api_key)

index_name = "langchain-test-index"  # change if desired

existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large", api_key=os.getenv("BTECH_OPENAI_API_KEY_MERMAID")
)

if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=3072,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    while not pc.describe_index(index_name).status["ready"]:
        time.sleep(1)

index = pc.Index(index_name)

vector_store = PineconeVectorStore(index=index, embedding=embeddings)
