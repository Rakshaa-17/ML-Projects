import streamlit as st
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import PyPDF2
import requests
from bs4 import BeautifulSoup
import re
from typing import List
import pickle
import os
from together import Together

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'vector_store' not in st.session_state:
    st.session_state.vector_store = None
if 'chunks' not in st.session_state:
    st.session_state.chunks = []
if 'embeddings_model' not in st.session_state:
    st.session_state.embeddings_model = None

@st.cache_resource
def load_embedding_model():
    """Load the sentence transformer model"""
    return SentenceTransformer('all-MiniLM-L6-v2')

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """Split text into overlapping chunks"""
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
        if i + chunk_size >= len(words):
            break
    
    return chunks

def extract_text_from_pdf(pdf_file) -> str:
    """Extract text from uploaded PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"
        if not text.strip():
            st.warning(f"No text extracted from PDF: {pdf_file.name}")
        return text
    except Exception as e:
        st.error(f"Error reading PDF {pdf_file.name}: {str(e)}")
        return ""

def extract_text_from_url(url: str) -> str:
    """Extract text from URL"""
    try:
        if not url.startswith(('http://', 'https://')):
            st.error(f"Invalid URL format: {url}")
            return ""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        for script in soup(["script", "style"]):
            script.decompose()
        
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        if not text.strip():
            st.warning(f"No text extracted from URL: {url}")
        return text
    except Exception as e:
        st.error(f"Error fetching URL {url}: {str(e)}")
        return ""

def save_vector_store(index, chunks, index_path="index.faiss", chunks_path="chunks.pkl"):
    """Save FAISS index and chunks to disk"""
    try:
        faiss.write_index(index, index_path)
        with open(chunks_path, 'wb') as f:
            pickle.dump(chunks, f)
    except Exception as e:
        st.error(f"Error saving vector store: {str(e)}")

def load_vector_store(index_path="index.faiss", chunks_path="chunks.pkl"):
    """Load FAISS index and chunks from disk"""
    try:
        if os.path.exists(index_path) and os.path.exists(chunks_path):
            index = faiss.read_index(index_path)
            with open(chunks_path, 'rb') as f:
                chunks = pickle.load(f)
            return index, chunks
        return None, []
    except Exception as e:
        st.error(f"Error loading vector store: {str(e)}")
        return None, []

def create_vector_store(chunks: List[str], embedding_model) -> faiss.IndexFlatIP:
    """Create FAISS vector store from text chunks"""
    if not chunks:
        st.error("No chunks available to create vector store.")
        return None
    
    try:
        embeddings = embedding_model.encode(chunks)
        embeddings = embeddings.astype('float32')
        faiss.normalize_L2(embeddings)
        
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatIP(dimension)
        index.add(embeddings)
        
        return index
    except Exception as e:
        st.error(f"Error creating vector store: {str(e)}")
        return None

def search_similar_chunks(query: str, vector_store, chunks: List[str], embedding_model, k: int = 10) -> List[str]:
    """Search for similar chunks in the vector store"""
    if vector_store is None or not chunks:
        st.error("No vector store available. Please process documents first.")
        return []
    
    try:
        query_embedding = embedding_model.encode([query]).astype('float32')
        faiss.normalize_L2(query_embedding)
        scores, indices = vector_store.search(query_embedding, k)
        relevant_chunks = [chunks[i] for i in indices[0] if i < len(chunks)]
        return relevant_chunks
    except Exception as e:
        st.error(f"Error searching vector store: {str(e)}")
        return []

def generate_response(query: str, context: List[str], together_client) -> str:
    """Generate response using Together AI"""
    if not context:
        return "I don't have enough context to answer your question. Please upload some documents first."
    
    context_text = "\n\n".join(context)
    prompt = f"""Based on the following context, please answer the question. If the answer is not in the context, say so.

Context:
{context_text}

Question: {query}

