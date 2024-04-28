import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import BedrockEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator
from langchain_aws import BedrockLLM
import requests

SOURCE_PDF_FINLAND = "https://www.prh.fi/material/sites/prh/attachments/patentinliitteet/xdzzfkx7q/Patent_regulations_2023.pdf"
SOURCE_PDF_ITALY="https://uibm.mise.gov.it/images/DLgs_10_febbraio_2005_n_30.pdf"
MODEL_ID_LLAMA =  'meta.llama2-70b-chat-v1'
MODEL_ID_CLAUDE = 'anthropic.claude-3-sonnet-20240229-v1:0'
MODEL_ID_CLAUDE_V2 = 'anthropic.claude-v2'
AWS_PROFILE = 'default'

SOURCE_PDF = SOURCE_PDF_ITALY
MODEL_ID = MODEL_ID_CLAUDE

def no_pdf_index():
    # PDFLoader
    data_load=PyPDFLoader(SOURCE_PDF)
    
    data_split=RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " ", ""], chunk_size=100,chunk_overlap=10)
    
    data_embeddings=BedrockEmbeddings(
        credentials_profile_name= 'default',
        model_id='amazon.titan-embed-text-v1')
    
    data_index=VectorstoreIndexCreator(
        text_splitter=data_split,
        embedding=data_embeddings,
        vectorstore_cls=FAISS)
    
    # index

    db_index=data_index.from_loaders([data_load])
    print(db_index)
    return db_index

#connect to Bedrock Claude FM

def augmented_llm():
    llm=BedrockLLM(
        credentials_profile_name=AWS_PROFILE,
        model_id=MODEL_ID,
        model_kwargs={
        "max_tokens_to_sample":3000,
        "temperature": 0.5,
        "top_p": 0.7})
    return llm

# user prompt +  Vector DB  -->  LLM.
def no_pdf_rag_response(index,question):
    rag_llm=augmented_llm()
    no_rag_query=index.query(question=question,llm=rag_llm)
    return no_rag_query
