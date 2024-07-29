from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(documents, chunk_size=1000, chunk_overlap=150):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap,
        is_separator_regex=True,
        separators=["\n\n", "\n", "(?<=\\.)", " ", ""]
    )
    return splitter.split_documents(documents)
