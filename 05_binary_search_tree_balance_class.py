
# coding: utf-8

# In[1]:


from math import log2, ceil

def GenerateBBSTArray(a, BST_array = [], slot = 0, index = 0):
    if len(BST_array) == 0:
        BST_array = [None] * (2**(ceil(log2((len(a)+1)/2))+1)-1)
        a = sorted (a)
           
    index = int((len(a)/2))
    
    if index < len(a) and a[index] not in BST_array:
        
        BST_array[slot] = a[index]
        
        GenerateBBSTArray(a[:index], BST_array, slot * 2 + 1, index )

        GenerateBBSTArray(a[index+1:], BST_array, slot * 2 + 2, index )
    
    return BST_array

