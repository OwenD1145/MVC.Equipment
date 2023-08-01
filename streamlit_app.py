st.set_page_config(
  page_title="Equipment Dashboard",
  page_icon=":bar_chart:",
  layout="wide"                 
)

# MAINPAGE

st.header(":space_invader: MVC Equipment Schedule Automation")
st.markdown("##")


hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
 
st.markdown(hide_st_style, unsafe_allow_html=True)
