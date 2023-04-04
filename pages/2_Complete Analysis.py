import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
data=Path(__file__).parents[1] / 'pages/leetcode_problem.csv'
# pd.set_option('max_columns',200)

#  Importing dataset
df=pd.read_csv(data)
st.title('Leetcode All Problems Analysis')
df=df.drop(['Unnamed: 0'],axis=1)
new_df=df
new_df=new_df.drop(['description','solution_link','url','related_topics','similar_questions','companies'],axis=1)

def handle_accepted(value):
    if 'M' in value:
        value=value.replace('M','')
        if '.' in value:
            value=value.replace('.','')
        return int(float(value)*(1e6))
    elif 'K' in value:
        value=value.replace('K','')
        if '.' in value:
            value=value.replace('.','')
        return int(float(value)*1e3)
    else:
        return int(value)
new_df['accepted']=new_df['accepted'].apply(handle_accepted)

def handle_submissions(value):
    if 'M' in value:
        value=value.replace('M','')
        if '.' in value:
            value=value.replace('.','')
        return int(float(value)*(1e6))
    elif 'K' in value:
        value=value.replace('K','')
        if '.' in value:
            value=value.replace('.','')
        return int(float(value)*1e3)
    else:
        return int(value)
new_df['submissions']=new_df['submissions'].apply(handle_submissions)

## Showing analysis
st.header('Count of Problems on the basis of Difficulty Level')
fig1=plt.figure(figsize=(10, 4))
sns.countplot(x=new_df['difficulty'])
st.pyplot(fig1)

st.header('Count of Premium and Non premium problems')
fig2=plt.figure(figsize=(10,4))
sns.countplot(x=new_df['is_premium'])
st.pyplot(fig2)

st.header('Problems asked in FAANG')
fig3=plt.figure(figsize=(10,4))
sns.countplot(x=new_df['asked_by_faang'])
st.pyplot(fig3)

st.header('Problems distribution based on difficulty')
list1=new_df['difficulty'].value_counts()
list2=["Medium","Easy","Hard"]
# Creating color parameters
colors = ( "orange", "blue", "red")
 
# Wedge properties
wp = { 'linewidth' : 3, 'edgecolor' : "black" }

def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%".format(pct, absolute)
# Creating plot
fig4,ax= plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(list1,
                                  autopct = lambda pct: func(pct, list1),
                                  labels = list2,
                                  colors = colors,
                                  startangle = 90,
                                  wedgeprops = wp,
                                  textprops = dict(color ="black"))
 
 
plt.setp(autotexts, size = 20, weight ="bold")
# show plot
st.pyplot(fig4)

st.header('Average acceptance rate of easy, hard and medium problems')
result1 = new_df.groupby(['difficulty'])['acceptance_rate'].mean()
st.table(result1)

st.header('Average Frequency of easy, hard and medium problems')
result2 = new_df.groupby(['difficulty'])['frequency'].mean()
st.table(result2)

st.header('Average Rating of easy, hard and medium problems')
result3 = new_df.groupby(['difficulty'])['rating'].mean()
st.table(result3)

# fig5,ax1=px.histogram(df,x='difficulty',color='is_premium',nbins=10)
# st.pyplot(fig5)

st.header('Top 10 Hard problems with high acceptance rate')
result4=new_df[new_df['difficulty']=='Hard'][['id','title','acceptance_rate']].sort_values('acceptance_rate',ascending=False)[:10]
st.table(result4)

st.header('Top 50 medium and easy problems with low acceptance rate')
result5=new_df[new_df['difficulty']!='Hard'][['id','title','difficulty','acceptance_rate']].sort_values('acceptance_rate')[:50]
st.table(result5)

st.header('Correlation between different parameters of data')
corr=new_df.corr()
fig8=plt.figure(figsize=(16,8))
sns.heatmap(corr, annot=True, annot_kws={'weight':'bold'},linewidths=.5, cmap='RdPu')
st.pyplot(fig8)