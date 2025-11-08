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
st.title("Electrical Engineering Study Guide")

# Tabs
tabs = st.tabs(["Equations", "Load Calculators", "LLM Tutor", "Reference Tables", "Quizzes"])

# Tab 1: Equations
with tabs[0]:
    st.header("Electrical Engineering Equations")
    
    eq_category = st.selectbox("Select Category", ["Power", "Transformers", "Motors", "VA & Power Factor", "Breaker Calculations"])
    
    if eq_category == "Power":
        with st.expander("DC Power"):
            st.latex(r"P = V \times I = I^2 \times R = \frac{V^2}{R}")
            col1, col2, col3 = st.columns(3)
            with col1:
                v_dc = st.number_input("Voltage (V)", value=12.0, key="v_dc")
            with col2:
                i_dc = st.number_input("Current (A)", value=2.0, key="i_dc")
            with col3:
                r_dc = st.number_input("Resistance (Ω)", value=6.0, key="r_dc")
            
            if st.button("Calculate DC Power"):
                p_vi = v_dc * i_dc
                p_i2r = i_dc**2 * r_dc
                p_v2r = v_dc**2 / r_dc if r_dc != 0 else 0
                st.success(f"P = V×I = {p_vi:.2f} W")
                st.success(f"P = I²×R = {p_i2r:.2f} W")
                st.success(f"P = V²/R = {p_v2r:.2f} W")
        
        with st.expander("AC Power (Single Phase)"):
            st.latex(r"P = V \times I \times \cos(\phi)")
            st.latex(r"Q = V \times I \times \sin(\phi)")
            st.latex(r"S = V \times I = \sqrt{P^2 + Q^2}")
            col1, col2, col3 = st.columns(3)
            with col1:
                v_ac = st.number_input("RMS Voltage (V)", value=120.0, key="v_ac")
            with col2:
                i_ac = st.number_input("RMS Current (A)", value=10.0, key="i_ac")
            with col3:
                pf = st.number_input("Power Factor", value=0.8, min_value=0.0, max_value=1.0, key="pf")
            
            if st.button("Calculate AC Power"):
                phi = math.acos(pf)
                p_real = v_ac * i_ac * pf
                q_reactive = v_ac * i_ac * math.sin(phi)
                s_apparent = v_ac * i_ac
                st.success(f"Real Power (P) = {p_real:.2f} W")
                st.success(f"Reactive Power (Q) = {q_reactive:.2f} VAR")
                st.success(f"Apparent Power (S) = {s_apparent:.2f} VA")
        
        with st.expander("Three Phase Power"):
            st.latex(r"P_{3\phi} = \sqrt{3} \times V_L \times I_L \times \cos(\phi)")
            st.latex(r"P_{3\phi} = 3 \times V_{ph} \times I_{ph} \times \cos(\phi)")
            col1, col2, col3 = st.columns(3)
            with col1:
                v_line = st.number_input("Line Voltage (V)", value=480.0, key="v_line")
            with col2:
                i_line = st.number_input("Line Current (A)", value=20.0, key="i_line")
            with col3:
                pf_3ph = st.number_input("Power Factor", value=0.85, min_value=0.0, max_value=1.0, key="pf_3ph")
            
            if st.button("Calculate 3-Phase Power"):
                p_3ph = math.sqrt(3) * v_line * i_line * pf_3ph
                s_3ph = math.sqrt(3) * v_line * i_line
                q_3ph = s_3ph * math.sin(math.acos(pf_3ph))
                st.success(f"3-Phase Real Power = {p_3ph:.2f} W ({p_3ph/1000:.2f} kW)")
                st.success(f"3-Phase Apparent Power = {s_3ph:.2f} VA ({s_3ph/1000:.2f} kVA)")
                st.success(f"3-Phase Reactive Power = {q_3ph:.2f} VAR")
    
    elif eq_category == "Transformers":
        with st.expander("Transformer Turns Ratio"):
            st.latex(r"\frac{N_p}{N_s} = \frac{V_p}{V_s} = \frac{I_s}{I_p}")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                np = st.number_input("Primary Turns", value=1000, key="np")
            with col2:
                ns = st.number_input("Secondary Turns", value=100, key="ns")
            with col3:
                vp = st.number_input("Primary Voltage (V)", value=480.0, key="vp")
            with col4:
                ip = st.number_input("Primary Current (A)", value=2.0, key="ip")
            
            if st.button("Calculate Transformer"):
                turns_ratio = np / ns if ns != 0 else 0
                vs = vp / turns_ratio if turns_ratio != 0 else 0
                is_calc = ip * turns_ratio
                st.success(f"Turns Ratio = {turns_ratio:.2f}:1")
                st.success(f"Secondary Voltage = {vs:.2f} V")
                st.success(f"Secondary Current = {is_calc:.2f} A")
        
        with st.expander("Transformer Efficiency"):
            st.latex(r"\eta = \frac{P_{out}}{P_{in}} \times 100\%")
            st.latex(r"P_{losses} = P_{copper} + P_{iron}")
            col1, col2, col3 = st.columns(3)
            with col1:
                p_out = st.number_input("Output Power (W)", value=9500.0, key="p_out")
            with col2:
                p_copper = st.number_input("Copper Losses (W)", value=200.0, key="p_copper")
            with col3:
                p_iron = st.number_input("Iron Losses (W)", value=150.0, key="p_iron")
            
            if st.button("Calculate Efficiency"):
                p_losses = p_copper + p_iron
                p_in = p_out + p_losses
                efficiency = (p_out / p_in) * 100 if p_in != 0 else 0
                st.success(f"Total Losses = {p_losses:.2f} W")
                st.success(f"Input Power = {p_in:.2f} W")
                st.success(f"Efficiency = {efficiency:.2f}%")
        
        with st.expander("Transformer Regulation"):
            st.latex(r"Regulation = \frac{V_{NL} - V_{FL}}{V_{FL}} \times 100\%")
            col1, col2 = st.columns(2)
            with col1:
                v_nl = st.number_input("No-Load Voltage (V)", value=240.0, key="v_nl")
            with col2:
                v_fl = st.number_input("Full-Load Voltage (V)", value=230.0, key="v_fl")
            
            if st.button("Calculate Regulation"):
                regulation = ((v_nl - v_fl) / v_fl) * 100 if v_fl != 0 else 0
                st.success(f"Voltage Regulation = {regulation:.2f}%")
    
    elif eq_category == "Motors":
        with st.expander("Motor Power & Torque"):
            st.latex(r"P = T \times \omega = T \times 2\pi \times \frac{n}{60}")
            st.latex(r"T = \frac{P \times 60}{2\pi \times n}")
            col1, col2 = st.columns(2)
            with col1:
                power_hp = st.number_input("Power (HP)", value=10.0, key="power_hp")
            with col2:
                speed_rpm = st.number_input("Speed (RPM)", value=1750.0, key="speed_rpm")
            
            if st.button("Calculate Motor Torque"):
                power_watts = power_hp * 746  # Convert HP to Watts
                omega = (2 * math.pi * speed_rpm) / 60  # rad/s
                torque = power_watts / omega if omega != 0 else 0
                torque_lb_ft = torque * 0.737562  # Convert N⋅m to lb⋅ft
                st.success(f"Power = {power_watts:.0f} W")
                st.success(f"Torque = {torque:.2f} N⋅m ({torque_lb_ft:.2f} lb⋅ft)")
        
        with st.expander("Motor Efficiency & Current"):
            st.latex(r"I = \frac{P_{out}}{\sqrt{3} \times V_L \times \eta \times \cos(\phi)}")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                motor_hp = st.number_input("Motor HP", value=5.0, key="motor_hp")
            with col2:
                motor_v = st.number_input("Line Voltage (V)", value=460.0, key="motor_v")
            with col3:
                motor_eff = st.number_input("Efficiency", value=0.9, min_value=0.0, max_value=1.0, key="motor_eff")
            with col4:
                motor_pf = st.number_input("Power Factor", value=0.85, min_value=0.0, max_value=1.0, key="motor_pf")
            
            if st.button("Calculate Motor Current"):
                p_out_watts = motor_hp * 746
                motor_current = p_out_watts / (math.sqrt(3) * motor_v * motor_eff * motor_pf) if (motor_v * motor_eff * motor_pf) != 0 else 0
                st.success(f"Output Power = {p_out_watts:.0f} W")
                st.success(f"Line Current = {motor_current:.2f} A")
        
        with st.expander("Synchronous Speed"):
            st.latex(r"n_s = \frac{120 \times f}{P}")
            col1, col2 = st.columns(2)
            with col1:
                frequency = st.number_input("Frequency (Hz)", value=60.0, key="frequency")
            with col2:
                poles = st.number_input("Number of Poles", value=4, key="poles")
            
            if st.button("Calculate Sync Speed"):
                sync_speed = (120 * frequency) / poles if poles != 0 else 0
                st.success(f"Synchronous Speed = {sync_speed:.0f} RPM")
    
    elif eq_category == "VA & Power Factor":
        with st.expander("Power Triangle"):
            st.latex(r"S^2 = P^2 + Q^2")
            st.latex(r"PF = \cos(\phi) = \frac{P}{S}")
            col1, col2 = st.columns(2)
            with col1:
                p_kw = st.number_input("Real Power (kW)", value=100.0, key="p_kw")
            with col2:
                pf_given = st.number_input("Power Factor", value=0.8, min_value=0.0, max_value=1.0, key="pf_given")
            
            if st.button("Calculate Power Triangle"):
                s_kva = p_kw / pf_given if pf_given != 0 else 0
                phi_rad = math.acos(pf_given)
                q_kvar = p_kw * math.tan(phi_rad)
                st.success(f"Apparent Power (S) = {s_kva:.2f} kVA")
                st.success(f"Reactive Power (Q) = {q_kvar:.2f} kVAR")
                st.success(f"Phase Angle = {math.degrees(phi_rad):.2f}°")
        
        with st.expander("Power Factor Correction"):
            st.latex(r"Q_c = P \times (\tan(\phi_1) - \tan(\phi_2))")
            col1, col2, col3 = st.columns(3)
            with col1:
                p_load = st.number_input("Load Power (kW)", value=50.0, key="p_load")
            with col2:
                pf_existing = st.number_input("Existing PF", value=0.7, min_value=0.0, max_value=1.0, key="pf_existing")
            with col3:
                pf_desired = st.number_input("Desired PF", value=0.95, min_value=0.0, max_value=1.0, key="pf_desired")
            
            if st.button("Calculate Capacitor Size"):
                phi1 = math.acos(pf_existing)
                phi2 = math.acos(pf_desired)
                qc = p_load * (math.tan(phi1) - math.tan(phi2))
                st.success(f"Required Capacitor = {qc:.2f} kVAR")
                st.success(f"Original kVA = {p_load/pf_existing:.2f}")
                st.success(f"Corrected kVA = {p_load/pf_desired:.2f}")
    
    elif eq_category == "Breaker Calculations":
        with st.expander("Circuit Breaker Sizing (NEC)"):
            st.latex(r"I_{breaker} \geq 1.25 \times I_{continuous}")
            col1, col2 = st.columns(2)
            with col1:
                load_current = st.number_input("Load Current (A)", value=20.0, key="load_current")
            with col2:
                load_type = st.selectbox("Load Type", ["Continuous (3+ hrs)", "Non-Continuous"], key="load_type")
            
            if st.button("Size Circuit Breaker"):
                if load_type == "Continuous (3+ hrs)":
                    min_breaker = load_current * 1.25
                else:
                    min_breaker = load_current
                
                # Standard breaker sizes
                standard_sizes = [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 125, 150, 175, 200, 225, 250, 300, 350, 400, 450, 500, 600, 700, 800, 1000, 1200]
                selected_breaker = next((size for size in standard_sizes if size >= min_breaker), standard_sizes[-1])
                
                st.success(f"Minimum Breaker Rating = {min_breaker:.1f} A")
                st.success(f"Standard Breaker Size = {selected_breaker} A")
        
        with st.expander("Short Circuit Current"):
            st.latex(r"I_{sc} = \frac{V}{Z_{total}}")
            col1, col2, col3 = st.columns(3)
            with col1:
                system_voltage = st.number_input("System Voltage (V)", value=480.0, key="system_voltage")
            with col2:
                source_impedance = st.number_input("Source Impedance (Ω)", value=0.1, key="source_impedance")
            with col3:
                cable_impedance = st.number_input("Cable Impedance (Ω)", value=0.05, key="cable_impedance")
            
            if st.button("Calculate Short Circuit"):
                total_impedance = source_impedance + cable_impedance
                isc = system_voltage / total_impedance if total_impedance != 0 else 0
                isc_3ph = isc * math.sqrt(3)  # 3-phase fault current
                st.success(f"Single Phase Fault = {isc:.0f} A")
                st.success(f"Three Phase Fault = {isc_3ph:.0f} A")
                st.success(f"Required AIC Rating ≥ {isc_3ph:.0f} A")
        
        with st.expander("Arc Flash Energy"):
            st.latex(r"E = 4.184 \times C_f \times E_n \times \left(\frac{t}{0.2}\right) \times \left(\frac{610^x}{D^x}\right)")
            col1, col2, col3 = st.columns(3)
            with col1:
                fault_current_af = st.number_input("Fault Current (kA)", value=10.0, key="fault_current_af")
            with col2:
                clearing_time = st.number_input("Clearing Time (s)", value=0.1, key="clearing_time")
            with col3:
                working_distance = st.number_input("Working Distance (in)", value=18.0, key="working_distance")
            
            if st.button("Calculate Arc Flash"):
                # Simplified IEEE 1584 calculation for 480V system
                cf = 1.0  # Configuration factor
                en = 4.184 * cf * fault_current_af * clearing_time * (610**1.081) / (working_distance**1.081)
                
                # PPE Categories
                if en < 1.2:
                    ppe_cat = "0 (Untreated cotton)"
                elif en < 4:
                    ppe_cat = "1 (4 cal/cm²)"
                elif en < 8:
                    ppe_cat = "2 (8 cal/cm²)"
                elif en < 25:
                    ppe_cat = "3 (25 cal/cm²)"
                else:
                    ppe_cat = "4 (40+ cal/cm²)"
                
                st.success(f"Arc Flash Energy = {en:.2f} cal/cm²")
                st.success(f"PPE Category = {ppe_cat}")
                if en > 40:
                    st.warning("⚠️ Dangerous level - Consider remote operation")