Answer:"""
    
    try:
        response = together_client.chat.completions.create(
            model="meta-llama/Llama-3-8b-chat-hf",  # Updated to a likely valid model
            messages=[{"role": "user", "content": prompt}],
            max_tokens=512,
            temperature=0.3,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {str(e)}"

def main():
    st.set_page_config(page_title="RAG Chatbot", page_icon="🤖", layout="wide")
    
    st.title("🤖 RAG Chatbot")
    st.markdown("Upload PDFs or provide URLs to chat with your documents!")
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("Configuration")
        
        # Together AI API Key
        together_api_key = st.text_input(
            "Together AI API Key", 
            type="password", 
            help="Get your API key from https://api.together.xyz/"
        )
        
        if together_api_key:
            together_client = Together(api_key=together_api_key)
        else:
            together_client = None
            st.warning("Please enter your Together AI API key to use the chatbot.")
        
        # Chunk size and overlap configuration
        chunk_size = st.slider("Chunk Size (words)", 100, 1000, 500)
        overlap = st.slider("Chunk Overlap (words)", 0, 200, 50)
        
        st.header("Document Sources")
        
        # File uploader
        uploaded_files = st.file_uploader(
            "Upload PDF files",
            type=['pdf'],
            accept_multiple_files=True
        )
        
        # URL input
        urls = st.text_area("Enter URLs (one per line)", height=100)
        url_list = [url.strip() for url in urls.split('\n') if url.strip()]
        
        # Load existing vector store
        if st.button("Load Existing Vector Store"):
            index, chunks = load_vector_store()
            if index is not None and chunks:
                st.session_state.vector_store = index
                st.session_state.chunks = chunks
                st.success(f"Loaded vector store with {len(chunks)} chunks!")
            else:
                st.warning("No existing vector store found or error loading.")
        
        # Process documents button
        if st.button("Process Documents"):
            if uploaded_files or url_list:
                with st.spinner("Processing documents..."):
                    # Load embedding model
                    if st.session_state.embeddings_model is None:
                        st.session_state.embeddings_model = load_embedding_model()
                    
                    all_chunks = []
                    
                    # Process PDFs
                    for pdf_file in uploaded_files:
                        text = extract_text_from_pdf(pdf_file)
                        if text:
                            chunks = chunk_text(text, chunk_size, overlap)
                            all_chunks.extend(chunks)
                            st.success(f"Processed PDF: {pdf_file.name}")
                    
                    # Process URLs
                    for url in url_list:
                        text = extract_text_from_url(url)
                        if text:
                            chunks = chunk_text(text, chunk_size, overlap)
                            all_chunks.extend(chunks)
                            st.success(f"Processed URL: {url}")
                    
                    if all_chunks:
                        # Create vector store
                        st.session_state.vector_store = create_vector_store(
                            all_chunks, st.session_state.embeddings_model
                        )
                        if st.session_state.vector_store:
                            st.session_state.chunks = all_chunks
                            save_vector_store(st.session_state.vector_store, all_chunks)
                            st.success(f"Created vector store with {len(all_chunks)} chunks!")
                        else:
                            st.error("Failed to create vector store.")
                    else:
                        st.error("No content was extracted from the provided sources.")
            else:
                st.warning("Please upload files or provide URLs first.")
        
        # Display current status
        if st.session_state.vector_store is not None:
            st.success(f"Vector store ready with {len(st.session_state.chunks)} chunks")
        else:
            st.info("No documents processed yet")
    
    # Main chat interface
    if together_client and st.session_state.vector_store is not None:
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Ask a question about your documents..."):
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Generate response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    # Search for relevant chunks
                    relevant_chunks = search_similar_chunks(
                        prompt,
                        st.session_state.vector_store,
                        st.session_state.chunks,
                        st.session_state.embeddings_model
                    )
                    
                    # Generate response
                    response = generate_response(prompt, relevant_chunks, together_client)
                    st.markdown(response)
            
            # Add assistant response
            st.session_state.messages.append({"role": "assistant", "content": response})
    
    elif not together_client:
        st.info("👈 Please enter your Together AI API key in the sidebar to start chatting.")
    else:
        st.info("👈 Please process some documents first using the sidebar.")
    
    # Clear chat button
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

if __name__ == "__main__":
    main()