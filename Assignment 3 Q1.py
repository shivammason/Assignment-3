#!/usr/bin/env python
# coding: utf-8

# In[1]:


count = 0
sum = 0
average  = 0
while True:
  try:
    x = input("Enter a number: ")
    if (x == "done"): 
     break
    value = float(x)
    sum = value + sum
    count = count + 1
    average = sum / count
  except:
    print("Invalid input.")
print (sum)
print (count)
print (average)


# In[ ]:




