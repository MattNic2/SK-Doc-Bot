# Semantic Kernel Chatbot

Welcome to the **Semantic Kernel Chatbot** project! This bot leverages OpenAI's GPT-3.5 model to provide accurate and up-to-date information from the evolving Semantic Kernel documentation.

## Overview

Semantic Kernel is a dynamic framework, with its documentation constantly updated to reflect the latest features and improvements. Keeping track of these changes can be challenging, which is why we developed this chatbot. It reads the latest documentation, parses it, and allows users to query the bot for specific information, ensuring you always have access to the most current and relevant details.

## Features

- **Latest Documentation Access**: The bot is trained on the most recent Semantic Kernel documentation, ensuring accurate and timely responses.
- **Advanced Document Parsing**: Uses LangChain for splitting and embedding text, allowing for efficient information retrieval.
- **Interactive Q&A**: Engage in a conversational interface, where the bot remembers the context of your queries for a more coherent interaction.

## Getting Started

### Prerequisites

- **Python 3.8+**
- **OpenAI API Key**: Required for accessing the OpenAI models.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/semantic-kernel-chatbot.git
   cd semantic-kernel-chatbot
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Ensure you have the `OPENAI_API_KEY` set in your environment variables. This key is essential for accessing OpenAI's API.

### Running the Bot

To start the bot, simply run:

```bash
python main.py
```

## How it works

1. Document Loading: The bot uses PyPDFLoader to load the latest Semantic Kernel documentation.
2. Text Splitting: Documents are split into manageable chunks using RecursiveCharacterTextSplitter, optimized for semantic search.
3. Embedding and Search: OpenAIEmbeddings are used to convert text into embeddings, which are stored and searched through DocArrayInMemorySearch.
4. Conversational AI: The ConversationalRetrievalChain manages the conversation flow, leveraging OpenAI's ChatOpenAI model to generate responses.

## Customization

This project is a basic Retrieval-Augmented Generation (RAG) application. You can tweak the results by changing the search_type to MMR (Maximal Marginal Relevance) or adjusting the similarity_score_threshold to fine-tune the retrieval process.

### Document Splitting

Documents can be split in various ways for better chunking. In this project, we've used newlines, periods, and whitespace as separators. You can adjust these settings to optimize document splitting according to your needs.

### Adapting to New Documentation

This bot can be applied to any documentation. Simply replace the PDFs in the data folder with your own documents and update the paths in document_loader.py accordingly.

### Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please submit an issue or create a pull request.
