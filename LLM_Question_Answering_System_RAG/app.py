import streamlit as st
from scripts.rag_pipeline import load_documents, create_embeddings, create_qa_chain, answer_question

# Streamlit app
st.title("LLM Question Answering System, by Bernardo Xavier")
st.write("Let's get in touch: https://www.linkedin.com/in/bernardo-xavier-da-silva/ | https://github.com/Bernardo-Xavier")
st.write("Upload a text file and ask questions based on its content.")

# File upload
uploaded_file = st.file_uploader("Upload a text file", type="txt")
if uploaded_file is not None:
    file_path = "uploaded_file.txt"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Load documents and create QA chain
    documents = load_documents(file_path)
    db = create_embeddings(documents)
    qa_chain = create_qa_chain(db)
    
    # Question input
    question = st.text_input("Enter your question:")
    if question:
        answer = answer_question(qa_chain, question)
        st.write("Answer:")
        st.write(answer)