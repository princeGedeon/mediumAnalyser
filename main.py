import os
from dotenv import load_dotenv
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import Pinecone
from pinecone import Pinecone as P
load_dotenv()
pc=P(api_key=os.environ.get("PINECONE_API_KEY"))

loader=TextLoader('mediumblogs/blog1.txt')
document=loader.load()


text_spliter=CharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
#La taille du morceau, et en cas de cheveauchement
texts=text_spliter.split_documents(document)
# J'ai une liste avec les morceaux.
print(len(texts))

embeddings=OpenAIEmbeddings()
docsearch=Pinecone.from_documents(texts,embeddings,index_name="medium-blog-embeddings-index")

qa=RetrievalQA.from_chain_type(
    llm=OpenAI(),chain_type='stuff',retriever=docsearch.as_retriever()
)

query=input("Your query : ")
result=qa({"query":query})
print(result)