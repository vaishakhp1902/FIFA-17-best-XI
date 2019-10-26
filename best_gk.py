

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



#choosing defenders

df['df_center_backs'] = (d*df.Reactions + c*df.Interceptions + d*df.Sliding_Tackle + d*df.Standing_Tackle + b*df.Vision + b*df.Composure + b*df.Crossing + a*df.Short_Pass + c*df.Long_Pass +c*df.Acceleration + b*df.Speed + d*df.Stamina + d*df.Jumping + d*df.Heading + b*df.Long_Shots + d*df.Marking + c*df.Aggression)/(6*b + 3*c + 7*d)
df['df_wb_Wing_Backs'] = (b*df.Ball_Control + a*df.Dribbling + a*df.Marking + d*df.Sliding_Tackle + d*df.Standing_Tackle + a*df.Attacking_Position + c*df.Vision + c*df.Crossing + b*df.Short_Pass + c*df.Long_Pass + d*df.Acceleration + d*df.Speed + c*df.Stamina + a*df.Finishing)/(4*a + 2*b +4*c)

#plot let center back
plt.figure(figsize=(15,6))
#Generating sequential data and plot
sd=df[(df['Club_Position']=='LCB')].sort_values('df_center_backs',ascending=False)[:5]
x2=np.array(list(sd['Name']))
y2=np.array(list(sd['df_center_backs']))
sns.barplot(x2,y2,palette=sns.color_palette("Blues_d"))
plt.ylabel("LCB Score")


#plot Right center back
plt.figure(figsize=(15,6))
#Generating sequential data and plot
sd=df[(df['Club_Position']=='RCB')].sort_values('df_center_backs',ascending=False)[:5]
x2=np.array(list(sd['Name']))
y2=np.array(list(sd['df_center_backs']))
sns.barplot(x2,y2,palette=sns.color_palette("Blues_d"))
plt.ylabel("RCB Score")





#plot lwb
plt.figure(figsize=(15,6))
sd=df[(df['Club_Position'] =='LWB') | (df['Club_Position'] =='LB') ].sort_values('df_wb_Wing_Backs',ascending=False)[:5]
x4=np.array(list(sd['Name']))
y4=np.array(list(sd['df_wb_Wing_Backs']))
sns.barplot(x4,y4,palette=sns.color_palette("Blues_d"))
plt.ylabel("Left Back Score")




#plot lwb
plt.figure(figsize=(15,6))
sd=df[(df['Club_Position'] =='RWB') | (df['Club_Position'] =='RB') ].sort_values('df_wb_Wing_Backs',ascending=False)[:5]
x5=np.array(list(sd['Name']))
y5=np.array(list(sd['df_wb_Wing_Backs']))
sns.barplot(x5,y5,palette=sns.color_palette("Blues_d"))
plt.ylabel("Right Back Score")
