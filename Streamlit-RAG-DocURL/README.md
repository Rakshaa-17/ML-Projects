## Streamlit RAG Chatbot for Document and URL-Based QA
This project is a Streamlit-powered Retrieval-Augmented Generation (RAG) Chatbot designed to answer user queries based on the contents of a PDF and document URL. By leveraging embeddings and vector similarity search, the chatbot retrieves the most relevant information from the document and responds using a language model.

### 🚀 Project Features
- 🔗 Upload a PDF or provide a document URL
- 🧠 Embeds the document using SentenceTransformer or OpenAI Embeddings
- 🔍 Performs semantic search using FAISS vector store
- 💬 Generates context-aware answers using a language model (e.g., OpenAI GPT)
- 🌐 Simple and interactive Streamlit web interface

### 🛠️ Technologies Used
- Streamlit – for building the interactive web app
- FAISS – for fast vector similarity search
- PyPDF2 – to extract text from PDF documents
- SentenceTransformers / OpenAI Embeddings – for converting text into embeddings
- OpenAI GPT / Chat Models – to generate responses based on context

### 🧪 How It Works
- Upload Document / Paste URL: User uploads a PDF or provides a document URL.
- Text Extraction: The content is extracted from the PDF.
- Embedding Generation: The extracted text is chunked and converted to vector embeddings.
- FAISS Indexing: These embeddings are stored in a FAISS index.
- Query Processing: User inputs a question; it's embedded and matched with relevant chunks.
- Answer Generation: Top chunks are passed to an LLM to generate the final answer.

### 📝 Example Use Cases
- 📚 Academic paper Q&A
- 📄 Contract understanding
- 📊 Company report summarization
- 🧠 Knowledge base assistant

 ### 🧑‍💻 Author
Developed by [Raksha](https://github.com/Rakshaa-17)

Let's connect [LinkedIn](https://www.linkedin.com/in/rakshamalela/)
