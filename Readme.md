# Document Analyzer

Document Analyzer is an application designed to analyze PDF documents and generate answers based on their content. The application utilizes  natural language processing models, such as DeBERTa from Hugging Face, to extract key information from the documents. Users can interact with the chat bot interface to ask questions about the document's content, and the bot will provide responses based on the analysis.


## Technologies Used

The application leverages the DeBERTa model available from Hugging Face for document analysis. Serverless inference points are utilized to run the inference, ensuring scalability and efficiency. The frontend interface is built using Streamlit, providing a user-friendly experience.

### Technologies:
- [DeBERTa Model](https://github.com/microsoft/DeBERTa) - DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing

## Usage

To run the application, ensure that the required dependencies are installed. Then, execute the following command:

```bash
streamlit run main.py
