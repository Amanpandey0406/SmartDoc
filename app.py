import streamlit as st
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains import RetrievalQA
import time

# Configure Streamlit page
st.set_page_config(
    page_title="SmartDoc",
    page_icon="⭐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Color palette
colors = {
    "primary": "#333333",
    "secondary": "#555555",
    "accent": "#777777",
    "background": "#F8F9FA",
    "surface": "#FFFFFF",
    "text": "#1B1B1B",
    "success": "#4CAF50",
    "error": "#F44336",
    "warning": "#FF9800"
}

# Custom CSS with enhanced styling
st.markdown(f"""
    <style>
    /* Global Styles */
    .stApp {{
        background-color: {colors["background"]};
        color: {colors["text"]};
    }}
    
    /* Headers */
    h1, h2, h3 {{
        color: {colors["primary"]};
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 600;
    }}
    
    /* Buttons */
    .stButton>button {{
        background: linear-gradient(45deg, {colors["primary"]}, {colors["accent"]});
        color: white;
        border-radius: 8px;
        border: none;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: 500;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }}
    .stButton>button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }}
    
    /* Text Input */
    .stTextInput>div>div>input {{
        border: 2px solid {colors["primary"]};
        border-radius: 8px;
        padding: 12px;
        font-size: 16px;
        transition: all 0.3s ease;
    }}
    .stTextInput>div>div>input:focus {{
        border-color: {colors["accent"]};
        box-shadow: 0 0 0 2px rgba(51, 51, 51, 0.1);
    }}
    
    /* File Uploader */
    .stFileUploader>div>div>div>button {{
        background: linear-gradient(45deg, {colors["secondary"]}, {colors["primary"]});
        color: white;
        border-radius: 8px;
        border: none;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: 500;
        transition: all 0.3s ease;
    }}
    
    /* Custom Cards */
    .custom-card {{
        background-color: {colors["surface"]};
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 10px 0;
    }}
    
    /* Response Container */
    .response-container {{
        background-color: {colors["surface"]};
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid {colors["primary"]};
        margin: 20px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    
    /* Progress Bar */
    .stProgress > div > div > div > div {{
        background-color: {colors["primary"]};
    }}
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'pdf_processed' not in st.session_state:
    st.session_state.pdf_processed = False

# Sidebar
with st.sidebar:
    # st.title("⭐ Build a RAG System")
    # st.markdown("---")
    st.markdown("""
    ### How to use:
    1. Upload your PDF document
    2. Wait for processing
    3. Ask questions about the content
    4. Get AI-powered responses
    
    ### Features:
    - 📚 PDF Analysis
    - 🔍 Semantic Search
    - 💡 Smart Responses
    - 📝 Chat History
    """)
    st.markdown("---")
    st.markdown("Made by Aman Pandey")

# Main content
st.title("SmartDoc: AI-Powered Document Analysis using DeepSeek & Ollama")
st.markdown("### Upload your document and start asking questions")

# File upload with progress bar
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", key="pdf_uploader")

if uploaded_file and not st.session_state.pdf_processed:
    with st.spinner("Processing your PDF... Please wait"):
        # Show progress bar
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        
        # Save and process PDF
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getvalue())
        
        # Initialize components
        loader = PDFPlumberLoader("temp.pdf")
        docs = loader.load()
        text_splitter = SemanticChunker(HuggingFaceEmbeddings())
        documents = text_splitter.split_documents(docs)
        embedder = HuggingFaceEmbeddings()
        vector = FAISS.from_documents(documents, embedder)
        retriever = vector.as_retriever(search_type="similarity", search_kwargs={"k": 3})
        
        # Initialize LLM and chains
        llm = Ollama(model="deepseek-r1")
        prompt = """
        Based on the provided context, please answer the question:
        
        Context: {context}
        
        Question: {question}
        
        Instructions:
        1. Only use information from the context
        2. If unsure, respond with "I don't know"
        3. Keep answers concise (3-4 sentences)
        4. Be clear and direct
        
        Answer:"""
        
        QA_CHAIN_PROMPT = PromptTemplate.from_template(prompt)
        llm_chain = LLMChain(llm=llm, prompt=QA_CHAIN_PROMPT)
        document_prompt = PromptTemplate(
            input_variables=["page_content", "source"],
            template="Content: {page_content}\nSource: {source}"
        )
        
        combine_documents_chain = StuffDocumentsChain(
            llm_chain=llm_chain,
            document_variable_name="context",
            document_prompt=document_prompt
        )
        
        st.session_state.qa = RetrievalQA(
            combine_documents_chain=combine_documents_chain,
            retriever=retriever,
            return_source_documents=True
        )
        
        st.session_state.pdf_processed = True
        st.success("✅ PDF processed successfully!")

# Question input section
if st.session_state.pdf_processed:
    st.markdown("### Ask Your Question")
    col1, col2 = st.columns([4, 1])
    
    with col1:
        user_input = st.text_input(
            "Type your question here",
            placeholder="What would you like to know about the document?",
            key="question_input"
        )
    
    with col2:
        ask_button = st.button("Ask 🔍", use_container_width=True)

    # Process question and display response
    if ask_button and user_input:
        with st.spinner("🤔 Thinking..."):
            try:
                response = st.session_state.qa(user_input)
                
                # Add to chat history
                st.session_state.chat_history.append({
                    "question": user_input,
                    "answer": response["result"]
                })
                
                # Display response in custom container
                st.markdown("""
                    <div class="response-container">
                        <h4>Answer:</h4>
                        <p>{}</p>
                    </div>
                """.format(response["result"]), unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")

    # Display chat history
    if st.session_state.chat_history:
        st.markdown("### 📝 Chat History")
        for i, chat in enumerate(st.session_state.chat_history):
            with st.expander(f"Q: {chat['question']}", expanded=False):
                st.markdown(f"**Answer:** {chat['answer']}")

else:
    # Welcome message
    st.markdown("""
        <div class="custom-card">
            <h3>👋 Welcome!</h3>
            <p>Get started by uploading a PDF document. Once processed, you can:</p>
            <ul>
                <li>Ask questions about the content</li>
                <li>Get AI-powered answers</li>
                <li>View your chat history</li>
                <li>Export conversations</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)