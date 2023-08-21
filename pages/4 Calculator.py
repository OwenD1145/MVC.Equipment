import streamlit as st

st.title("VA Calculator")
st.write("---")

num1 = st.number_input(label = 'Load')

operation = st.radio('Select an Operation to Perform:',
                     ('120/1','120/3','208/1','208/3','277/1','277/3','480/1','480/3'))

def VAcalculator():
  if operation == '120/1':
    ans = round((num1 * 120), 2)
  elif operation == '120/3':
    ans = round((num1 * 208), 2)
  elif operation == '208/1':
    ans = round((num1 * 208), 2) 
  elif operation == '208/3':
    ans = round((num1 * 360), 2)  
  elif operation == '277/1':
    ans = round((num1 * 277), 2) 
  elif operation == '277/3':
    ans = round((num1 * 480), 2)                     
  elif operation == '480/1':
    ans = round((num1 * 480), 2)                   
  elif operation == '480/3':
    ans = round((num1 * 831), 2) 
  else:
    st.warning("Division by 0 error. Please enter a non-zero number.")
    ans = "Not defined"
  st.success('Answer = ' + str(ans))
 

if st.button('Calculate'):
  VAcalculator()


