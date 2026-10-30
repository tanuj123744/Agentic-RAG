# Agentic RAG Assistant
## 30-Day Development Roadmap

**Project Goal:** Build, test, and deploy a functional Agentic RAG application within 30 days.

**Development Philosophy:**

Build a working foundation → Connect all components → Create a usable application → Introduce agentic capabilities → Evaluate → Deploy → Improve.

---

# 1. Project Vision

We are building an Agentic Retrieval-Augmented Generation (RAG) application that allows users to upload their documents, ask questions about their content, and receive contextually relevant answers supported by document sources.

The initial version will focus on reliability, usability, and a functional end-to-end workflow rather than implementing every advanced RAG technique.

The project will be developed incrementally. After deploying the initial version, we will improve its architecture, retrieval quality, agentic capabilities, and scalability.

## Core Objectives

1. Build a functional RAG pipeline.
2. Support document uploading and processing.
3. Generate embeddings and store them in a vector database.
4. Retrieve relevant information based on user queries.
5. Generate answers using an LLM and retrieved context.
6. Display source references for generated answers.
7. Introduce an initial agentic workflow.
8. Evaluate retrieval and answer quality.
9. Build a user-friendly web interface.
10. Deploy a working MVP within 30 days.

---

# 2. Development Principles

The following principles will guide the entire development process.

### 2.1 Build Before Over-Engineering

Our first priority is a functional application. We will not spend excessive time implementing advanced features before the basic system works.

### 2.2 Learn While Building

We will continue learning the theoretical concepts behind RAG and agentic systems, but theory will be directly connected to implementation.

### 2.3 Reuse Existing Work

Previously implemented components will be inspected and reused wherever appropriate. We will avoid unnecessary rewrites.

### 2.4 Use Proven Libraries

We will implement and understand the important application logic ourselves while using reliable libraries for infrastructure where appropriate.

### 2.5 Test Every Major Component

Each major feature must be tested before we build additional functionality on top of it.

### 2.6 Keep the Application Deployable

We will maintain a working application throughout development rather than connecting everything during the final week.

### 2.7 Improve Through Evaluation

We will use actual evaluation results and observed limitations to decide which improvements are necessary.

---

# 3. Initial MVP Features

The following features are targeted for the first release.

| Feature | Description | Priority |
|---|---|---|
| Document ingestion | Load PDF and TXT documents | Essential |
| Document cleaning | Clean and normalize extracted text | Essential |
| Text chunking | Split documents into meaningful chunks | Essential |
| Embeddings | Convert chunks into vector representations | Essential |
| Vector database | Store and search embeddings | Essential |
| Retrieval | Retrieve relevant document passages | Essential |
| LLM integration | Generate answers using retrieved context | Essential |
| Source citations | Display supporting document references | Essential |
| Web interface | Upload documents and ask questions | Essential |
| Error handling | Handle invalid files and application errors | Essential |
| Retrieval evaluation | Measure retrieval quality | Essential |
| Answer evaluation | Check answer relevance and grounding | Essential |
| Agentic workflow | Introduce controlled decision-making and retrieval refinement | Initial |
| Deployment | Make the application accessible online | Essential |

---

# 4. Proposed Technology Stack

The following technologies are initial preferences. Final decisions will be made during implementation based on compatibility, cost, and project requirements.

| Component | Proposed Technology |
|---|---|
| Programming language | Python |
| Frontend | Streamlit |
| Backend/application logic | Python |
| LLM | API-based or local LLM |
| Embedding model | Pretrained embedding model |
| Vector database | ChromaDB or another suitable vector store |
| Document processing | PyMuPDF and Python libraries |
| Agentic workflow | Initially controlled Python-based workflow; framework if justified |
| Version control | Git and GitHub |
| Deployment | Streamlit Community Cloud or another suitable hosting platform |
| Testing | pytest and custom evaluation scripts |

Technology choices should remain flexible until implementation requirements are clear.

---

# 5. Project Architecture

The initial application will contain the following logical layers.

## Layer 1: User Interface

Responsibilities:
- Document uploading.
- User query input.
- Display generated answers.
- Display source references.
- Basic conversation history.

## Layer 2: Document Ingestion

Responsibilities:
- Load supported documents.
- Extract text.
- Clean extracted content.
- Preserve document metadata.

## Layer 3: Retrieval Pipeline

Responsibilities:
- Chunk documents.
- Generate embeddings.
- Store vectors.
- Perform similarity search.
- Retrieve relevant passages.

## Layer 4: Answer Generation

Responsibilities:
- Construct prompts.
- Pass retrieved context to the LLM.
- Generate context-grounded answers.
- Handle insufficient evidence.
- Return source information.

## Layer 5: Agentic Workflow

Initial responsibilities:
- Decide when retrieval is required.
- Refine queries when appropriate.
- Perform additional retrieval when necessary.
- Determine whether sufficient evidence is available.
- Return an answer or explain the limitations.

## Layer 6: Evaluation and Deployment

Responsibilities:
- Evaluate retrieval quality.
- Test answer grounding.
- Handle application errors.
- Prepare deployment configuration.
- Deploy and test the application.

---

# 6. Thirty-Day Development Roadmap

## PHASE 1: BUILD THE RAG FOUNDATION
### Days 1–7

**Goal:** Build a functional end-to-end RAG pipeline.

### Day 1 — Repository Inspection and Project Planning
- Inspect the existing GitHub repository.
- Review previously implemented components.
- Identify reusable code and missing components.
- Finalize the initial architecture.
- Establish the development environment.

**Deliverable:** A clear implementation plan based on the existing repository.

### Day 2 — Document Ingestion and Processing
- Review document loading.
- Implement or improve PDF and TXT support.
- Improve text extraction.
- Handle empty and invalid documents.
- Preserve useful metadata.

**Deliverable:** A reliable document ingestion pipeline.

### Day 3 — Chunking and Metadata
- Review chunking strategies.
- Implement the selected chunking approach.
- Preserve document identifiers and metadata.
- Test chunk sizes and overlap.
- Inspect generated chunks.

**Deliverable:** A functional chunking module.

### Day 4 — Embedding Integration
- Understand embedding models and vector representations.
- Select a pretrained embedding model.
- Generate embeddings for document chunks.
- Test embedding dimensions and output.
- Organize embedding generation into reusable code.

**Deliverable:** Working embedding generation.

### Day 5 — Vector Database Integration
- Understand vector database fundamentals.
- Select and integrate a vector database.
- Store document chunks and embeddings.
- Preserve metadata.
- Test insertion and retrieval.

**Deliverable:** A working vector storage system.

### Day 6 — Retrieval Pipeline
- Connect embeddings with vector storage.
- Implement similarity search.
- Retrieve top-k relevant chunks.
- Return chunk text and metadata.
- Test retrieval using sample queries.

**Deliverable:** A reusable retrieval component.

### Day 7 — LLM Integration and Basic RAG
- Integrate an LLM.
- Construct a context-grounded prompt.
- Connect retrieval with answer generation.
- Handle insufficient context.
- Test questions against uploaded documents.

**Deliverable:** A basic end-to-end RAG pipeline.

---

## PHASE 2: BUILD THE APPLICATION
### Days 8–14

**Goal:** Convert the Python pipeline into a usable application.

### Day 8 — User Interface Foundation
- Set up Streamlit.
- Create the application entry point.
- Build the initial page layout.
- Add document upload functionality.

**Deliverable:** A basic working interface.

### Day 9 — Connect Document Ingestion
- Connect uploaded files to document processing.
- Process documents through the ingestion pipeline.
- Generate chunks and embeddings.
- Store processed documents.

**Deliverable:** Document uploading and processing through the interface.

### Day 10 — Connect Question Answering
- Add a question input area.
- Connect the interface to the RAG pipeline.
- Display generated answers.
- Handle invalid and empty queries.

**Deliverable:** Users can ask questions through the interface.

### Day 11 — Source Citations
- Return source metadata from retrieval.
- Connect retrieved passages with generated answers.
- Display source document names.
- Show supporting passages where appropriate.

**Deliverable:** Answers with document references.

### Day 12 — Conversation History
- Implement basic conversation history.
- Preserve relevant interaction state.
- Display previous questions and answers.
- Test multiple queries within a session.

**Deliverable:** Basic conversational interaction.

### Day 13 — Error Handling
- Handle unsupported file formats.
- Handle empty documents.
- Handle API failures.
- Handle missing configuration.
- Improve user-facing error messages.

**Deliverable:** More robust application behavior.

### Day 14 — Application Integration Testing
- Test the complete user workflow.
- Upload multiple documents.
- Ask different types of questions.
- Verify retrieved passages.
- Verify answer generation and citations.
- Fix major integration issues.