# Tab 2: Load Calculators
with tabs[1]:
    st.header("Load Calculators")
    
    calc_type = st.selectbox("Calculator Type", ["Volt-Amp Calculator", "Voltage Drop", "Power Factor Correction", "Transformer Sizing"])
    
    if calc_type == "Volt-Amp Calculator":
        st.subheader("Volt-Amp (VA) Calculator")
        
        calc_mode = st.radio("Calculation Mode", ["Single Phase", "Three Phase"])
        
        if calc_mode == "Single Phase":
            col1, col2, col3 = st.columns(3)
            with col1:
                voltage_1ph = st.number_input("Voltage (V)", value=120.0, key="v_1ph")
            with col2:
                current_1ph = st.number_input("Current (A)", value=10.0, key="i_1ph")
            with col3:
                pf_1ph = st.number_input("Power Factor", value=1.0, min_value=0.0, max_value=1.0, key="pf_1ph")
            
            if st.button("Calculate Single Phase VA"):
                va_1ph = voltage_1ph * current_1ph
                watts_1ph = va_1ph * pf_1ph
                vars_1ph = va_1ph * math.sin(math.acos(pf_1ph)) if pf_1ph < 1.0 else 0
                
                st.success(f"Apparent Power (VA) = {va_1ph:.2f} VA")
                st.success(f"Real Power (W) = {watts_1ph:.2f} W")
                st.success(f"Reactive Power (VAR) = {vars_1ph:.2f} VAR")
        
        else:  # Three Phase
            col1, col2, col3 = st.columns(3)
            with col1:
                voltage_3ph = st.number_input("Line Voltage (V)", value=480.0, key="v_3ph")
            with col2:
                current_3ph = st.number_input("Line Current (A)", value=20.0, key="i_3ph")
            with col3:
                pf_3ph = st.number_input("Power Factor", value=0.85, min_value=0.0, max_value=1.0, key="pf_3ph_va")
            
            if st.button("Calculate Three Phase VA"):
                va_3ph = math.sqrt(3) * voltage_3ph * current_3ph
                watts_3ph = va_3ph * pf_3ph
                vars_3ph = va_3ph * math.sin(math.acos(pf_3ph)) if pf_3ph < 1.0 else 0
                
                st.success(f"Apparent Power (VA) = {va_3ph:.2f} VA ({va_3ph/1000:.2f} kVA)")
                st.success(f"Real Power (W) = {watts_3ph:.2f} W ({watts_3ph/1000:.2f} kW)")
                st.success(f"Reactive Power (VAR) = {vars_3ph:.2f} VAR ({vars_3ph/1000:.2f} kVAR)")
    
    elif calc_type == "Voltage Drop":
        st.subheader("Voltage Drop Calculator")
        length = st.number_input("Wire Length (ft)", value=100)
        current = st.number_input("Current (A)", value=20)
        voltage = st.number_input("System Voltage (V)", value=120)
        wire_type = st.selectbox("Wire Material", ["Copper", "Aluminum"])
        
        if st.button("Calculate Voltage Drop"):
            # Resistance per 1000ft for 12 AWG
            r_per_1000 = 1.93 if wire_type == "Copper" else 3.18
            vd = (2 * length * current * r_per_1000) / 1000
            vd_percent = (vd / voltage) * 100
            
            st.success(f"Voltage Drop: {vd:.2f} V ({vd_percent:.1f}%)")
            if vd_percent > 3:
                st.warning("⚠️ Voltage drop exceeds 3% NEC recommendation")

