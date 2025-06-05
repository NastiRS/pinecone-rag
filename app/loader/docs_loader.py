from pathlib import Path
import os
from langchain_community.document_loaders import (
    TextLoader,
    DirectoryLoader,
    PyPDFLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredPowerPointLoader,
    UnstructuredExcelLoader,
)
from functools import partial


from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_docs(documents, chunk_size, chunk_overlap):
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            add_start_index=True,
        )
        splits = text_splitter.split_documents(documents)
        return splits
    except Exception as e:
        print(f"Error splitting documents: {str(e)}")
        return []


def load_documents_from_directory(directory_path, chunk_size=800, chunk_overlap=100):
    try:
        path = Path(directory_path)

        if not path.exists():
            raise FileNotFoundError(f"Path does not exist: {directory_path}")

        if not os.access(str(path), os.R_OK):
            raise PermissionError(f"No read permissions for: {directory_path}")

        if path.is_file():
            file_ext = path.suffix.lower()
            documents = []
            try:
                if file_ext == ".txt":
                    documents = TextLoader(directory_path, encoding="utf-8").load()
                elif file_ext == ".pdf":
                    documents = PyPDFLoader(directory_path, extract_images=False).load()
                elif file_ext == ".docx":
                    documents = UnstructuredWordDocumentLoader(
                        directory_path, encoding="utf-8"
                    ).load()
                elif file_ext == ".pptx":
                    documents = UnstructuredPowerPointLoader(
                        directory_path, encoding="utf-8"
                    ).load()
                elif file_ext in (".xlsx", ".xls"):
                    documents = UnstructuredExcelLoader(
                        directory_path, mode="elements"
                    ).load()
                else:
                    raise ValueError(f"Unsupported file type: {file_ext}")

                # Llamar a split_docs también para archivos individuales
                return split_docs(
                    documents, chunk_size=chunk_size, chunk_overlap=chunk_overlap
                )
            except Exception as e:
                print(f"Error loading file {directory_path}: {str(e)}")
                return []

        # Si es directorio, usar la lógica original
        docx_loader = partial(UnstructuredWordDocumentLoader, encoding="utf-8")
        txt_loader = partial(TextLoader, encoding="utf-8")
        pptx_loader = partial(UnstructuredPowerPointLoader, encoding="utf-8")
        pdf_loader = partial(PyPDFLoader, extract_images=False)
        excel_loader = partial(UnstructuredExcelLoader, mode="elements")

        documents = []

        try:
            loader_docx = DirectoryLoader(
                directory_path,
                glob="**/*.docx",
                loader_cls=docx_loader,
                show_progress=True,
                use_multithreading=True,
            )
            documents.extend(loader_docx.load())
        except Exception as e:
            print(f"Error loading DOCX files: {str(e)}")

        try:
            loader_pdf = DirectoryLoader(
                directory_path,
                glob="**/*.pdf",
                loader_cls=pdf_loader,
                show_progress=True,
                use_multithreading=True,
            )
            documents.extend(loader_pdf.load())
        except Exception as e:
            print(f"Error loading PDF files: {str(e)}")

        try:
            loader_txt = DirectoryLoader(
                directory_path,
                glob="**/*.txt",
                loader_cls=txt_loader,
                show_progress=True,
                use_multithreading=True,
            )
            documents.extend(loader_txt.load())
        except Exception as e:
            print(f"Error loading TXT files: {str(e)}")

        try:
            loader_pptx = DirectoryLoader(
                directory_path,
                glob="**/*.pptx",
                loader_cls=pptx_loader,
                show_progress=True,
                use_multithreading=True,
            )
            documents.extend(loader_pptx.load())
        except Exception as e:
            print(f"Error loading PPTX files: {str(e)}")

        try:
            loader_xlsx = DirectoryLoader(
                directory_path,
                glob="**/*.xlsx",
                loader_cls=excel_loader,
                show_progress=True,
                use_multithreading=True,
            )
            documents.extend(loader_xlsx.load())
        except Exception as e:
            print(f"Error loading XLSX files: {str(e)}")

        try:
            loader_xls = DirectoryLoader(
                directory_path,
                glob="**/*.xls",
                loader_cls=excel_loader,
                show_progress=True,
                use_multithreading=True,
            )
            documents.extend(loader_xls.load())
        except Exception as e:
            print(f"Error loading XLS files: {str(e)}")

        if not documents:
            print(f"No documents were loaded from {directory_path}")
            return []

        return split_docs(documents, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    except Exception as e:
        print(f"Error in load_documents_from_directory: {str(e)}")
        return []
