# Build RAG chatbot with Langchain

## 1. reason


## 2. Phases of building RAG application

### 2.1 Content Ingestion
Before users can query Q&A chatbot, you need to store relevant content into a vector store. During content ingestion, text content is splitted into small chunks. Each chunk is then transformed into an **embedding** which is a numerical vector representation of text.

### 2.2 Retrieval and Generation
When users query with Q&A chatbot, a **retriever** converts the query into a vector representation using the same embedding model employed during the content ingestion stage. The **retriever** queries the vector store by performing a similarity search between the question vector and the stored text chunk vectors. The vector store returns the relevant document chunks by vector distance.<br>

Once the relevant content chunks are retrieved, the chatbot sends the LLM a prompt that includes the initial question and a context incorporating the retrieved document chunks. The LLM then generates the answer and returns it to the chatbot which then delivers it to the user.