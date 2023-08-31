import streamlit as st

st.set_page_config(
  page_title="Calculators",
  page_icon=":bar_chart:",
  layout="wide"                 
)

st.title(":space_invader: Calculators")
st.markdown('###')
# st.write("---")
# CAtype = st.selectbox('Select Desired Calculator',
#             ('None','VA Calculator', 'HP Calculator'))
# if CAtype == 'VA Calculator':
tab1, tab2 = st.tabs('VA Calculator', 'HP Calculator')

with tab1:
  st.header('VA Calculator')
  num1 = st.number_input(label = 'Load')

  operation1 = st.radio('What is your Load Type?:',
                     ('FLA','MCA'))
  
  operation2 = st.radio('Select an Operation to Perform:',
                     ('120/1','208/1','208/3','277/1','480/1','480/3'))

  def VAcalculator():
    if operation1 == 'FLA' and operation2 == '120/1':
      ans = round(((num1 * 1.25) * 120), 2)
    elif operation1 == 'MCA' and operation2 == '120/1':
      ans = round((num1 * 120), 2)  
    elif operation1 == 'FLA' and operation2 == '208/1':
      ans = round(((num1 * 1.25) * 208), 2) 
    elif operation1 == 'MCA' and operation2 == '208/1':
      ans = round((num1 * 208), 2) 
    elif operation1 == 'FLA' and operation2 == '208/3':
      ans = round(((num1 * 1.25) * 360), 2)  
    elif operation1 == 'MCA' and operation2 == '208/3':
      ans = round((num1 * 360), 2)
    elif operation1 == 'FLA' and operation2 == '277/1':
      ans = round(((num1 * 1.25) * 277), 2) 
    elif operation1 == 'MCA' and operation2 == '277/1':
      ans = round((num1 * 277), 2)   
    elif operation1 == 'FLA' and operation2 == '480/1':
      ans = round(((num1 * 1.25) * 480), 2)                   
    elif operation1 == 'MCA' and operation2 == '480/1':
      ans = round((num1 * 480), 2)
    elif operation1 == 'FLA' and operation2 == '480/3':
      ans = round(((num1 * 1.25) * 831), 2) 
    elif operation1 == 'MCA' and operation2 == '480/3':
      ans = round((num1 * 831), 2) 
    else:
      st.warning("Division by 0 error. Please enter a non-zero number.")
      ans = "Not defined"
    st.success('VA = ' + str(ans))
 
  if st.button('Calculate'):
    VAcalculator()

# if CAtype == 'HP Calculator':
with tab2:
  st.header('HP Calculator')
  num1 = st.number_input(label = 'Load')

  operation = st.radio('Select an Operation to Perform:',
                     ('Mechanic/Hydraulic','Electric'))

  def HPcalculator():
    if operation == 'Mechanic/Hydraulic':
      ans = round((num1 * 745.699872), 2)
    elif operation == 'Electric':
      ans = round((num1 * 746), 2)
    else:
      st.warning("Division by 0 error. Please enter a non-zero number.")
      ans = "Not defined"
    st.success('Total Motor Load = ' + str(ans) + ' Watts')
 
  if st.button('Calculate'):
    HPcalculator()       

