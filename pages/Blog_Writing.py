import openai
import streamlit as st

# Get API key
openai.api_key = st.secrets["openaiKey"]

# Create a function that uses GPT to write a blog post
def write_blog_post(prompt, topic):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please write a blog post on the topic: {topic}\n{prompt}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

# Create a Streamlit app
st.set_page_config(page_title="Blog Post Generator", page_icon=":guardsman:", layout="wide")
st.title("Blog Post Generator")

# Get topic information
topic = st.text_input("Enter the topic for your blog post:")
prompt = st.text_area("Enter any additional information or instructions:")

# Use GPT to write the blog post
if st.button("Write Blog Post"):
    blog_post = write_blog_post(prompt, topic)
    st.success("Blog post generated!")
    st.write("```")
    st.write(blog_post)
    st.write("```")
