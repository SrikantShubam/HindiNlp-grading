
import spacy_udpipe
spacy_udpipe.download("hi")
import pandas as pd
nlp = spacy_udpipe.load("hi")

# doc='''महर्षि विश्वामित्र और दोनों भाई ने चलते-चलते ऐसी जगह पर पहुँचे जहाँ दो नदियाँ आपस में मिलती थी'''
# doc1=''' जहाँ दो नदियाँ आपस में मिलती थी महर्षि विश्वामित्र और दोनों भाई ने चलते-चलते ऐसी जगह पर पहुँचे'''

import sys
# doc = sys.argv[2:]
print("UDPIPE---------")
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

print(student_answer)
print(teacher_answer)

# print(q)
# arg1 = args[0]
# arg2 = args[1]

# print(args[0][1])
# print(arg2)
# doc1= sys.argv[2:3] 


doc=nlp(student_answer)
doc1=nlp(teacher_answer)


list1=[]
list2=[]
for token in doc:
    # print(token.text, token.dep_, token.head.text)
    result = " ".join([token.text, token.dep_, token.head.text])
    list1.append(result)
for token in doc1:
    # print(token.text, token.dep_, token.head.text)
    result1 = " ".join([token.text, token.dep_, token.head.text])
    list2.append(result1)  

similarity=[]

for i in list1:
    for j in list2:
      if i==j:
        similarity.append(i)


a=len(list1)
b=len(similarity)


# Fining the percent of correct mapping
c=(b/a)*100
print(c,"% of dependency found")       
df=pd.read_csv('result.csv')
# print(df.head())
df["dependency_score"]=c
print(df.head())

df.to_csv('result.csv')