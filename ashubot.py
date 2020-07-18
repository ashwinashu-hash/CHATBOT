#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install chatterbot==0.8.6')


# In[3]:


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# In[4]:


bot=ChatBot("akku")
bot.set_trainer(ChatterBotCorpusTrainer)


# In[5]:


bot.train("chatterbot.corpus.english")


# In[ ]:


while(True):
    message=input("You: ")
    if(message=="Bye" or message=="bye"):
        print("akku: nice talking to you, bye!!!!")
        break
    if(message!="Bye" or message!="bye"):
        print("akku: ",bot.get_response(message))


# In[ ]:




