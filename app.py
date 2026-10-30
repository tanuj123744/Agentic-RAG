import streamlit as st


# Page configuration

st.set_page_config(
    page_title="Agentic RAG Assistant",
    page_icon="📚",
    layout="wide"
)


# Main heading

st.title("Agentic RAG Assistant")

st.write(
    "Upload your documents and ask questions "
    "about their content."
)


# Sidebar

with st.sidebar:

    st.header("Document Upload")

    uploaded_files = st.file_uploader(
        "Upload PDF or TXT documents",

        type=["pdf", "txt"],

        accept_multiple_files=True
    )

    if uploaded_files:

        st.success(
            f"{len(uploaded_files)} document(s) selected."
        )

        for file in uploaded_files:

            st.write(file.name)


# Main question area

st.header("Ask Your Question")

query = st.text_input(
    "Enter your question"
)


if st.button("Ask"):

    if not query.strip():

        st.warning("Please enter a question.")

    else:

        st.info(
            "Question received. RAG integration "
            "will be connected in the next development step."
        )