import streamlit as st
import base64

# st.set_page_config(
#   page_title="MVC Tools - Homepage",
#   page_icon=":bar_chart:",
#   layout="wide"                 
# )

# # MAINPAGE

# st.header("MVC Tools of the Trade")
# st.markdown("##")


# hide_st_style="""
#             <style>
#             #MainMenu {visibility:hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """


def displayPDF(file):
    # Opening file from file path
    # pdf_path = path("2019_dbc.pdf")
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(file.read_bytes()).decode("utf-8")
    # Embedding PDF in HTML
    pdf_display = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}" width="800px" height="2100px" type="application/pdf"></iframe>
    """
                  
    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

displayPDF('2019_dbc.pdf')
st.markdown(hide_st_style, unsafe_allow_html=True)
