import pandas as pd
import streamlit as st
from pathlib import Path
data=Path(__file__).parents[1] / 'pages/leetcode_problem.csv'
st.set_page_config(layout="wide")
df=pd.read_csv(data)
st.write("# Enter the name of Company to see the problems asked in their interviews")
title = st.text_input('Company name', 'Company Name')
if title=='Company Name':
    st.write('')
else:
    result=df[df['companies'].str.contains(title.capitalize(),na=False)]
    result=result.drop(['Unnamed: 0','solution_link','url','related_topics','similar_questions','companies'
                            ,'frequency','is_premium','discuss_count','similar_questions','asked_by_faang',
                            'rating','dislikes','likes','submissions','accepted','description'],axis=1)
    st.table(result)

