# Pinecone RAG System

Un sistema de Retrieval-Augmented Generation (RAG) que utiliza Pinecone como base de datos vectorial y LangChain para el procesamiento de documentos e interacciones con IA.

## 🚀 Características

- **Carga de Documentos**: Soporte para múltiples formatos de archivo (PDF, DOCX, TXT, PPTX, XLSX, XLS)
- **Procesamiento Inteligente**: División automática de documentos en chunks con overlap configurable
- **Base de Datos Vectorial**: Integración con Pinecone para almacenamiento y búsqueda de embeddings
- **IA Conversacional**: Integración con OpenAI GPT-4 para respuestas basadas en contexto
- **Configuración Flexible**: Parámetros personalizables para chunk size y overlap

## 📋 Requisitos

- Python 3.13 o superior
- Cuenta de Pinecone
- API Key de OpenAI

## 🛠️ Instalación

1. **Clona el repositorio**:
   ```bash
   git clone <repository-url>
   cd pinecone-rag
   ```

2. **Instala las dependencias**:
   ```bash
   pip install -e .
   ```

3. **Instala las dependencias de desarrollo** (opcional):
   ```bash
   pip install -e ".[dev]"
   ```

4. **Configura las variables de entorno**:
   Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:
   ```env
   PINECONE_API_KEY=tu_api_key_de_pinecone
   BTECH_OPENAI_API_KEY_MERMAID=tu_api_key_de_openai
   ```

## 🏗️ Estructura del Proyecto

```
pinecone-rag/
├── app/
│   ├── ai/
│   │   ├── __init__.py
│   │   └── llm_config.py          # Configuración de LLM y prompts
│   ├── loader/
│   │   ├── __init__.py
│   │   └── docs_loader.py         # Cargador de documentos
│   └── pinecone_db_services/
│       ├── __init__.py
│       ├── config.py              # Configuración de Pinecone
│       └── add_docs.py            # Servicios para agregar documentos
├── docs/                          # Documentos de ejemplo
├── main.py                        # Punto de entrada principal
├── pyproject.toml                 # Configuración del proyecto
└── README.md                      # Este archivo
```

## 📖 Uso

### 1. Cargar Documentos

El sistema puede cargar documentos desde un directorio o archivo individual:

```python
from app.loader.docs_loader import load_documents_from_directory

# Cargar desde un directorio
documents = load_documents_from_directory(
    directory_path="./docs",
    chunk_size=800,
    chunk_overlap=100
)

# Cargar un archivo individual
documents = load_documents_from_directory(
    directory_path="./docs/documento.pdf",
    chunk_size=800,
    chunk_overlap=100
)
```

### 2. Agregar Documentos a Pinecone

```python
from app.pinecone_db_services.add_docs import add_docs_into_vector_store

# Agregar documentos al vector store
success = add_docs_into_vector_store(documents)
if success:
    print("Documentos agregados exitosamente")
```

### 3. Realizar Consultas RAG

```python
from app.ai.llm_config import State, retrieve, generate

# Crear un estado para la consulta
state = State(question="¿Cuál es la experiencia de Reynaldo Suarez?")

# Recuperar documentos relevantes
state = retrieve(state)

# Generar respuesta
state = generate(state)

print(f"Respuesta: {state.answer}")
```

## ⚙️ Configuración

### Parámetros de Chunking

- **chunk_size**: Tamaño de cada chunk (por defecto: 800)
- **chunk_overlap**: Overlap entre chunks (por defecto: 100)

### Configuración de Pinecone

- **Index Name**: `langchain-test-index` (configurable en `app/pinecone_db_services/config.py`)
- **Dimension**: 3072 (para embeddings de OpenAI)
- **Metric**: Cosine similarity
- **Cloud**: AWS us-east-1

### Modelos de IA

- **Embeddings**: `text-embedding-3-large` (OpenAI)
- **LLM**: `gpt-4o` (OpenAI)

## 📁 Formatos de Archivo Soportados

- **PDF**: Documentos PDF
- **DOCX**: Documentos de Word
- **TXT**: Archivos de texto plano
- **PPTX**: Presentaciones de PowerPoint
- **XLSX/XLS**: Hojas de cálculo de Excel

## 🔧 Desarrollo

### Herramientas de Desarrollo

El proyecto incluye las siguientes herramientas de desarrollo:

- **Black**: Formateador de código
- **Ruff**: Linter y formateador
- **Codespell**: Verificador de ortografía
- **Pre-commit**: Hooks de pre-commit

### Ejecutar Herramientas de Desarrollo

```bash
# Formatear código
black .

# Linting
ruff check .

# Verificar ortografía
codespell .

# Instalar hooks de pre-commit
pre-commit install
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🆘 Soporte

Si tienes problemas o preguntas:

1. Revisa la documentación
2. Busca en los issues existentes
3. Crea un nuevo issue con detalles del problema

## 🔄 Roadmap

- [ ] Interfaz web para consultas
- [ ] Soporte para más formatos de archivo
- [ ] Optimización de embeddings
- [ ] Sistema de caché para consultas frecuentes
- [ ] Métricas y monitoreo