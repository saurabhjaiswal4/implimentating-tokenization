


import re 
import nltk
text = "This is a sample sentence for tokenization[1],[2].It demonstrates44 basic tokenization.I am, doing 287%$internship $in nullclass44."
def remove_between_square_brackets(text):
     return re.sub(r'[^\w\s]', '', text)


text = remove_between_square_brackets(text)
text=re.sub(r'\d+', '', text)
print(text)


# In[ ]:




