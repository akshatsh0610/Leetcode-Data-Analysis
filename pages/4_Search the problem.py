import pandas as pd
import streamlit as st
from pathlib import Path
data=Path(__file__).parents[1] / 'pages/leetcode_problem.csv'

df=pd.read_csv(data)
st.write("# Enter Problem ID")
title = st.text_input('Please enter problem id', 'Problem ID')
if title=='Problem ID' or title=="":
    st.write('')
else:
    if float(title) in df['id']:
        st.subheader("ID : "+title)
        res=str(df.loc[df['id']==float(title),'title'].iloc[0])
        st.subheader("Title -: "+res)
        st.subheader("Description -: ")
        res1=str(df.loc[df['id']==float(title),'description'].iloc[0])
        st.markdown(res1)
        st.subheader("Company tags -: ")
        res3=str(df.loc[df['id']==float(title),'companies'].iloc[0])
        st.markdown(res3)
        st.subheader("Related Topics -: ")
        res4=str(df.loc[df['id']==float(title),'related_topics'].iloc[0])
        st.markdown(res4)
        st.subheader("Similar Questions -: ")
        res5=str(df.loc[df['id']==float(title),'similar_questions'].iloc[0])
        split_string = res5.split("], [") # split into individual strings
        result = "" # initialize empty result string

        for s in split_string:
            problem_name = s.split(", ")[0][0:] # extract problem name and remove opening square bracket
            result += problem_name + " , " # add problem name to result string

        result = result[1:-3] # remove trailing comma and space
        st.markdown(result)
    else:
        st.subheader("Problem not found")
        