**Deliverable:** A usable local RAG application.

---

## PHASE 3: EVALUATION AND AGENTIC CAPABILITIES
### Days 15–21

**Goal:** Measure system quality and introduce the first agentic workflow.

### Day 15 — Evaluation Dataset
- Prepare representative test queries.
- Define expected relevant documents or chunks.
- Organize test cases.
- Establish a retrieval evaluation baseline.

**Deliverable:** A structured evaluation dataset.

### Day 16 — Retrieval Evaluation
- Implement Precision@K.
- Implement Recall@K.
- Implement Mean Reciprocal Rank (MRR).
- Run evaluation against the retrieval system.
- Record baseline results.

**Deliverable:** Retrieval evaluation report.

### Day 17 — Retrieval Improvement
- Analyze evaluation results.
- Identify retrieval weaknesses.
- Experiment with metadata filtering or search settings.
- Compare improved retrieval with the baseline.

**Deliverable:** A measured retrieval improvement or documented baseline limitations.

### Day 18 — Query Refinement
- Understand query rewriting.
- Identify situations where user queries need refinement.
- Implement a basic query refinement mechanism.
- Test original and refined queries.

**Deliverable:** Initial query refinement capability.

### Day 19 — Initial Agentic Workflow
- Introduce controlled decision-making.
- Determine when retrieval should be performed.
- Allow additional retrieval when appropriate.
- Define clear stopping conditions.
- Handle insufficient evidence.

**Deliverable:** A basic agentic RAG workflow.

### Day 20 — Answer Grounding and Quality Checks
- Check whether answers are supported by retrieved context.
- Identify unsupported claims.
- Improve prompts and answer handling.
- Test insufficient-context scenarios.

**Deliverable:** Initial answer-grounding checks.

### Day 21 — System Evaluation
- Compare the original RAG pipeline with the improved workflow.
- Review retrieval metrics.
- Test answer quality.
- Identify remaining limitations.
- Document results.

**Deliverable:** Initial system evaluation report.

---

## PHASE 4: DEPLOYMENT AND FINALIZATION
### Days 22–30

**Goal:** Deploy a functional MVP and prepare the repository for demonstration.

### Day 22 — Architecture Finalization
- Review the complete application architecture.
- Remove unnecessary duplication.
- Improve module organization.
- Verify component responsibilities.
- Finalize application integration.

**Deliverable:** A stable application structure.

### Day 23 — Configuration Management
- Organize environment variables.
- Secure API keys.
- Prepare configuration files.
- Verify local configuration.
- Check dependency management.

**Deliverable:** Deployment-ready configuration.

### Day 24 — Deployment Preparation
- Select the deployment platform.
- Prepare the requirements file.
- Configure the application entry point.
- Prepare deployment settings.
- Verify the application can run in a clean environment.

**Deliverable:** Deployment-ready application.

### Day 25 — Initial Deployment
- Deploy the application.
- Configure environment variables.
- Verify application startup.
- Test public accessibility.
- Fix deployment-related issues.

**Deliverable:** First deployed version.

### Day 26 — Production Workflow Testing
- Upload real documents.
- Test multiple queries.
- Verify retrieval and answer generation.
- Check source references.
- Test error handling.
- Identify deployment-specific problems.

**Deliverable:** Tested deployed application.

### Day 27 — Bug Fixes and Stability
- Resolve critical bugs.
- Improve error handling.
- Fix issues discovered during testing.
- Verify application stability.

**Deliverable:** More stable deployed MVP.

### Day 28 — Interface and Documentation
- Improve the user interface.
- Organize the README.
- Add setup instructions.
- Document features and limitations.
- Add architecture information.

**Deliverable:** Presentable application and documentation.

### Day 29 — Final Testing
- Perform end-to-end testing.
- Verify core features.
- Review evaluation results.
- Fix critical remaining issues.
- Check repository cleanliness.

**Deliverable:** Final MVP testing report.

### Day 30 — MVP Release
- Finalize the application.
- Update GitHub documentation.
- Add architecture diagrams where useful.
- Document the deployment.
- Prepare a project demonstration.
- Record future improvement opportunities.

**Deliverable:** A deployed Agentic RAG MVP.

---

# 7. Repository Organization Standards

We will maintain a clean separation between reusable application logic, data, experiments, and tests.

