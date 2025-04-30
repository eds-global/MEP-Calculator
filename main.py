import streamlit as st
import subprocess
import os
import pandas as pd
from streamlit_card import card
from PIL import Image as PILImage
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tempfile
from src import ps_e 

# Set the page configuration with additional options layout='wide',
st.set_page_config(
    page_title="MEP Calculator",
    page_icon="♻️",
    layout='wide',  # Only 'centered' or 'wide' are valid options
    menu_items={                          
        'Get Help': 'https://www.example.com/help',
        'Report a bug': 'https://www.example.com/bug',
        'About': '# This is an **eQuest Utilities** application!'
    }
)

button_style = """
    <style>
        .stButton>button {
            box-shadow: 1px 1px 1px rgba(0, 0, 0, 0.8);
        }
    </style>
"""

# Render the button with the defined style
st.markdown(button_style, unsafe_allow_html=True)

# Define CSS style with text-shadow effect for the heading
heading_style = """
    <style>
    .heading-with-shadow {
        text-align: left;
        color: red;
        text-shadow: 0px 8px 4px rgba(255, 255, 255, 0.4);
        background-color: white;
    }
</style>
"""

# Render the heading with the defined style
st.markdown(heading_style, unsafe_allow_html=True)

# Define button carousel items
carousel_items = ["About EDS", "About eQuest", "INP Parser", "Purging INP", "SIM Parser", "SIM to PDF", "Baseline Automation", "EXE Files", "Queries", "Visual"]

