import streamlit as st
from datetime import date
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate



# chroma_client = chromadb.Client()
# collection = chroma_client.create_collection(name="new_collection")
st.set_page_config(layout="wide")
st.title("Hello Warzo")

#prompt = "the man who created electric bulb"
prompt = "the man who worked on the moon first"

llm = ChatGroq(    
    temperature=0,
    groq_api_key='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',
    model_name='llama-3.3-70b-versatile'  
)
response = llm.invoke(prompt)
#print(response.content)
st.write("Results ", response.content)
st.write("********************************************************************************************")
st.markdown("<h3 style='text-align: center; color: violet;'>Page Content ♈ ♉ ♓</h2>", unsafe_allow_html=True)


loader = WebBaseLoader("https://careers.nike.com/lead-ai-ml-engineer/job/R-48983")
#https://jobs.nike.com/job/R-33460
#https://jobs.nike.com/job/R-49848?from=job%20search%20funnel
page_data=loader.load().pop().page_content
#print(page_data)
st.write(page_data)
st.write("********************************************************************************************")
st.markdown("<h3 style='text-align: center; color: violet;'>Extract Content and JSON Format ♈ ♉ ♓</h2>", unsafe_allow_html=True)

prompt_extract = PromptTemplate.from_template(
    """
    ###Scraped text from the website :
    {page_data}
    ### Instruction:
    The scraped text is from the career's page of a website.
    Your job is to extract the job posting and return them in JSON format containing the following keys: 
    'role', 'experience', 'skills' and 'description'.
    Only return the valid JSON.
    ### Valid JSON (No Preamble):
    """
)
chain_extract = prompt_extract | llm
res = chain_extract.invoke(input={'page_data':page_data})
#st.write(res.content)
#st.write(type(res.content))

st.write("********************************************************************************************")
st.markdown("<h3 style='text-align: center; color: violet;'>JSON Parser ♈ ♉ ♓</h2>", unsafe_allow_html=True)

from langchain_core.output_parsers import JsonOutputParser
json_parser=JsonOutputParser()
json_res=json_parser.parse(res.content)
st.write(json_res)
#st.write(type(json_res))

st.write("********************************************************************************************")
st.markdown("<h3 style='text-align: center; color: violet;'>TechStack ♈ ♉ ♓</h2>", unsafe_allow_html=True)

import pandas as pd
df = pd.read_csv('./TechStack.csv')
st.write(df)

#import chromadb as cmdb
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")
