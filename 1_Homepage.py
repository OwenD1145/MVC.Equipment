import streamlit as st

st.set_page_config(
  page_title="MVC Tools - Homepage",
  page_icon=":bar_chart:",
  layout="wide"                 
)

# MAINPAGE

st.header("MVC Tools of the Trade")
st.markdown("##")


hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
 
st.markdown(hide_st_style, unsafe_allow_html=True)