Proposed structure:

```text
Agentic-RAG/
│
├── main/
│   ├── ingestion/
│   ├── embeddings/
│   ├── retrieval/
│   ├── generation/
│   ├── agent/
│   └── utils/
│
├── data/
│   └── sample_documents/
│
├── experiments/
│
├── tests/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── PROJECT_ROADMAP.md
```

This is the target structure, not a requirement to create every folder immediately.

### Folder Responsibilities

- `main/`: Reusable application code.
- `main/ingestion/`: Document loading, cleaning, and chunking.
- `main/embeddings/`: Embedding generation.
- `main/retrieval/`: Vector storage and retrieval.
- `main/generation/`: Prompt construction and LLM response generation.
- `main/agent/`: Agentic decision-making and workflow logic.
- `main/utils/`: Shared utilities.
- `data/`: Sample documents and development data.
- `experiments/`: Experimental scripts and evaluation programs.
- `tests/`: Automated tests.
- `app.py`: Application entry point.

### Important Rules

1. Reusable code belongs in `main/`.
2. Sample and development data belongs in `data/`.
3. Experimental implementations belong in `experiments/`.
4. Automated tests belong in `tests/`.
5. Do not create duplicate implementations unnecessarily.
6. Do not hardcode API keys.
7. Do not commit `.env`, virtual environments, or unnecessary generated files.
8. Use meaningful filenames and function names.
9. Keep modules focused on specific responsibilities.
10. Commit meaningful changes regularly.

---

# 8. Definition of MVP Completion

The project will be considered successfully completed by Day 30 when the following conditions are met:

- [ ] The application can be accessed online.
- [ ] Users can upload supported PDF and TXT documents.
- [ ] Documents are extracted and processed correctly.
- [ ] Documents are divided into chunks.
- [ ] Embeddings are generated.
- [ ] Embeddings and metadata are stored in a vector database.
- [ ] User queries retrieve relevant document passages.
- [ ] An LLM generates answers using retrieved context.
- [ ] Answers display supporting document references.
- [ ] The application handles insufficient information appropriately.
- [ ] Basic conversation history works.
- [ ] An initial agentic workflow is implemented.
- [ ] Retrieval evaluation metrics are available.
- [ ] Basic answer-grounding checks are implemented.
- [ ] Major errors and failure cases have been tested.
- [ ] GitHub documentation is complete.
- [ ] Deployment instructions are documented.

---

# 9. Features Intentionally Postponed

The following features are outside the initial 30-day MVP unless they become necessary:

- Complex multi-agent architectures.
- Custom training of embedding models.
- Building a vector database from scratch.
- Advanced knowledge graph integration.
- Distributed infrastructure.
- Large-scale production optimization.
- Complex multi-user authentication and permissions.
- Advanced reranking before establishing a retrieval baseline.
- Extensive observability infrastructure.

These features can be considered in future development phases.

---

# 10. Working Method Between Developer and AI Assistant

The development process will follow these standards:

1. Inspect the existing repository before proposing changes.
2. Review relevant source files before modifying them.
3. Explain the concepts required for each implementation.
4. Provide exact file paths for code changes.
5. Explain what is being changed and why.
6. Avoid inventing files or assuming that a file already exists.
7. Provide commands to execute and test implementations.
8. Explain expected outputs and common errors.
9. Verify each major component before moving forward.
10. Reuse existing working code wherever possible.
11. Maintain GitHub commits throughout development.
12. Keep the 30-day deployment deadline as the primary development target.

The assistant should prioritize practical implementation without sacrificing the user's understanding of the underlying concepts.

---

# 11. Post-Day-30 Direction

Day 30 marks the completion of the initial MVP, not the end of the project.

Future development will be guided by actual application performance and user requirements.

Potential improvement areas include:

- Hybrid search.
- Advanced reranking.
- Better chunking strategies.
- Query expansion and decomposition.
- More capable agentic workflows.
- Tool integration.
- Conversation-aware retrieval.
- Better answer evaluation.
- Improved user experience.
- Scalability and performance.
- Multi-user support.

These improvements will be planned after evaluating the deployed MVP.

---

## Final Development Principle

**Our first objective is to build a working product, not a perfect product.**

We will prioritize functionality, reliability, and deployment within 30 days.

After that, we will continuously improve the system through testing, evaluation, experimentation, and better engineering decisions.