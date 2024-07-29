from langchain_community.document_loaders import PyPDFLoader

def load_documents(api_path, intro_path):
    api_loader = PyPDFLoader(api_path)
    intro_loader = PyPDFLoader(intro_path)
    api_pages = api_loader.load()
    intro_pages = intro_loader.load()
    return api_pages, intro_pages
