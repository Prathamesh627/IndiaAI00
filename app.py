import streamlit as sr
from dotenv import load_dotenv 
from PyPDF2 import PdfReader

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def main():
    load_dotenv()
    sr.set_page_config(page_title="Bondify", page_icon=":pen:")
    sr.header("Chat with your Bond Assistant")
    sr.text_input("Ask Anything on the electoral bonds:")
    with sr.sidebar:
        sr.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if sr.button("Process"):
            with sr.spinner("Processing"):
                #pdf to text
                raw_text=get_pdf_text(pdf_docs)

                #text to text chunks

                #creating vector store



if __name__=='__main__':
    main()
