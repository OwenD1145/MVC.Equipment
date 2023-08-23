import streamlit as st
import pandas as pd


st.set_page_config(
  page_title="Detail Notes",
  page_icon=":bar_chart:",
  layout="wide"                 
)

# MAINPAGE

st.header(":space_invader: MVC Detail Notes")
st.markdown("##")

option = st.selectbox(
    'What Detail Notes Are We Searching For?',
    ('EV-Charging', 'Mechanical Systems', 'One-Line'))

if option == 'EV-Charging':
  st.code('EVSE	ELECTRIC VEHICLE SUPPLY EQUIPMENT: PROVIDE CHARGEPOINT CT4000-PMGMT LEVEL 2 COMMERCIAL CHARGING STATION WITH LOAD MANAGEMENT OR APPROVED EQUAL. PROVIDE 50A, 208V, 1∅ CONNECTION WITH 2#6Cu,1#10G IN 1\" CONDUIT TO SPECIFIED CIRCUIT . WHERE TWO CONNECTIONS ARE ADJACENT PROVIDE DUAL CHARGER.')

  
	    
  
  
          
          
                


 
    

# if st.button('Read Me'):
#     st.text('Please add your personal downloads folder to Excels trusted locations to enable Macros in the produced document:') 
#     st.code('File -> Options -> Trust Center -> Trust Center Settings -> Trusted Locations -> Add New Location')
#     st.text('The file path will be:')
#     st.code('C:/Users/user_directory/Downloads')  

# st.text('Loads must be seperated by a space between the value and the load type. Horsepower must be written out in fractional form. MOP/MOCP must be listed first. Table below for example formatting:')
# ex = pd.DataFrame(
#     {
#         'Key': ['CP', '1', 'EF', '2', 'FCU', '1'],
#         'Equipment': ['Circulation Pump', '', 'Exhaust Fan', '', 'Fan Coil Unit', ''],
#         'Load': ['1-1/2 HP', '', '3.5 FLA', '','25 MOCP', '19 MCA' ],
#         'Volts': ['120', '', '120', '', '208',''],
#         '%%C': ['1', '', '1', '', '1', ''], 
#         'Conductors' : ['', '', '', '', '', '',],
#         'Conduit' : ['', '', '', '', '', '',],
#         'Switch' : ['', '', '', '', '', '',],
#         'Fuse' : ['', '', '', '', '', '',],
#         }
# )

# st.dataframe(width = 1500,data = ex)


hide_st_style="""
            <style>
            #MainMenu {visibility:hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
 
st.markdown(hide_st_style, unsafe_allow_html=True)

