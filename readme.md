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
![our_app](https://github.com/user-attachments/assets/8ebe7f41-3f16-4cf3-89b0-4e2bf8b9f9e1)
The main interface provides a clean, user-friendly design where you can upload your PDF documents and interact with the AI.

### PDF Upload Process
![PDF_Uploaded](https://github.com/user-attachments/assets/9a9a7dd9-50fc-4b35-83c9-edd43362e81b)
Simply drag and drop or click to upload your PDF document. The system will process it automatically.

### Question Asking Interface
![processing](https://github.com/user-attachments/assets/27695220-c17c-49ab-bf8b-8ac39f7f0edb)
After processing, you can ask questions about your document's content using natural language.

### Answer Display
![Answer](https://github.com/user-attachments/assets/6de4b3a7-517e-44b7-ad61-ec7cb575b4d8)
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

Made by Aman Pandey

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

