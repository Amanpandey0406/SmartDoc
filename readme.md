# SmartDoc: AI-Powered Document Analysis using DeepSeek & Ollama

SmartDoc is an intelligent document analysis system that leverages the power of DeepSeek and Ollama to provide smart, context-aware responses to questions about your PDF documents. Built with Streamlit and LangChain, it offers an intuitive interface for document processing and information retrieval.

## 🌟 Features

- 📚 PDF Document Analysis
- 🔍 Semantic Search Capability
- 💡 Intelligent Question Answering
- 📝 Chat History Tracking
- 🎯 Context-Aware Responses
- 🚀 Real-time Processing

## 📸 Application Screenshots

### Main Interface
![Main Interface](path_to_main_interface.png)
The main interface provides a clean, user-friendly design where you can upload your PDF documents and interact with the AI.

### PDF Upload Process
![PDF Upload](path_to_pdf_upload.png)
Simply drag and drop or click to upload your PDF document. The system will process it automatically.

### Question Asking Interface
![Question Interface](path_to_question_interface.png)
After processing, you can ask questions about your document's content using natural language.

### Answer Display
![Answer Display](path_to_answer_display.png)
Get clear, context-aware answers derived directly from your document's content.

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/smartdoc.git
cd smartdoc
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Install Ollama:
- For Mac/Linux:
```bash
curl https://ollama.ai/install.sh | sh
```
- For Windows:
  - Download from [Ollama Website](https://ollama.ai/download/windows)

5. Pull the DeepSeek model:
```bash
ollama pull deepseek
```

## 🚀 Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Upload a PDF document:
   - Click the upload button or drag and drop your PDF
   - Wait for processing to complete

4. Ask questions:
   - Type your question in the input field
   - Click "Ask" or press Enter
   - View the AI-generated response

5. View chat history:
   - Scroll down to see previous Q&A pairs
   - Click to expand/collapse individual conversations

## 💡 Tips for Better Results

- Upload clear, well-formatted PDF documents
- Ask specific questions
- Provide context in your questions when needed
- Review chat history for related information

## 🔧 Troubleshooting

Common issues and solutions:

1. **Ollama Model Not Found**
```bash
ollama pull deepseek
```

2. **PDF Processing Error**
- Ensure PDF is not password protected
- Check PDF is readable and not corrupted
- Verify file size is within limits

3. **Slow Response Times**
- Check your internet connection
- Ensure Ollama is running
- Consider reducing PDF file size

## 👨‍💻 Developer

Made with ❤️ by Aman Pandey

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

