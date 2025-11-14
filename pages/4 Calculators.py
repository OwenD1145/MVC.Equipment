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
tab1, tab2, tab3 = st.tabs(["VA Calculator", "HP Calculator", "NEC Codes"])

with tab1:
  st.header('VA Calculator')
  num1 = st.number_input(label = 'Load', key = "<VA>")

  operation1 = st.radio('What is your Load Type?:',
                     ('FLA','MCA'))
  
  operation2 = st.radio('Select an Operation to Perform:',
                     ('120/1','208/1','208/3','277/1','480/1','480/3'))

  def VAcalculator():
    if operation1 == 'FLA' and operation2 == '120/1':
      ans = round(((num1 * 1.25) * 120), 2)
      ans1 = round((ans / 2), 2)
      st.success('VA = ' + str(ans) + '      W/ph = ' + str(ans1))
    elif operation1 == 'MCA' and operation2 == '120/1':
      ans = round((num1 * 120), 2)
      ans1 = round((ans / 2), 2)
      st.success('VA = ' + str(ans) + '      W/ph = ' + str(ans1))
    elif operation1 == 'FLA' and operation2 == '208/1':
      ans = round(((num1 * 1.25) * 208), 2)
      ans1 = round((ans / 2), 2)
      st.success('VA = ' + str(ans) + '      W/ph = ' + str(ans1))
    elif operation1 == 'MCA' and operation2 == '208/1':
      ans = round((num1 * 208), 2)
      ans1 = round((ans / 2), 2)
      st.success('VA = ' + str(ans) + '      W/ph = ' + str(ans1))
    elif operation1 == 'FLA' and operation2 == '208/3':
      ans = round(((num1 * 1.25) * 360), 2)
      ans3 = round((ans / 3), 2)
      st.success('VA = ' + str(ans) + '      W/ph = ' + str(ans3))  
    elif operation1 == 'MCA' and operation2 == '208/3':
      ans = round((num1 * 360), 2)
      ans3 = round((ans / 3), 2)
      st.success('VA = ' + str(ans) + '      W/ph = ' + str(ans3))  
    elif operation1 == 'FLA' and operation2 == '277/1':
      ans = round(((num1 * 1.25) * 277), 2)
      ans1 = round((ans / 2), 2)
      st.success('VA = ' + str(ans) + '      W/ph = ' + str(ans1))
    elif operation1 == 'MCA' and operation2 == '277/1':
      ans = round((num1 * 277), 2)   
      ans1 = round((ans / 2), 2)
      st.success('VA = ' + str(ans) + '      W/ph = ' + str(ans1))
    elif operation1 == 'FLA' and operation2 == '480/1':
      ans = round(((num1 * 1.25) * 480), 2)
      ans1 = round((ans / 2), 2)
      st.success('VA = ' + str(ans) + '      W/ph = ' + str(ans1))
    elif operation1 == 'MCA' and operation2 == '480/1':
      ans = round((num1 * 480), 2)
      ans1 = round((ans / 2), 2)
      st.success('VA = ' + str(ans) + '      W/ph = ' + str(ans1))
    elif operation1 == 'FLA' and operation2 == '480/3':
      ans = round(((num1 * 1.25) * 831), 2)
      ans3 = round((ans / 3), 2)
      st.success('VA = ' + str(ans) + '      W/ph = ' + str(ans3))  
    elif operation1 == 'MCA' and operation2 == '480/3':
      ans = round((num1 * 831), 2)
      ans3 = round((ans / 3), 2)
      st.success('VA = ' + str(ans) + '      W/ph = ' + str(ans3))  
    else:
      st.warning("Division by 0 error. Please enter a non-zero number.")
      ans = "Not defined"
    
    # if operation2 == '120/1' or '208/1' or '277/1' or '480/1':
    #   st.success('VA = ' + str(ans) + '  W/ph = ' + str(ans1))
    # if operation2 == '208/3' or '480/3':
    #   st.success('VA = ' + str(ans) + '  W/ph = ' + str(ans3))  
 
  if st.button('Calculate', key = "<VAC>"):
    VAcalculator()
   
# if CAtype == 'HP Calculator':
with tab2:
  st.header('HP Calculator')
  num2 = st.number_input(label = 'Load', key = "<HP>")

  operation = st.radio('Select an Operation to Perform:',
                     ('Mechanic/Hydraulic','Electric'))

  def HPcalculator():
    if operation == 'Mechanic/Hydraulic':
      ans = round((num2 * 745.699872), 2)
    elif operation == 'Electric':
      ans = round((num2 * 746), 2)
    else:
      st.warning("Division by 0 error. Please enter a non-zero number.")
      ans = "Not defined"
    st.success('Total Motor Load = ' + str(ans) + ' Watts')
 
  if st.button('Calculate', key = "<HPC>"):
    HPcalculator()       

