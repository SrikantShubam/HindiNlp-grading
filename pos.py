import nltk
import nltk
import pandas as pd
import sys
nltk.download('punkt')
# Download the Indian language corpus
nltk.download('indian')
print("Running POS---->")

# Load the tagged sentences in the Indian language corpus
tagged_sents = nltk.corpus.indian.tagged_sents()

# Train the TnT tagger on the tagged sentences in the corpus
tnt_tagger = nltk.tag.tnt.TnT()
tnt_tagger.train(tagged_sents)



print("POS---------")
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




tokens = nltk.word_tokenize(student_answer)
tags = tnt_tagger.tag(tokens)

tokens = nltk.word_tokenize(teacher_answer)
tags1 = tnt_tagger.tag(tokens)

# print(tags)

similar=[]


for i in tags:
  if i in tags1:
    similar.append(i)
print(len(similar))
pos=(len(similar)/len(tags))*100
print(" % of similar POS",pos)


df=pd.read_csv('result.csv')
print(df.head())
df["pos_score"]=pos
df.to_csv('result.csv')
print("POS data in csv check")
print(df.head())