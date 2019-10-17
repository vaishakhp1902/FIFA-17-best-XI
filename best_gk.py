

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
df=pd.read_csv("C:\\Users\\VAISHAKH\\Desktop\\fifa 17\\FullData.csv")
df.head(7)



del df['National_Kit']


plt.figure(figsize=(15,32))
sns.countplot(y=df.Nationality,palette="Set2")



plt.figure(figsize=(15,6))
sns.countplot(x="Age",data=df)  #no of players in each age


#weights
a = 0.5
b = 1
c = 2
d = 3

df['gk_Shot_Stopper'] = (b*df.Reactions + b*df.Composure + a*df.Speed + a*df.Strength + c*df.Jumping + b*df.GK_Positioning + c*df.GK_Diving + d*df.GK_Reflexes + b*df.GK_Handling)/(2*a + 4*b + 2*c + 1*d)
df['gk_Sweeper'] = (b*df.Reactions + b*df.Composure + a*df.Speed + a*df.Short_Pass + a*df.Long_Pass + c*df.Jumping + b*df.GK_Positioning + c*df.GK_Diving + d*df.GK_Reflexes + b*df.GK_Handling + d*df.GK_Kicking)/(2*a + 4*b + 2*c + 2*d)










plt.figure(figsize=(15,6))
#Generating sequential data and plot
sd1 = df.sort_values('gk_Shot_Stopper', ascending=False)[:5]
x1 = np.array(list(sd1['Name']))
y1 = np.array(list(sd1['gk_Shot_Stopper']))
sns.barplot(x1,y1,palette="colorblind")