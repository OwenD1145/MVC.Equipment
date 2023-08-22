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


def displayPDF():
    # Opening file from file path
    with open((2021 - Xcel-Energy-Standard-For-Electric-Installation-and-Use.pdf), "rb") as f:
        base64_pdf = base64.b64encode(f.read(2021 - Xcel-Energy-Standard-For-Electric-Installation-and-Use.pdf)).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
 
st.markdown(hide_st_style, unsafe_allow_html=True)
