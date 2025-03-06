# Building a Question-Answering System with Langchain and Streamlit

In this blog post, I'll walk you through the process of building a simple question-answering system using Langchain and deploying it with Streamlit. This project was part of my NLP course, where I explored the use of Retrieval-Augmented Generation (RAG) to create an LLM-based application.

## What is RAG?

Retrieval-Augmented Generation (RAG) is a method that combines the strengths of retrieval-based and generation-based models. It retrieves relevant documents from a corpus and then generates an answer based on the retrieved information.

## How It Works

1. **Document Loading**: The system loads a text file provided by the user.
2. **Embedding Creation**: The text is split into chunks, and embeddings are created using HuggingFace's pre-trained models.
3. **Question Answering**: The system uses OpenAI's GPT model to generate answers based on the retrieved documents.

## Deployment with Streamlit

Streamlit makes it easy to deploy machine learning models as web applications. The app allows users to upload a text file and ask questions based on its content.

## Conclusion

This project was a great way to explore the capabilities of Langchain and Streamlit. It demonstrated how powerful LLMs can be when combined with retrieval methods, and how easy it is to deploy such systems using Streamlit.
