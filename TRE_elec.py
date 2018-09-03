
# coding: utf-8

# In[647]:


# Problem data:
total_cadeiras = 29
QE = 12684


# In[648]:


elec_votes = dict()
elections = []

# Filtering the coalitions
with open("eleicao.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        elections.append(line.split(";"))
        data = line.split(";")
        parties_coal = data[2]
        
        if parties_coal.find("-") != -1:
            parties_coal = parties_coal[(parties_coal.find("-") + 2):]

        # Assigning the number of votes to each party 
        if parties_coal in elec_votes:
            elec_votes[parties_coal] += int(data[3])
        else:
            elec_votes[parties_coal] = int(data[3]) 


# In[649]:


# Sorting candidates by the number of votes
elections = sorted(elections, key = lambda votes: int(votes[3]), reverse=True)        


# In[650]:


# Finding the Parties Coefficient
QP = {parties: (votes // QE) for parties, votes in elec_votes.items() if (votes // QE) > 0}


# In[651]:


# The number of chairs left after the first distribution
chairs_left = total_cadeiras - sum(filter(lambda elem:elem,(map(lambda QP:int(QP),QP.values()))))
print(">>> Remaining chairs number: ",chairs_left)


# In[652]:


# Distribution of remaining chairs
M = dict()
for i in range(chairs_left):
    #M = {party : elec_votes[party] / (qp + 1) for party, qp in QP.items()}
    for party,qp in QP.items():
        M[party] = (elec_votes[party]/(qp + 1))
    winner_party = max(M, key=M.get)
    QP[winner_party] += 1


# In[653]:


# Selecting Elected Politicians
for i, coalitions in enumerate(elections):
    if coalitions[2].find("-") != -1:
        party = coalitions[2][(coalitions[2].find("-") + 2):]
    else:
        party = coalitions[2]
    if party in QP and QP[party] > 0:
        QP[party] += -1
    else:
        elections[i] = 0

elections = [elected for elected in elections if elected != 0]


# In[654]:


# Generating output file with elected politicians
result = open("electeds.tsv", "w")
for i in range(0,total_cadeiras):
    result.write("\t".join(elections[i]))

