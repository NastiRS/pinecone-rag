# pinecone-rag

Este proyecto es una base para implementar un sistema de Recuperación Aumentada por Generación (RAG) usando Pinecone y modelos de lenguaje de OpenAI.

## Características principales
- Carga y procesamiento de documentos en formatos PDF, Word, PowerPoint, Excel y texto.
- Almacenamiento y búsqueda semántica de documentos usando Pinecone.
- Generación de respuestas a preguntas usando modelos de lenguaje de OpenAI (GPT-4o).

## Requisitos
- Python 3.13
- Claves de API para OpenAI y Pinecone (definidas en variables de entorno)

## Instalación
1. Clona este repositorio.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt  # O usa pyproject.toml con tu gestor preferido
   ```
3. Crea un archivo `.env` con tus claves de API:
   ```env
   PINECONE_API_KEY=tu_clave_pinecone
   BTECH_OPENAI_API_KEY_MERMAID=tu_clave_openai
   ```

## Uso
Ejecuta el archivo principal:
```bash
python main.py
```

## Estructura del proyecto
- `app/ai/llm_config.py`: Configuración del modelo de lenguaje y lógica RAG.
- `app/loader/docs_loader.py`: Carga y procesamiento de documentos.
- `app/pinecone_db_services/`: Configuración y operaciones con Pinecone.
- `docs/`: Ejemplos de documentos de prueba.

## Calidad de código
Incluye configuración para pre-commit con herramientas como Ruff, Black y Codespell.

---
Proyecto base para experimentos con RAG y Pinecone.