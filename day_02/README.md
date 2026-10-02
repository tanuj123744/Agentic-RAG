Q1 What is document ingestion ?
Answer: It is process of extracting raw data from uploaded/given file into our system.

Q2. Why can't we directly give a 500-page PDF to our retrieval system ?
Answer: Retrieving whole document can be inefficient and can be difficult to find specific relevant information about a query.
        So we break the entire text into small chunks which can then be converted into embeddings. 

Q3. What is difference between text extraction and chunking ?
Answer: Text Extraction is a simple process of extracting raw text from the file while chunking is the process of breaking the extracted 
        data into useful/meaningful chunks/parts.

Q4. Why do we store metadata with text ?
Answer: To give contextual information with the text data we use/store metadata, like while extracting text from pdf we can store page number
        or author or even file name so that while answering the query we can pass the refrence to the user.

Q5. Why might page number be useful metadata ?
Answer: It provides useful refrence that from where the answer is given. 

Q6. What does path.suffix return ?
Answer: path.suffix returns type of file(extension of a file).

Q7. Why do we use Path(file_path) ?
Answer: We use it to create a path object which then later can be used to extract useful metadata.

Q8. Suppose a PDF has 50 pages. After extraction, should we automatically assume we have 50 final RAG chunks?
Answer: No, there is a difference between extracted text and chunks.  Chunks are not list of strings rather they are very small parts of 
        words/strings which are created from the extracted text. 

Q9. Why can blindly removing all whitespace/newlines from a PDF be problematic ?
Answer: Because removing all the white spaces/newlines can alter/destroy headings, tables, code, lists, mathematical expressions etc. 

Q10.Complete the architecture: 
 Document
   ↓
__________
   ↓
Clean text + metadata
   ↓
__________
   ↓
Embeddings
   ↓
Vector Database
ANswer: (1) Extract text (2) Chunking 




        