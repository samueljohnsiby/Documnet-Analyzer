import dotenv
import os
import requests
import streamlit as st
from pypdf import PdfReader


dotenv.load_dotenv()






class HuggingFaceQuery:
    def __init__(self, api_url, headers, file):
        self.api_url = api_url
        self.headers = headers
        self.file = file
        self.text = ""

    def query(self, payload):
        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            response_data = response.json()

            result = response_data.get('answer')
            score = response_data.get('score')
        
         

            if result is not None and score > 0.3:
                return result
            else:
                return "Sorry, I am not sure."

        except requests.exceptions.RequestException as e:
            return f"Error: {e}"

    def read_pdf(self):
        try:
            # Check if a file is uploaded
            if self.file is not None:
                # Open the uploaded file in binary mode
                with self.file:
                    pdf_reader = PdfReader(self.file)
                    num_pages = len(pdf_reader.pages)
                    text = ""

                    # Iterate through each page and extract text
                    for page_num in range(num_pages):
                        page = pdf_reader.pages[page_num]
                        text += " ".join(page.extract_text().split())  

                    return text
        except Exception as e:
            print(f"Error: {e}")
            
    def get_answer_from_context(self, question):
        self.text = self.read_pdf()
        if self.text:
            return self.query({
                "inputs": {
                    "question": question,
                    "context": self.text
                },
            })
        else:
            return "Error reading PDF."

def main():

    #Initilize variables

    API_KEY = os.getenv('api_key')
    API_URL = "https://api-inference.huggingface.co/models/timpal0l/mdeberta-v3-base-squad2"
    headers = {"Authorization": "Bearer " + API_KEY}
    print(f"headers: {headers}")

    
    # Upload Pdf 
    st.title("PDF Uploader and Text Analyzer")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    

    if uploaded_file:

        model = HuggingFaceQuery(api_url=API_URL,file=uploaded_file,headers=headers)

            # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])




        # React to user input
        if prompt := st.chat_input("Enter your Question"):
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})

            print(f"prompt:{prompt}")

            response = model.get_answer_from_context(question=prompt)
            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                st.markdown(response)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})

    

           
        

            

if __name__ == "__main__":

    main()
