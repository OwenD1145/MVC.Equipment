import streamlit as st
import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from scipy import signal
import requests
import json
import math

# Page config
st.set_page_config(page_title="EE Study Guide", layout="wide")

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'quiz_total' not in st.session_state:
    st.session_state.quiz_total = 0

# Use hardcoded Groq API key
api_key = "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"

# Main title
st.title("Electrical Study Guide")

# Tabs
tabs = st.tabs(["Electrical Equations", "LLM Tutor", "Reference Tables", "Building Codes"])

# Tab 1: Equations
with tabs[0]:

    



    with st.expander("Single Phase Volt Amp"):
        st.latex(r"VA = V \times \left( FLA \times 1.25 \right)")
        col1, col2 = st.columns(2)
        with col1:
            voltage_1ph = st.number_input("Voltage (V)", value=120.0, key="voltage_1ph")
        with col2:
            current_1ph = st.number_input("Current (A)", value=20.0, key="current_1ph")
        
        if st.button("Calculate Single Phase VA"):
            va_1ph = voltage_1ph * current_1ph
            st.success(f"VA = {va_1ph:.0f} VA")
            st.success(f"kVA = {va_1ph/1000:.2f} kVA")
    
    with st.expander("Three Phase Volt Amp"):
        st.latex(r"VA = \left( V \times \sqrt{3} \right) \times \left( FLA \times 1.25 \right)")
        col1, col2 = st.columns(2)
        with col1:
            voltage_3ph = st.number_input("Line Voltage (V)", value=480.0, key="voltage_3ph")
        with col2:
            current_3ph = st.number_input("Line Current (A)", value=50.0, key="current_3ph")
        
        if st.button("Calculate Three Phase VA"):
            va_3ph = (math.sqrt3 * voltage_3ph) * (current_3ph * 1.25)
            st.success(f"VA = {va_3ph:.0f} VA")
            st.success(f"kVA = {va_3ph/1000:.2f} kVA")
    
    with st.expander("Breaker Size Calculator"):
        st.latex(r"I = \frac{P}{V} \text{ (1φ)} \quad I = \frac{P}{\sqrt{3} \times V} \text{ (3φ)}")
        col1, col2, col3 = st.columns(3)
        with col1:
            load_watts = st.number_input("Load (Watts)", value=5000.0, key="load_watts")
        with col2:
            system_voltage = st.selectbox("System Voltage", ["120V", "208V", "277V", "480V"], key="system_voltage")
        with col3:
            phase_type = st.selectbox("Phase", ["Single Phase", "Three Phase"], key="phase_type")
        
        if st.button("Calculate Breaker Size"):
            voltage = float(system_voltage.replace("V", ""))
            
            if phase_type == "Single Phase":
                current = load_watts / voltage
            else:
                current = load_watts / (math.sqrt(3) * voltage)
            
            # NEC 125% rule for continuous loads
            breaker_current = current * 1.25
            
            # Standard US breaker sizes
            standard_sizes = [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 125, 150, 175, 200, 225, 250, 300, 350, 400, 450, 500, 600, 700, 800, 1000, 1200]
            selected_breaker = next((size for size in standard_sizes if size >= breaker_current), standard_sizes[-1])
            
            st.success(f"Load Current = {current:.1f} A")
            st.success(f"Min Breaker (125%) = {breaker_current:.1f} A")
            st.success(f"Standard Breaker = {selected_breaker} A")
    


