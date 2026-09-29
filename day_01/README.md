# DAY_01 RAG FOUNDATIONS

# Q1 What is LLM ? -- LLM stands for large language model, it gerenrates text based on our query. 


# Q2 What is RAG ? -- RAG stands for Retrieval Augumented Generation, it gathers relevant information from documents, web, 
#                     PDFs, APIs, github, databses etc. and passes it to the LLM with the context.


# Q3 What is Retrieval ? -- It is basically pocess of gathering useful information from various sources.


# Q4 What is Generation ? -- Generation means creating/synthesizsing answer to a query based on information.


# Q5 What is an Agent ? -- Agent can a do planning and execution based on a query to get the best possible answer. An agent can decide when/ #                          how to retrieve, what to retrieve, whether another retrieval/tool call is needed, etc.


# Q6 What is Agentic RAG ? -- As indicated by name, a RAG system gathers and supplies relevant information to the agent and 
#                             the agent then takes suitable decision on with that information to get the answer.
#                             Agentic RAG is a RAG system in which an agent can dynamically decide when and how to retrieve information, what #                             sources or retrieval steps to use, and whether additional actions are needed before generating the final answer.


# Q7 What I implemented ? -- I created a knowledge base first which contains some information and then i created a retriver which 
#                            retrives the information based on keyword match(lexical overlap) between the knowledge base and  user query.
#                            Then i built a context generator which generates context for an LLM from our retrieved rsult. Then i built 
#                            a prompt for the LLM which contains the context as well the user query.


# Q8 How my Retriever works ? -- My retrever is based on keyword match, it matches the keywords between document and user query and 
#                                retrieves top 2 documents which has most matching keywords.


# Q9 Limitations of my Retriever ? -- My retriever's limitation is that it based on keyword match. It does not understands contextual meaning 
#                                     of words. It can also give irrelevant answers because of this trait. This can be fixed later by using 
#                                     sematic retrieval or concept of embeddings.


# Q10 Why Embeddings are needed ? -- They are needed so that our model can understand contextual meaning of words insted of just giving 
#                                    answer based on keyword matching. Embeddings will reduce the irrelevant answers which our model is giving
#                                    now.


# Q11 What I learned ? -- I learned basic meaning of RAG, Agent, LLM, how these things are connected, how we retrieve information, different 
#                         types of retrieval, embeddings, How to seprate revriever, context generation, prompt generation etc. 