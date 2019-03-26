#!/usr/bin/env python
# coding: utf-8
# author: Timothy Briant S. Conejos
# date: March 26, 2019

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#show graph of month of January on LRT


#dataframe
df = pd.read_csv("datasets/lrt1_daily_and_monthly_passenger_traffic_per_station_2014_0.csv")


# In[2]:


df.head()


# In[63]:


LRTEntry = pd.DataFrame()
LRTEntry["station"] = df.copy()["station"].unique()
LRTEntry = LRTEntry.set_index("station")
months = df.copy()["month"].unique()

LRTExit = LRTEntry.copy()
#groupby movement
entry = df.groupby("movement").get_group("Entry")
exit = df.groupby("movement").get_group("Exit")

for name, group in entry.groupby("month"):
    LRTEntry = LRTEntry.join(group.set_index("station")[["count_traffic"]].rename(columns={"count_traffic":name}))
for name, group in exit.groupby("month"):
    LRTExit = LRTExit.join(group.set_index("station")[["count_traffic"]].rename(columns={"count_traffic":name}))
    
LRTEntry = LRTEntry[months]
LRTExit = LRTExit[months]


# In[123]:


LRTEntry.sum()
#plt.matshow(LRTEntry)

#other method
labels = [c for c in LRTEntry.columns]

fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(111)
ax.matshow(LRTEntry, cmap=plt.cm.bwr)
ax.set_xticklabels(labels)
ax.set_yticklabels(LRTEntry.index)
ax.set_xticks(np.arange(len(labels)))
ax.set_yticks(np.arange(len(LRTEntry.index)))


# In[ ]:





# In[124]:


LRTEntry.sum()
#plt.matshow(LRTEntry)

#other method
labels = [c for c in LRTExit.columns]

fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(111)
ax.matshow(LRTExit, cmap=plt.cm.bwr)
ax.set_xticklabels(labels)
ax.set_yticklabels(LRTExit.index)
ax.set_xticks(np.arange(len(labels)))
ax.set_yticks(np.arange(len(LRTExit.index)))

