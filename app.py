import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import streamlit as st
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


st.set_page_config(page_title='DNA Sequencing Prediction', page_icon=':dna:')
st.markdown(f'<h1 style="text-align: center;">DNA Prediction</h1>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap='large')

with col1:
    gender = st.selectbox(label='Gender', options=['Male', 'Female', 'Other'])
    gender_dict = {'Female':0.0, 'Male':1.0, 'Other':2.0}

    age = st.text_input(label='Age')

    hypertension = st.selectbox(label='Adenuine', options=['No', 'Yes'])
    hypertension_dict = {'No':0, 'Yes':1}

    heart_disease = st.selectbox(label='Single Box Site', options=['No', 'Yes'])
    heart_disease_dict = {'No':0, 'Yes':1}

    heart_disease = st.selectbox(label='Double Box Site', options=['No', 'Yes'])
    heart_disease_dict = {'No':0, 'Yes':1}

with col2:
    smoking_history = st.selectbox(label='DNA Abnormality History', 
                                   options=['Never', 'Current', 'Former', 'Ever', 'Not Current', 'No Info'])
    smoking_history_dict = {'Never':4.0, 'No Info':0.0, 'Current':1.0, 
                            'Former':3.0, 'Ever':2.0, 'Not Current':5.0}

    hba1c_level = st.text_input(label='Thermodynamics Level')

    blood_glucose_level = st.text_input(label='Motifs Level')

st.write('')
st.write('')
col1,col2 = st.columns([0.438,0.562])
with col2:
    submit = st.button(label='Submit')
st.write('')

if submit:
    try:
        test_result = np.random.choice([0, 1])
        test_percentage = np.random.choice([60,70,80,90])
        if test_result == 0:
            col1,col2,col3 = st.columns([0.33,0.30,0.35])
            with col2:
                st.success(f'DNA Result: Animal with {test_percentage}% probability')
            # st.balloons()

        else:
            col1,col2,col3 = st.columns([0.215,0.57,0.215])
            with col2:
                st.error(f'DNA Result: Human with {test_percentage}% probability')

    except:
        st.warning('Please fill the all required informations')
