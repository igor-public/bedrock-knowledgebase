import os
from langchain.document_loaders import PyPDFLoader

SOURCE_PDF = "https://www.prh.fi/material/sites/prh/attachments/patentinliitteet/xdzzfkx7q/Patent_regulations_2023.pdf"

data_load=PyPDFLoader(SOURCE_PDF)
data_test=data_load.load_and_split()
print(len(data_test))
print(data_test[0])

# https://api.python.langchain.com/en/latest/indexes/langchain.indexes.vectorstore.VectorstoreIndexCreator.html