# Tab 3: LLM Tutor
with tabs[2]:
    st.header("EE Tutor Chatbot")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input with form for Enter key support
    with st.form(key="chat_form", clear_on_submit=True):
        col1, col2 = st.columns([4, 1])
        with col1:
            prompt = st.text_input("Ask me anything about Electrical Engineering!", key="chat_input", label_visibility="collapsed")
        with col2:
            send_button = st.form_submit_button("💬 Send", use_container_width=True)
    
    # Process input
    if prompt and send_button:
        st.session_state.messages.append({"role": "user", "content": prompt})
        
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
                st.rerun()
            else:
                st.error(f"API Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Tab 4: Reference Tables
with tabs[3]:
    st.header("Reference Tables & Tools")
    
    ref_type = st.selectbox("Reference Type", ["AWG Wire Table", "Resistor Color Code", "Unit Converter"])
    
    if ref_type == "AWG Wire Table":
        awg_data = {
            'AWG': [14, 12, 10, 8, 6, 4, 2, 1, 0],
            'Diameter (mils)': [64.1, 80.8, 101.9, 128.5, 162.0, 204.3, 257.6, 289.3, 324.9],
            'Resistance (Ω/1000ft)': [2.525, 1.588, 0.999, 0.628, 0.395, 0.249, 0.156, 0.124, 0.098],
            'Ampacity (A)': [15, 20, 30, 40, 55, 70, 95, 110, 125]
        }
        df_awg = pd.DataFrame(awg_data)
        st.dataframe(df_awg)
    
    elif ref_type == "Resistor Color Code":
        st.subheader("Resistor Color Code Decoder")
        colors = ['Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Gray', 'White']
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            band1 = st.selectbox("1st Band", colors, index=1)
        with col2:
            band2 = st.selectbox("2nd Band", colors, index=0)
        with col3:
            band3 = st.selectbox("3rd Band", colors, index=2)
        with col4:
            tolerance = st.selectbox("Tolerance", ['Brown (±1%)', 'Red (±2%)', 'Gold (±5%)', 'Silver (±10%)'])
        
        if st.button("Decode Resistor"):
            values = {color: i for i, color in enumerate(colors)}
            digit1 = values[band1]
            digit2 = values[band2]
            multiplier = 10 ** values[band3]
            resistance = (digit1 * 10 + digit2) * multiplier
            st.success(f"Resistance: {resistance:,} Ω ({resistance/1000:.1f} kΩ)")
    
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

# Tab 5: Quizzes
with tabs[4]:
    st.header("Quizzes & Practice")
    
    quiz_questions = [
        {
            "question": "What is the unit of electrical resistance?",
            "options": ["Ampere", "Volt", "Ohm", "Watt"],
            "correct": 2,
            "explanation": "The ohm (Ω) is the SI unit of electrical resistance."
        },
        {
            "question": "In a series circuit, what remains constant?",
            "options": ["Voltage", "Current", "Resistance", "Power"],
            "correct": 1,
            "explanation": "In a series circuit, current remains constant throughout all components."
        },
        {
            "question": "What does AC stand for?",
            "options": ["Automatic Current", "Alternating Current", "Active Current", "Applied Current"],
            "correct": 1,
            "explanation": "AC stands for Alternating Current, which periodically reverses direction."
        }
    ]
    
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    
    if st.session_state.current_question < len(quiz_questions):
        q = quiz_questions[st.session_state.current_question]
        st.subheader(f"Question {st.session_state.current_question + 1}")
        st.write(q["question"])
        
        answer = st.radio("Select your answer:", q["options"], key=f"q_{st.session_state.current_question}")
        
        if st.button("Submit Answer"):
            if q["options"].index(answer) == q["correct"]:
                st.success("Correct! " + q["explanation"])
                st.session_state.quiz_score += 1
            else:
                st.error("Incorrect. " + q["explanation"])
            
            st.session_state.quiz_total += 1
            st.session_state.current_question += 1
            st.rerun()
    else:
        st.subheader("Quiz Complete!")
        score_percent = (st.session_state.quiz_score / st.session_state.quiz_total) * 100
        st.success(f"Final Score: {st.session_state.quiz_score}/{st.session_state.quiz_total} ({score_percent:.1f}%)")
        
        if st.button("Restart Quiz"):
            st.session_state.current_question = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_total = 0
            st.rerun()

# Settings
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.success("✅ Groq API Connected")
with col2:
    if st.button("🔄 Reset Session"):
        st.session_state.clear()
        st.rerun()

# Footer
st.markdown("*Electrical Engineering Study Guide*")
