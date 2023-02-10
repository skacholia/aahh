import openai
import streamlit as st

# Get API key
openai.api_key = st.secrets["openaiKey"]

# Create a function that uses GPT to summarize a document
def summarize_document(prompt, document):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please summarize the following document: {document} \n{prompt}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

# Create a Streamlit app
st.set_page_config(page_title="Document Summarizer", page_icon=":guardsman:", layout="wide")
st.title("Document Summarizer")

# Get document information
document = st.text_area("Enter the document you want to summarize:", max_chars=1000)
prompt = st.text_area("Enter any additional information or instructions:", max_chars=1000)

# Use GPT to summarize the legal document
if st.button("Summarize Document"):
    summary = summarize_document(prompt, document)
    st.success("Document summarized!")
    st.write("```")
    st.write(summary)
    st.write("```")
