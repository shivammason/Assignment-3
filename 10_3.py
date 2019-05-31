#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string
fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()
    
counts = dict()
liste = tuple()

for line in fhand:
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans("", "", string.punctuation))
    line = line.translate(line.maketrans("", "", string.digits))
    line = line.replace("”","")
    line = line.replace("“","")
    line = line.replace("’","")
    line = line.replace(" ","")
    text = tuple(line)
    liste = liste + text
    
    for letters in text:
        if letters not in counts:
            counts[letters] = 1
        else:
            counts[letters] +=1
            
freq = dict()
frequence = 0.00
total = 0
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
lst.sort(reverse = True)

for key, val in lst[:]:
    total = total+key
    
for key, val in lst[:]:
    frequence = float(key/total)
    freq[key,val]=frequence
    
for key, val in freq:
    print(key, val, '{:.2%}'.format(freq[key,val]))


# In[ ]:




