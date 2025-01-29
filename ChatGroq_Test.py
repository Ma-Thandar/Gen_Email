import streamlit as st
from datetime import date
from langchain_groq import ChatGroq
#import chromadb


# chroma_client = chromadb.Client()
# collection = chroma_client.create_collection(name="new_collection")

prompt = "the man who created electric bulb"

llm = ChatGroq(    
    temperature=0,
    groq_api_key='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',
    model_name='llama-3.1-70b-versatile'  
)
response = llm.invoke(prompt)
#print(response.content)
st.write("Results ", response.content)

st.set_page_config(layout="wide")
st.title("Hello Warzo")
