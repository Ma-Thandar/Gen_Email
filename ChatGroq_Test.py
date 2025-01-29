import streamlit as st
from datetime import date
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
#import chromadb


# chroma_client = chromadb.Client()
# collection = chroma_client.create_collection(name="new_collection")
st.set_page_config(layout="wide")
st.title("Hello Warzo")

prompt = "the man who created electric bulb"

llm = ChatGroq(    
    temperature=0,
    groq_api_key='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',
    model_name='llama-3.3-70b-versatile'  
)
response = llm.invoke(prompt)
#print(response.content)
st.write("Results ", response.content)
st.write("********************************************************************************************")


#loader = WebBaseLoader("https://jobs.nike.com/job/R-49848?from=job%20search%20funnel")
#https://jobs.nike.com/job/R-33460
#page_data=loader.load().pop().page_content
#print(page_data)
#st.write(page_data)