with tabs[3]:
    st.header("Electrical Building Codes")
    
    # Search function
    search_term = st.text_input("🔍 Search codes:", placeholder="Enter keywords (e.g., 'outlet spacing', 'GFCI', 'wire size')")
    
    # Code database with descriptions
    codes = {
        "NEC 210.52(A) - Receptacle Outlet Spacing": "Receptacle outlets in dwelling units - at least one outlet within 6 feet of each wall space 2 feet or more in width",
        "NEC 210.8(A) - GFCI Protection Requirements": "GFCI protection required in bathrooms, garages, outdoors, crawl spaces, basements, kitchens, and laundry areas",
        "NEC 210.11(C)(1) - Small Appliance Circuits": "Small appliance circuits - at least two 20-amp circuits for kitchen and dining room receptacles",
        "NEC 220.14(J) - Dwelling Unit Load Calculations": "Dwelling unit loads - 3 VA per square foot for general lighting and receptacles",
        "NEC 310.15(B)(16) - Conductor Ampacity Tables": "Ampacity tables for conductors - copper and aluminum wire current ratings",
        "NEC 240.4(D) - Overcurrent Protection for Small Conductors": "Small conductor protection - 15A max for #14 AWG, 20A max for #12 AWG, 30A max for #10 AWG",
        "NEC 250.52(A) - Grounding Electrode System": "Grounding electrode system - water pipe, concrete-encased electrode, ground ring, rod/pipe electrodes",
        "NEC 314.16 - Electrical Box Fill Calculations": "Box fill calculations - volume allowances for conductors, devices, and fittings in electrical boxes",
        "NEC 334.80 - Nonmetallic Cable Ampacity": "NM cable ampacity - based on 90°C conductor temperature rating with 60°C termination derating",
        "NEC 422.16(B)(2) - Appliance Cord Length Limits": "Cord-and-plug connected appliances - flexible cord length shall not exceed 3 feet for built-in dishwashers",
        "NEC 410.16(A) - Luminaire Installation": "Luminaires shall be installed so that connections between luminaires and circuit conductors are accessible",
        "NEC 410.130(G) - LED Driver Accessibility": "LED drivers shall be accessible and located where they will not be subjected to temperatures exceeding manufacturer ratings",
        "NEC 411.3 - Low-Voltage Lighting Systems": "Low-voltage lighting systems operating at 30V or less shall comply with Class 2 circuit requirements",
        "NEC 430.6(A) - Motor Full-Load Current Tables": "Motor full-load currents used for conductor sizing shall be taken from NEC tables, not nameplate values",
        "NEC 430.32(A) - Motor Overload Protection": "Motors shall be protected against overload by separate overload devices rated at 115-125% of motor full-load current",
        "NEC 430.52 - Motor Short-Circuit Protection": "Motor branch circuits shall be protected by fuses or circuit breakers sized per NEC table 430.52",
        "NEC 445.13 - Generator Ampacity": "Generator conductors shall have ampacity not less than 115% of nameplate current rating",
        "NEC 450.3 - Transformer Overcurrent Protection": "Transformers shall be protected by overcurrent devices on primary and secondary sides per NEC requirements",
        "NEC 517.13 - Receptacles in Patient Care Areas": "Hospital patient care areas require hospital-grade receptacles and special grounding requirements",
        "NEC 680.22(A) - Pool Equipment Grounding": "All electrical equipment associated with pools shall be grounded and bonded per NEC requirements",
        "NEC 690.8 - Solar PV Circuit Requirements": "Photovoltaic systems shall comply with DC and AC disconnect requirements and rapid shutdown provisions",
        "NEC 700.12 - Emergency System Sources": "Emergency systems shall have automatic transfer capability and battery backup or generator power sources",
        "NEC 725.121 - Class 2 Circuit Power Limitations": "Class 2 circuits limited to 100VA and 30V for inherently limited power sources",
        "IECC C405.2 - Interior Lighting Power Allowance": "Interior lighting power density shall not exceed values specified in IECC tables (typically 0.6-1.0 W/sq ft)",
        "IECC C405.3 - Exterior Lighting Power Allowance": "Exterior lighting power shall not exceed specified allowances based on lighting zone classification",
        "IECC C405.4 - Lighting Controls Requirements": "Buildings shall have automatic lighting shutoff controls, occupancy sensors, and daylight controls where required",
        "IECC C406 - Additional Energy Efficiency": "Buildings must comply with one additional energy efficiency measure (enhanced envelope, HVAC, or lighting)",
        "ASHRAE 90.1 - Lighting Power Density": "Commercial buildings shall meet lighting power density limits ranging from 0.43-1.21 W/sq ft depending on space type",
        "IES RP-1-12 - Office Lighting Levels": "Recommended illuminance for office tasks: 300-500 lux (30-50 fc) for general office work",
        "UL 924 - Emergency Lighting Equipment": "Emergency lighting units shall be UL 924 listed and provide 90 minutes minimum battery backup"
    }
    
    # Filter codes based on search
    if search_term:
        filtered_codes = {k: v for k, v in codes.items() if search_term.lower() in v.lower() or search_term.lower() in k.lower()}
    else:
        filtered_codes = codes
    
    # Display codes
    if filtered_codes:
        for code_title, description in filtered_codes.items():
            with st.expander(f"📋 {code_title}"):
                st.write(description)
    else:
        st.info("No codes found matching your search term.")
    
    st.markdown("---")
    st.caption("⚠️ Always consult current NEC and local codes for official requirements")

