## 🤖 RAG Chatbot – Question Answering from Custom Text Input
This project demonstrates a Retrieval-Augmented Generation (RAG) Chatbot built in a Jupyter Notebook that answers user questions based on a manually provided text. It uses semantic search to retrieve relevant context and generates answers using a language model (like OpenAI’s GPT).

### 📌 Objective
- To build a lightweight QA system that:
- Accepts a custom sample text
- Embeds and stores the text for retrieval
- Uses semantic similarity to fetch relevant context
- Generates accurate and contextual responses to user questions

### 🧠 What is RAG?
- RAG (Retrieval-Augmented Generation) combines:
- 🔍 Retrieval: Finding the most relevant pieces of text for a given query.
- 🧾 Generation: Using an LLM to generate a response based on retrieved content.

### 🧪 How It Works
- Input Sample Text: The user provides some informative text (e.g., a paragraph or article).
- Text Chunking: The text is split into manageable segments.
- Embedding Generation: Each chunk is converted to a vector using SentenceTransformer.
- FAISS Indexing: Chunks are stored in a vector database (FAISS).
- User Question: A question is embedded and matched with relevant chunks.
- Answer Generation: The top-matched text chunks are sent to the LLM (e.g., GPT) to generate an answer.

### 🛠️ Tech Stack
- Python
- SentenceTransformers – to create embeddings
- FAISS – for similarity search
- OpenAI API – for response generation (if used)
- Jupyter Notebook

### ✅ Applications
- Learning assistant for notes and passages
- Q&A over summaries or articles
- FAQ bot over custom business content

### 👩‍💻 Author
Developed by [Raksha](https://github.com/Rakshaa-17)

Let's connect [LinkedIn](https://www.linkedin.com/in/rakshamalela/)
