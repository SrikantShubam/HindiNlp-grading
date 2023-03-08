import sys
# sys.path.append('./env/Lib/site-packages/sentence_transformers')
import pandas as pd
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('hiiamsid/sentence_similarity_hindi')

# import sys
# doc = sys.argv[1:2]
# doc1= sys.argv[2:3] 

# print(doc)
# print(doc2)
print("Running Semantic similarity---------")
args = sys.argv[1:]
# print(args)
# q=[]
# ans=[]
idx=args.index('1')
# q=args[1:38]
# print(idx)
teacher_answer = args[:idx]
student_answer = args[idx:]
teacher_answer = teacher_answer[1:]
student_answer = student_answer[1:]

student_answer = ' '.join(map(str, student_answer))
teacher_answer = ' '.join(map(str, teacher_answer))

sentences=[student_answer,teacher_answer]

embeddings = model.encode(sentences)
print(embeddings)
import numpy as np


def cosine_similarity(A, B):
    dot_product = np.dot(A, B)
    norm_a = np.linalg.norm(A)
    norm_b = np.linalg.norm(B)
    cosine_similarity = dot_product / (norm_a * norm_b)
    return cosine_similarity
A = embeddings[0]
B = embeddings[1]
cosine_similarity_value = cosine_similarity(A, B)
print(cosine_similarity_value)


data = {"semantic_score": cosine_similarity_value}
df=pd.DataFrame([data])
print("semantic score csv check--")
print(df.head())
df.to_csv('result.csv')