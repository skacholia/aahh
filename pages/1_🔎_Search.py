from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity
import streamlit as st
import openai
import pandas as pd
import ast

openai.api_key = st.secrets["oai-key"]

@st.cache_data
def read_dfs():
    df1 = pd.read_csv("https://raw.githubusercontent.com/athensai/aahh/main/pages/habitat1.csv")
    df2 = pd.read_csv("https://raw.githubusercontent.com/athensai/aahh/main/pages/habitat2.csv")
    df = pd.concat([df1, df2])
    df['embeddings'] = df['embeddings'].apply(lambda x: ast.literal_eval(x))
    return df

df = read_dfs()

def get_embedding(text, model="text-embedding-ada-002"):
    return openai.Embedding.create(input = [text], model=model)['data'][0]['embedding']

def search_embed(df, description, n):
    description_embedding = get_embedding(
        description,
        model="text-embedding-ada-002"
    )
    df["similarity"] = df.embeddings.apply(lambda x: cosine_similarity(x, description_embedding))

    results = (
        df.sort_values("similarity", ascending=False)
        .head(n)
    )
    
    return results

query = st.text_input("Enter your query:")

if st.button(label = "Answer"):
    try:
        result = search_embed(df, query, 5)
        context = result['paragraphs'].tolist()
        context = ' '.join(context)
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Using the following context, answer the query. Be thorough, but don't include unnecessary detail. If you are not sure, say I don't know. Query: " + query + "\n Context:" + context,
        max_tokens = 1000)
        st.write(response.choices[0].text)
        st.write("\nLinks:")
        unique_links = result['link'].drop_duplicates().tolist()
        st.write('\n\n'.join(unique_links))
    except:
        st.write("An error occurred while processing your request.")




