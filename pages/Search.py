from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity
import openai
import pandas as pd
import ast

openai.api_key = "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"
df1 = pd.read_csv("habitat1.csv")
df2 = pd.read_csv("habitat2.csv")
df = pd.concat([df1, df2])
df['embeddings'] = df['embeddings'].apply(lambda x: ast.literal_eval(x))

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

