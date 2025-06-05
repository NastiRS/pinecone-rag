from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from typing import List
from pydantic import BaseModel
from app.pinecone_db_services.config import vector_store
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(api_key=os.getenv("BTECH_OPENAI_API_KEY_MERMAID"), model="gpt-4o")


class State(BaseModel):
    question: str
    context: List[Document] = []
    answer: str = ""


template = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Use three sentences maximum and keep the answer as concise as possible.

Context: {context}

Question: {question}

Helpful Answer:"""
custom_rag_prompt = PromptTemplate.from_template(template)


def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state.question)
    state.context = retrieved_docs
    return state


def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state.context)
    messages = custom_rag_prompt.invoke(
        {"question": state.question, "context": docs_content}
    )
    response = llm.invoke(messages)
    state.answer = response.content
    return state
