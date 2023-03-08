import threading
import os
# import subprocess
# import sys
import pandas as pd
# def load():
#     os.system("transliterate.py")
    # 
# import udpipe  
doc2=["महर्षि विश्वामित्र और दोनों भाई ने चलते-चलते ऐसी जगह पर पहुँचे जहाँ दो नदियाँ आपस में मिलती थी","जहाँ दो नदियाँ आपस में मिलती थी महर्षि विश्वामित्र और दोनों भाई ने चलते-चलते ऐसी जगह पर पहुँचे"]
# doc="महर्षि विश्वामित्र और दोनों भाई ने चलते-चलते ऐसी जगह पर पहुँचे जहाँ दो नदियाँ आपस में मिलती थी"
# doc1="जहाँ दो नदियाँ आपस में मिलती थी महर्षि विश्वामित्र और दोनों भाई ने चलते-चलते ऐसी जगह पर पहुँचे"
# df=pd.read_csv(file)
def run_file1(arg1):
    a=""
    for i, name in enumerate(arg1):
        a+=" "+str(i)+" "+name
        
        
        # a=a+"split here"+name
    # print(a)   
    os.system("python pos.py {}".format(a))
    

def run_file2(arg1):
    # subprocess.call(['python', 'udpipe.py', arg1, arg2])
    a=""
    for i, name in enumerate(arg1):
        a+=" "+str(i)+" "+name
        
        
        # a=a+"split here"+name
    # print(a)   
    os.system("python udpipe.py {}".format(a))

        
def run_file3(arg1):
    # subprocess.call(['python', 'udpipe.py', arg1, arg2])
    a=""
    for i, name in enumerate(arg1):
        a+=" "+str(i)+" "+name
        
        
        # a=a+"split here"+name
    # print(a)   
    os.system("python semantic_similarity.py {}".format(a))        

# args = sys.argv[1:]
# arg1 = args[0]
# arg2 = args[1]
t1 = threading.Thread(target=run_file1,args=(doc2,))
t2 = threading.Thread(target=run_file2,args=(doc2,))
t3 = threading.Thread(target=run_file3,args=(doc2,))
t3.start()
t3.join()
t1.start()
t2.start()

t1.join()
t2.join()



weight_pos=0.4
weight_dependency=0.4
weight_cosine=0.2
data=pd.read_csv('result.csv')

cosine_similarity_value=data['semantic_score']
c=int(data['dependency_score'])
pos=int(data['pos_score'])
sim=int(cosine_similarity_value)*100
# sim
total=sim+c+pos
if (total>200 and total<250):
  print("We go ahead and give marks")
  print("marks=0.5")
if total>250:
  print("marks=1")
else:
  print("marks=0")