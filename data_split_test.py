import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

SOURCE_PDF = "https://uibm.mise.gov.it/images/DLgs_10_febbraio_2005_n_30.pdf"

data_load=PyPDFLoader(SOURCE_PDF)

data_split=RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " ", ""], chunk_size=100,chunk_overlap=10)
data_sample = 'The is a sample to be given to see the split working fine'
data_split_test = data_split.split_text(data_sample)
print(data_split_test)