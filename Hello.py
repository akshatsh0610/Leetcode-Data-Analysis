import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome 👋")
st.markdown("""
    <style>
      section[data-testid="stSidebar"][aria-expanded="true"]{
        height: 100% !important;
      }
      section[data-testid="stSidebar"][aria-expanded="false"]{
        height: 100% !important;
      }
    </style>""", unsafe_allow_html=True)

# st.sidebar.image("D:\ML project\LeetCode_logo_rvs.png",use_column_width=True)
st.sidebar.markdown("")
st.markdown(
    """
    Here you can view complete analysis of leetcode problems.
    **👈 Select an option from the sidebar** to see various 
    problems!
"""
)