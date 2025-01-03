import streamlit as st
import base64

st.set_page_config(
  page_title="MVC Tools - Homepage",
  page_icon=":bar_chart:",
  layout="wide"                 
)

# MAINPAGE

st.header("MVC Tools")
st.markdown("##")

col1, col2 = st.columns(2)
col1.write('Things I forget')
col2.write('Here they are')


hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

# def displayPDF(file):
#     # Opening file from file path
#     with open(file, "rb") as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')
#     # Embedding PDF in HTML
#     global pdf_display
#     pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
#     # Displaying File
#     st.markdown(pdf_display, unsafe_allow_html=True)
# displayPDF("2019_dbc.pdf")
st.markdown(hide_st_style, unsafe_allow_html=True)
# st.markdown(pdf_display, unsafe_allow_html=True)
