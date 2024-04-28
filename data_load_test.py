import os
from langchain.document_loaders import PyPDFLoader

SOURCE_PDF = "https://uibm.mise.gov.it/images/DLgs_10_febbraio_2005_n_30.pdf"

data_load=PyPDFLoader(SOURCE_PDF)
data_test=data_load.load_and_split()
print(len(data_test))
print(data_test[1])

# https://api.python.langchain.com/en/latest/indexes/langchain.indexes.vectorstore.VectorstoreIndexCreator.html
