from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

def load_documents(file_path):
    loader = TextLoader(file_path)
    documents = loader.load()
    return documents

def create_embeddings(documents):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(texts, embeddings)
    return db

def create_qa_chain(db):
    llm = OpenAI(temperature=0, openai_api_key="YOUR_API_KEY_HERE") # Input your api key here to run the application
    qa_chain = RetrievalQA.from_chain_type(llm, chain_type="stuff", retriever=db.as_retriever())
    return qa_chain

def answer_question(qa_chain, question):
    return qa_chain.run(question)