
# coding: utf-8

# In[7]:


total_cadeiras = 29
QE = 12684
QP_ = 0

with open("eleicao.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        line = line.split(";")
        print(line)
        


# In[9]:


import pandas as pd

data = pd.read_csv("eleicao.csv", sep=";")
data


# In[22]:


colig = data["Partido/Coligação"].unique()
colig


# In[26]:


partidos = []
coligacoes = []
for i in colig:
    if len(i) > 4:
        coligacoes.append(i)
    else:
        partidos.append(i)
print(partidos)
print(coligacoes)


# In[37]:


print(data['Partido/Coligação'].unique())
sum(data['Votos'])


# In[31]:


for i,partidos in data['Votos']:
    if i==partidos[i]:
        


# In[ ]:


for i,row in data.loc[data['Partido/Coligação'].unique(),:].iterrows():
    


# In[41]:


colTypes = ('Partido/Coligação','Votos')
for i, row in colTypes.iterrows():
    if row['type']==partidos:       
        data[row['feature']]=data[row['feature']].astype(np.object) 
    elif row['type']=="continuous":    
        data[row['feature']]=data[row['feature']].astype(np.float) 
    print(data.dtypes)


# In[46]:


for i in data:
    print([data['Nome'],data['Votos'])

