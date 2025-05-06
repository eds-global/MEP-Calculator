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
from src import ps_e, bepu

st.set_page_config(
    page_title="MEP Calculator",
    page_icon="♻️",
    layout='wide'
)

button_style = """
    <style>
        .stButton>button {
            box-shadow: 1px 1px 1px rgba(0, 0, 0, 0.8);
        }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)
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
st.markdown(heading_style, unsafe_allow_html=True)

def main(): 
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
        
    logo_image_path = "images/energy.jpeg"
    _, col2, col3 = st.columns([1, 1, 0.5])
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

    st.markdown("""
    <h4 style="color:red;">♻️ MEP Calculator</h4>
    The MEP Calculator is a tool to help working on energy-efficient building projects, such as LEED-certified projects, update and analyze MEP performance values.
    Upload and process four SIM files representing different rotations.
    """, unsafe_allow_html=True)

    st.markdown("""
    <b>Purpose:</b> a tool to help working on energy-efficient building projects, such as LEED-certified projects, update and analyze MEP performance values.<br>
    <b>Note:</b> Upload exactly 4 Baseline and 1 Proposed SIM files.
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        uploaded_0_degree = st.file_uploader("Upload 0° SIM File", type=["sim"], accept_multiple_files=False)
    with col2:
        uploaded_90_degree = st.file_uploader("Upload 90° SIM File", type=["sim"], accept_multiple_files=False)
    with col3:
        uploaded_180_degree = st.file_uploader("Upload 180° SIM File", type=["sim"], accept_multiple_files=False)
    with col4:
        uploaded_270_degree = st.file_uploader("Upload 270° SIM File", type=["sim"], accept_multiple_files=False)
    uploaded_proposed_file = st.file_uploader("Upload a Proposed SIM file", type=["sim"], accept_multiple_files=False)

    csv_file = r'tables/MEP Calculator.csv'
    df = pd.read_csv(csv_file)
    if st.button("Process Files"):
        ps_e.get_END_USE_Proposed(df, uploaded_0_degree, uploaded_90_degree, uploaded_180_degree, uploaded_270_degree, uploaded_proposed_file)
                
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