import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")
df=pd.read_csv('/app\pages\leetcode_problem.csv')
st.write("# Select the problem according to difficulty")
option = st.selectbox(
    'Select the tag of problem',
    ('All','Easy', 'Medium', 'Hard'))

if 'Easy' in option:
    result=df[df['difficulty']=='Easy']
    result=result.drop(['Unnamed: 0','solution_link','url','related_topics','similar_questions','companies'
                          ,'difficulty','frequency','description','is_premium','discuss_count'],axis=1)
    st.table(result)
elif 'Medium' in option:
    result=df[df['difficulty']=='Medium']
    result=result.drop(['Unnamed: 0','solution_link','url','related_topics','similar_questions','companies'
                          ,'difficulty','frequency','description','is_premium','discuss_count'],axis=1)
    st.table(result)
elif 'Hard' in option:
    result=df[df['difficulty']=='Hard']
    result=result.drop(['Unnamed: 0','solution_link','url','related_topics','similar_questions','companies'
                          ,'difficulty','frequency','description','is_premium','discuss_count'],axis=1)
    st.table(result)
elif 'All' in option:
    result=df
    result=result.drop(['Unnamed: 0','solution_link','url','related_topics','similar_questions','companies'
                        ,'frequency','description','is_premium','discuss_count'],axis=1)
    st.table(result)