def main(): 
    # Add custom CSS to set the background color and hide Streamlit branding elements
    card_button_style = """
        <style>
        .card-button {
            width: 100%;
            padding: 20px;
            background-color: white;
            border: none;
            border-radius: 10px;
            box-shadow: 0 2px 2px rgba(0,0,0,0.2);
            transition: box-shadow 0.3s ease;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
        }
        .card-button:hover {
            box-shadow: 0 8px 16px rgba(0,0,0,0.3);
        }
        </style>
    """
    
    st.markdown(
        """
        <style>
        body {
            background-color: #bfe1ff;  /* Set your desired background color here */
            animation: changeColor 5s infinite;
        }
        .css-18e3th9 {
            padding-top: 0rem;  /* Adjust the padding at the top */
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .viewerBadge_container__1QSob {visibility: hidden;}
        .stActionButton {margin: 5px;} /* Optional: Adjust button spacing */
        header .stApp [title="View source on GitHub"] {
            display: none;
        }
        .stApp header, .stApp footer {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Initialize session state for script_choice if it does not exist
    if 'script_choice' not in st.session_state:
        st.session_state.script_choice = "about"  # Set default to "about"
        
    logo_image_path = "images/energy.jpeg"
    _, col2, col3 = st.columns([1, 1, 0.5])
    # with col1:
    #     st.image(logo_image_path, width=80)
    with col2:
        st.markdown("<h1 class='heading-with-shadow'>MEP Calculator</h1>", unsafe_allow_html=True)
    with col3:
        st.image("images/EDSlogo.jpg", width=120)

    st.markdown("""
        <style>
        .stButton button {
            height: 30px;
            width: 265px;
        }
        </style>
    """, unsafe_allow_html=True)

    col2, col3, col4, col5, col6, col7, col8 = st.columns(7) 
    with st.sidebar:
        st.markdown("### 🔧 Select Calculator")
        if st.button("About EDS"):
            st.session_state.script_choice = "eds"
        if st.button("MEP Calculator"):
            st.session_state.script_choice = "about"
        if st.button("Baseline Energy End Use"):
            st.session_state.script_choice = "baselineenduse"
        if st.button("Proposed Energy End Use"):
            st.session_state.script_choice = "proposedenduse"
        if st.button("Baseline Annual Energy Cost"):
            st.session_state.script_choice = "baselinecost"
        if st.button("Prf. Rating Erg. Consumption & Cost"):
            st.session_state.script_choice = "baselineperformance"
        if st.button("Virtual Rate (Avg. ecpa)"):
            st.session_state.script_choice = "virtualrate"
        if st.button("Exceptional Calculation Methods"):
            st.session_state.script_choice = "methods"
        if st.button("Renewable Energy Production"):
            st.session_state.script_choice = "energyproduction"
        if st.button("Total Energy Usage"):
            st.session_state.script_choice = "energyusage"
        if st.button("Unment Loads"):
            st.session_state.script_choice = "unmetloads"

    if st.session_state.script_choice == "about":
        st.markdown("""
        <h4 style="color:red;">🌐 Welcome to MEP Calculator</h4>
        The MEP Calculator is a tool to help working on energy-efficient building projects, such as LEED-certified projects, update and analyze MEP performance values.
        - <b style="color:red;">Baseline Energy End Use:</b> Upload and process four SIM files representing different rotations.
        """, unsafe_allow_html=True)
       
    elif st.session_state.script_choice == "eds":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <h4 style="color:red;">🌐 Overview</h4>
            Environmental Design Solutions [EDS] is a sustainability advisory firm focusing on the built environment. Since its inception in 2002,
            EDS has worked on over 800 green building and energy efficiency projects worldwide. The diverse milieu of its team of experts converges on
            climate change mitigation policies, energy efficient building design, building code development, energy efficiency policy development, energy
            simulation and green building certification.<br>
    
            EDS has extensive experience in providing sustainable solutions at both, the macro level of policy advisory and planning, as well as a micro
            level of developing standards and labeling for products and appliances. The scope of EDS projects range from international and national level
            policy and code formulation to building-level integration of energy-efficiency parameters. EDS team has worked on developing the Energy Conservation
            Building Code [ECBC] in India and supporting several other international building energy code development, training, impact assessment, and 
            implementation. EDS has the experience of data collection & analysis, benchmarking, energy savings analysis, GHG impact assessment, and developing
            large scale implementation programs.<br>
    
            EDS’ work supports the global endeavour towards a sustainable environment primarily through the following broad categories:
            - Sustainable Solutions for the Built Environment
            - Strategy Consulting for Policy & Codes, and Research
            - Outreach, Communication, Documentation, and Training
    
            """, unsafe_allow_html=True)
            st.link_button("Know More", "https://edsglobal.com", type="primary")
        with col2:
            st.image("https://images.jdmagicbox.com/comp/delhi/k8/011pxx11.xx11.180809193209.h6k8/catalogue/environmental-design-solutions-vasant-vihar-delhi-environmental-management-consultants-leuub0bjnn.jpg", width=590)

    elif st.session_state.script_choice == "baselineenduse":
        st.markdown("""
        <h4 style="color:red;">📄 Baseline Energy End Use</h4>
        <b>Purpose:</b> a tool to help working on energy-efficient building projects, such as LEED-certified projects, update and analyze MEP performance values.<br>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader("Choose 4 Baseline SIM files", type=["sim"], accept_multiple_files=True)
        csv_file = r'tables/MEP Calculator.csv'
        df = pd.read_csv(csv_file)
        if st.button("Process Files"):
            if len(uploaded_file) != 4:
                st.warning("Please upload exactly 4 SIM files.")
            else:
                ps_e.get_END_USE(df, uploaded_file)

    elif st.session_state.script_choice == "proposedenduse":
        st.markdown("""
        <h4 style="color:red;">📄 Proposed Energy End Use</h4>
        <b>Purpose:</b> a tool to help working on energy-efficient building projects, such as LEED-certified projects, update and analyze MEP performance values.<br>
        <b>Note:</b> Upload exactly 4 Baseline and 1 Proposed SIM files.
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader("Upload a Proposed and 4 SIM files", type=["sim"], accept_multiple_files=True)
        csv_file = r'tables/MEP Calculator.csv'
        df = pd.read_csv(csv_file)
        if st.button("Process Files"):
            if len(uploaded_file) != 5:
                st.warning("Please upload exactly 4 Baseline and 1 Proposed SIM files.")
            else:
                ps_e.get_END_USE_Proposed(df, uploaded_file)

    elif st.session_state.script_choice == "SIM Parser":
        st.markdown("""
        <h4 style="color:red;">📄 SIM Parser</h4>
        <b>Purpose:</b> The SIM Parser is used to process SIM files generated by eQuest simulations. SIM files contain detailed results of energy simulations, including energy consumption, system performance, and cost estimates.<br>
        """, unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload a SIM file", type="sim", accept_multiple_files=False)
        
        if uploaded_file is not None:
            if st.button("Run SIM Parser"):
                sim_parserv01.main(uploaded_file)
                
    elif st.session_state.script_choice == "SIM to PDF":
        st.markdown("""
        <h4 style="color:red;">📝 SIM to PDF Converter</h4>
        <b>Purpose:</b> This tool converts SIM files into PDF format, making it easier to share and document simulation results.
        """, unsafe_allow_html=True)
        
        st.markdown("""Enter Reports in following format (comma-seperated and case-sensitive). And, It can accept multiple sim files.""", unsafe_allow_html=True)

        uploaded_files = st.text_input("Enter Folder Path:")
        reports_input = st.multiselect(
            "Select Reports",
            ["LV-B", "LV-D", "LV-M", "LV-A", "LV-C", "LV-E", "LV-F", "LV-G", "LV-H", "LV-I", "LV-J", 
             "LS-A", "LS-B", "LS-D", "LS-L", "LV-N", "LS-C", "LS-E", "LS-F", "LS-K", "PV-A", "BEPS", 
             "BEPU", "SV-A", "PV-A", "PS-E", "PS-F", "SS-A", "SS-B", "SS-C", "SS-D", "SS-E", "SS-M"],
            ["LV-B"]
        )

        if uploaded_files and reports_input:
            if st.button("Convert to PDF"):
                # Clean up each report name
                reports = [r.strip() for r in reports_input]
                sim_print.main(reports, uploaded_files)
                st.success("OUTPUT: Check your working directory for the generated PDF files.")

    elif st.session_state.script_choice == "baselineAutomation":
        st.markdown("""
        <h4 style="color:red;">🤖 Baseline Automation</h4>
        """, unsafe_allow_html=True)
        st.markdown("""
        <b>Purpose:</b> The Baseline Automation tool assists in modifying INP files based on user-defined criteria to create baseline models for comparison.
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            uploaded_inp_file = st.file_uploader("Upload an INP file", type="inp", accept_multiple_files=False)
        with col2:
            uploaded_sim_file = st.file_uploader("Upload a SIM file", type="sim", accept_multiple_files=False)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            input_climate = st.selectbox("Climate Zone", options=[1, 2, 3, 4, 5, 6, 7, 8])
        with col2:
            input_building_type = st.selectbox("Building Type", options=[0, 1], format_func=lambda x: "Residential" if x == 0 else "Non-Residential")
        with col3:
            input_area = st.number_input("Enter Area (Sqft)", min_value=0.0, step=0.1)
        with col4:
            number_floor = st.number_input("Number of Floors", min_value=1, step=1)
        with col5:
            heat_type = st.selectbox("Heating Type", options=[0, 1], format_func=lambda x: "Hybrid/Fossil" if x == 0 else "Electric")

        if uploaded_inp_file and uploaded_sim_file:
            if st.button("Run Baseline Automation"):
                baselineAuto.getInp(
                    uploaded_inp_file,
                    uploaded_sim_file,
                    input_climate,
                    input_building_type,
                    input_area,
                    number_floor,
                    heat_type)
                
if __name__ == "__main__":
    main()

st.markdown('<hr style="border:1px solid black">', unsafe_allow_html=True)
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
    .social-media {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .social-media a {
        margin: 0 10px;
        text-decoration: none;
        color: blue;
    }
    .social-media i {
        font-size: 24px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <div class="social-media" style="margin-top: 10px;">
        <p>@2024. All Rights Reserved</p>
        <a href="https://twitter.com/edsglobal?lang=en" target="_blank"><i class="fab fa-twitter"></i></a>
        <a href="https://www.facebook.com/Environmental.Design.Solutions/" target="_blank"><i class="fab fa-facebook"></i></a>
        <a href="https://www.instagram.com/eds_global/?hl=en" target="_blank"><i class="fab fa-instagram"></i></a>
        <a href="https://www.linkedin.com/company/environmental-design-solutions/" target="_blank"><i class="fab fa-linkedin"></i></a>
    </div>
    """,
    unsafe_allow_html=True
)