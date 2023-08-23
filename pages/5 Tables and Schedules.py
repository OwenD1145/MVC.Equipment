import streamlit as st
import pandas as pd

st.set_page_config(
  page_title="Tables and Schedules",
  page_icon=":bar_chart:",
  layout="wide"                 
)

# MAINPAGE

st.header(":space_invader: Tables and Schedules")
st.markdown("##")
CAtype = st.selectbox('Select Desired Table/Schedule',
            ('None','Master Feeder - AL', 'Master Feeder - CU'))
if CAtype == 'Master Feeder - AL':
  st.text('Master Feeder - AL')
  ex = pd.DataFrame(
      {
          'Ampacity': ['4000/W', '3000/W', '2500/W', '2000/W', '1600/W', '1200/W', '1000/W', '800/W', '750/W', '600/W', '500/W', '400/W', '350/W', '300/W', '250/W', '225/W', '200/W', '175/W', '150/W', '125/W', '100/W', '90/W', '80/W', '70/W', '60/W', '50/W', '40/W'],
          'Conductor': ['11[W-700kcmil, 750kcmilG, 4"C]', '8[W-700kcmil, 600kcmilG, 4"C]', '7[W-700kcmil, 600kcmilG, 4"C]', '6[W-600kcmil, 400kcmilG, 4"C]', 
                        '5[W-600kcmil, 350kcmilG, 4"C]', '4[W-500kcmil, 250kcmilG, 3-1/2"C]', '4[W-350kcmil, 4/0G, 3"C]', '3[W-400kcmil, 3/0G, 3"C]', 
                        '3[W-350kcmil, 3/0G, 3"C]', '2[W-500kcmil, 2/0G, 3-1/2"C]', '2[W-350kcmil, 1/0G, 3"C]', '2[W-250kcmil, #1G, 3"C]', 
                        '2[W-4/0, #1G, 2-1/2"C]', 'W-500kcmil, #2G, 3-1/2"C', 'W-350kcmil, #2G, 3"C', 'W-300kcmil, #2G, 3"C', 'W-250kcmil, #4G, 3"C', 'W- 4/0, #4G, 2-1/2"C', 'W- 3/0, #4G, 2"C',
                        'W- 2/0, #4G, 2"C', 'W-1/0, #6G, 2"C', 'W-1/0, #6G, 2"C', 'W#1, #6G, 1-1/2"C', 'W#2, #6G, 1-1/4"C', 'W#2, #8G, 1-1/4"C', 'W#4, #8G, 1-1/4"C', 'W#6, #8G, 1"C'],
          }
  )
  
  st.dataframe(width = 2000, data = ex)

hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
 
st.markdown(hide_st_style, unsafe_allow_html=True)
