import openai
import streamlit as st

# Get API key
openai.api_key = st.secrets["openaiKey"]

# Create a function that uses GPT to write a grant application
def write_grant(prompt, organization, grant):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Write a grant application for {organization} for {grant} funding.\n{prompt}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

# Create a Streamlit app
st.set_page_config(page_title="Grant Application Generator", page_icon=":guardsman:", layout="wide")
st.title("Grant Application Generator")

# Get organization and grant information
organization = st.text_input("Enter the name of your organization:")
grant = st.text_input("Enter the name of the grant you are applying for:")
prompt = st.text_area("Enter any additional information or instructions:")

# Use GPT to write the grant application
if st.button("Write Grant"):
    grant_application = write_grant(prompt, organization, grant)
    st.success("Grant application generated!")
    st.write("```")
    st.write(grant_application)
    st.write("```")