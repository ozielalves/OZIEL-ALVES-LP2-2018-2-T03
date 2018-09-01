
# coding: utf-8

# In[216]:


import math as mt

# Question data:
total_cadeiras = 29
QE = 12684

# New
QP = 0
elec_votes = dict()
chairs_dist = dict()


# Reading csv
with open("eleicao.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        pline = list(enumerate(line.split(";")))
        print(pline)
        


# In[217]:


with open("eleicao.csv", encoding="utf-8") as f:
    f.readline()
    for line in f: 
        elections = line.split(";")
        parties_coal = elections[2]
        
        if parties_coal in elec_votes:
            elec_votes[parties_coal] += int(elections[3]) # explicit cast
        else:
            elec_votes[parties_coal] = int(elections[3])

print(elec_votes)


# In[218]:


for i in elec_votes.keys():
    #QP = mt.floor(elec_votes[i]/QE)
    print(elec_votes[i],"-", QE)

    QP = int(elec_votes[i]/QE)
    print(QP)
    if QP > 0:
        chairs_dist[i] = QP

#rs_dist)


# In[221]:


QP = {parties: int(votes / QE) for parties, votes in elec_votes.items()}
QP


# In[228]:


chairs_left = int(total_cadeiras - sum(filter(lambda elem:elem,(map(lambda M1:float(M1),M1.values())))))
chairs_left


# In[212]:


max(M1.items())


# In[210]:


while chairs_left > 0:
    for key in M1.items():
        if M1[key] > M1[key+1]:
            max
    
    
print(type(M1))


# In[235]:


while chairs_left >0:
    media = {paties: int(votos / QP+i+1) for parties, votos in M1.items()}
    i += 1


# In[230]:


media = dict()
while chairs_left > 0:
    for key in QP.items():
        print(chairs_dist[key]+1)
        current_media = elec_votes[key]/(chairs_dist[key]+1)
        print(current_media)
        media[key] = current_media
        
    media_winner = max(media, key=media.get)
    chairs_dist[media_winner] += 1


# In[60]:


import pandas as pd

data = pd.read_csv("eleicao.csv", sep=";")
data


# In[ ]:


coligacao_votos = dict()

partidos = data["Partido/Coligação"]
    if partidos in coligacao_votos


# In[61]:


colig = data["Partido/Coligação"].unique()
colig


# In[62]:


partidos = []
coligacoes = []
for i in colig:
    if len(i) > 4:
        coligacoes.append(i)
    else:
        partidos.append(i)
print(partidos)
print(coligacoes)


# In[63]:


print(data['Partido/Coligação'].unique())
sum(data['Votos'])


# In[85]:


#data.loc['Partido/Coligação']


# In[84]:


#votos_colig = []
#for i in data.iloc['Partido/Coligação']:
#    for j in data.loc['Votos']:
#        votos_colig.append(i,j)


# In[83]:


#partidos_votos = partidos[partidos.Votos]

