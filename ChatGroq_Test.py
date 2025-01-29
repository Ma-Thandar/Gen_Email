import streamlit as st
from datetime import date
from langchain_groq import ChatGroq
import chromadb

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")

st.set_page_config(layout="wide")


st.title("Hello Warzo")
