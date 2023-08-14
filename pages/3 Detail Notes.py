import pandas as pd
import streamlit as st 

st.set_page_config(
  page_title="Equipment Dashboard",
  page_icon=":bar_chart:",
  layout="wide"                 
)

# MAINPAGE

st.header(":space_invader: MVC Detail Notes")
st.markdown("##")

if st.button('Read Me'):
    st.text('Please add your personal downloads folder to Excels trusted locations to enable Macros in the produced document:') 
    st.code('File -> Options -> Trust Center -> Trust Center Settings -> Trusted Locations -> Add New Location')
    st.text('The file path will be:')
    st.code('C:/Users/user_directory/Downloads')  

st.text('Loads must be seperated by a space between the value and the load type. Horsepower must be written out in fractional form. MOP/MOCP must be listed first. Table below for example formatting:')
ex = pd.DataFrame(
    {
        'Key': ['CP', '1', 'EF', '2', 'FCU', '1'],
        'Equipment': ['Circulation Pump', '', 'Exhaust Fan', '', 'Fan Coil Unit', ''],
        'Load': ['1-1/2 HP', '', '3.5 FLA', '','25 MOCP', '19 MCA' ],
        'Volts': ['120', '', '120', '', '208',''],
        '%%C': ['1', '', '1', '', '1', ''], 
        'Conductors' : ['', '', '', '', '', '',],
        'Conduit' : ['', '', '', '', '', '',],
        'Switch' : ['', '', '', '', '', '',],
        'Fuse' : ['', '', '', '', '', '',],
        }
)

st.dataframe(width = 1500,data = ex)