# Tab 2: LLM Tutor
with tabs[1]:
    st.header("EE Tutor Chatbot")
    
    # Chat input with form for Enter key support
    with st.form(key="chat_form", clear_on_submit=True):
        col1, col2 = st.columns([4, 1])
        with col1:
            prompt = st.text_input("Ask me anything about Electrical Engineering!", key="chat_input", label_visibility="collapsed")
        with col2:
            send_button = st.form_submit_button("💬 Send", use_container_width=True)
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Process input
    if prompt and send_button:
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message immediately
        with st.chat_message("user"):
            st.markdown(prompt)
        
        try:
            # Groq API call
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            
            # Prepare messages with system prompt first
            messages = [
                {"role": "system", "content": "You are an expert Electrical Engineering tutor. Explain concepts clearly, solve problems step-by-step, provide examples, and focus on EE topics."}
            ]
            
            # Add conversation history (excluding system messages)
            for msg in st.session_state.messages:
                if msg["role"] != "system":
                    messages.append(msg)
            
            data = {
                "messages": messages,
                "model": "llama-3.1-8b-instant",
                "temperature": 0.7,
                "max_tokens": 1024,
                "stream": False
            }
            
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                assistant_response = result["choices"][0]["message"]["content"]
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
                
                # Display the new response immediately
                with st.chat_message("assistant"):
                    st.markdown(assistant_response)
            else:
                st.error(f"API Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []

# Tab 3: Reference Tables
with tabs[2]:
    st.header("Reference Tables & Tools")
    
    ref_type = st.selectbox("Reference Type", ["Master Feeder Tables", "Unit Converter"])
    
    if ref_type == "Master Feeder Tables":
        tab1, tab2 = st.tabs(["Master Feeder - AL", "Master Feeder - CU"])
        
        with tab1:
            st.subheader('Master Feeder - Aluminum')
            al_data = {
                'Ampacity': ['4000/W', '3000/W', '2500/W', '2000/W', '1600/W', '1200/W', '1000/W', '800/W', '750/W', '600/W', '500/W', '400/W', '350/W', '300/W', '250/W', '225/W', '200/W', '175/W', '150/W', '125/W', '100/W', '90/W', '80/W', '70/W', '60/W', '50/W', '40/W'],
                'Conductor': ['11[W-700kcmil, 750kcmilG, 4"C]', '8[W-700kcmil, 600kcmilG, 4"C]', '7[W-700kcmil, 600kcmilG, 4"C]', '6[W-600kcmil, 400kcmilG, 4"C]', 
                            '5[W-600kcmil, 350kcmilG, 4"C]', '4[W-500kcmil, 250kcmilG, 3-1/2"C]', '4[W-350kcmil, 4/0G, 3"C]', '3[W-400kcmil, 3/0G, 3"C]', 
                            '3[W-350kcmil, 3/0G, 3"C]', '2[W-500kcmil, 2/0G, 3-1/2"C]', '2[W-350kcmil, 1/0G, 3"C]', '2[W-250kcmil, #1G, 3"C]', 
                            '2[W-4/0, #1G, 2-1/2"C]', 'W-500kcmil, #2G, 3-1/2"C', 'W-350kcmil, #2G, 3"C', 'W-300kcmil, #2G, 3"C', 'W-250kcmil, #4G, 3"C', 'W- 4/0, #4G, 2-1/2"C', 'W- 3/0, #4G, 2"C',
                            'W- 2/0, #4G, 2"C', 'W-1/0, #6G, 2"C', 'W-1/0, #6G, 2"C', 'W#1, #6G, 1-1/2"C', 'W#2, #6G, 1-1/4"C', 'W#2, #8G, 1-1/4"C', 'W#4, #8G, 1-1/4"C', 'W#6, #8G, 1"C']
            }
            df_al = pd.DataFrame(al_data)
            st.dataframe(df_al, height=600)
        
        with tab2:
            st.subheader('Master Feeder - Copper')
            cu_data = {
                'Ampacity': ['3000/W', '2000/W', '1600/W', '1200/W', '1000/W', '800/W', '750/W', '600/W', '500/W', '400/W', '350/W', '300/W', '250/W', '225/W', '200/W', '175/W', '150/W', '125/W', '100/W', '90/W', '80/W', '70/W', '60/W', '50/W', '40/W', '30/W', '20/W'],
                'Conductor': ['8[W-500kcmil, 400kcmilG, 3-1/2"C], 750kcmilG, 4"C]', '6[W-400kcmil, 250kcmilG, 3"C]', '5[W-400kcmil, 4/0G, 3"C]', '4[W-350kcmil, 3/0G, 3"C]', 
                            '3[W-400kcmil, 2/0G, 3"C]', '3[W-300kcmil, 1/0G, 3"C]', '3[W-250kcmil, 1/0G, 3"C]', '2[W-350kcmil, #1G, 3"C]', 
                            '2[W-250kcmil, #2G, 3"C]', '2[W-3/0, #3G, 2"C]', '2[W-2/0, #3G, 2"C]', 'W-350kcmil, #4G, 3"C', 
                            'W-250kcmil, #4G, 3"C', 'W-4/0,#4G,2"C', 'W-3/0, #6G, 2"C', 'W-2/0, #6G, 2"C', 'W- 1/0, #6G, 2"C', 'W- 1/0, #6G, 2"C', 'W#1, #6G, 1-1/2"C',
                            'W#2, #8G, 1-1/4"C', 'W#3, #8G, 1-1/4"C', 'W#4, #8G, 1-1/4"C', 'W#4, #8G, 1-1/4"C', 'W#6, #10G, 1"C', 'W#8, #10G, 1"C', 'W#10, #10G, 3/4"C', 'W#12, #12G, 3/4"C']
            }
            df_cu = pd.DataFrame(cu_data)
            st.dataframe(df_cu, height=600)
    
    
    elif ref_type == "Unit Converter":
        st.subheader("Electrical Unit Converter")
        conv_type = st.selectbox("Conversion", ["Watts to HP", "kVA to Amps", "Frequency to Period"])
        
        if conv_type == "Watts to HP":
            watts = st.number_input("Power (Watts)", value=1000.0)
            hp = watts / 746
            st.success(f"{watts} W = {hp:.3f} HP")
        elif conv_type == "kVA to Amps":
            kva = st.number_input("Power (kVA)", value=10.0)
            voltage = st.number_input("Voltage (V)", value=480.0, key="conv_v")
            amps = (kva * 1000) / voltage
            st.success(f"{kva} kVA at {voltage} V = {amps:.2f} A")

# Tab 4: Electrical Building Codes
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

# Settings
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.success("✅ Groq API Connected")
with col2:
    if st.button("🔄 Reset Session"):
        st.session_state.clear()

# Footer
st.markdown("*Electrical Engineering Study Guide*")
