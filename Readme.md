# Document Analyzer

Document Analyzer is a tool that analyzes a document and generates questions based on its content. Users can interact with the chat bot to receive responses relevant to the document.

## Technologies Used

The application leverages the DeBERTa model available from Hugging Face for document analysis. Serverless inference points are utilized to run the inference, ensuring scalability and efficiency. The frontend interface is built using Streamlit, providing a user-friendly experience.

### Technologies:
- [DeBERTa Model](https://github.com/microsoft/DeBERTa) - DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing

## Usage

To run the application, ensure that the required dependencies are installed. Then, execute the following command:

```bash
streamlit run main.py
