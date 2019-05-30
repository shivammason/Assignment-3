#!/usr/bin/env python
# coding: utf-8

# In[2]:


count = 0
average = 0
sum = 0
a = []

while True:
  b = input("Enter a number: ")
  if (b == "done"):
    break
  value = int(b)
  sum = sum + value
  count = count + 1
  average = sum / count
  a.append(value)
print (average)
print (max(a))
print (min(a))


# In[ ]:




