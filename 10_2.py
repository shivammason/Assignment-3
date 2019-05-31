#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string
fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print("File can't open:", fname)
    exit()
    
new = list()
counts = dict()
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    new.append(words[5])
    
for i in range(0,len(new)):
    time = new[i]
    atpos = time.find(':')
    hour = time[:atpos]
            
    counts[hour] = counts.get(hour,0)+1
    
lst = list()
for key, val in list(counts.items()):
    lst.append((key,val))
lst.sort()
for key, val in lst:
    print(key, val)


# In[ ]:




