import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from bot.document_loader import load_documents
from bot.text_processing import split_documents

def create_chatbot():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    
    api_path = r"data/Semantic_Kernel_API_Documentation.pdf"
    intro_path = r"data/Semantic_Kernel_Introduction_Guide.pdf"

    api_pages, intro_pages = load_documents(api_path, intro_path)
    api_splits = split_documents(api_pages)
    intro_splits = split_documents(intro_pages)

    combined_documents = api_splits + intro_splits
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    db = DocArrayInMemorySearch.from_documents(combined_documents, embeddings)
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    qa = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0), 
        chain_type="stuff", 
        retriever=retriever, 
        memory=memory,
        output_key="answer",
    )

    return qa
