# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 13:40:25 2024

@author: parij
"""

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
diabetes_model = pickle.load(open(os.path.join(working_dir, 'diabetes_model.sav'), 'rb'))
heart_disease_model = pickle.load(open(os.path.join(working_dir, 'heart_disease_model.sav'), 'rb'))
breast_cancer_model = pickle.load(open(os.path.join(working_dir, 'breast_cancer_model.sav'), 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Breast Cancer Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

def validate_input(input_list):
    try:
        return [float(x) for x in input_list]
    except ValueError:
        st.error("Please enter valid numeric values")
        return None

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        user_input = validate_input(user_input)
        
        if user_input is not None:
            diab_prediction = diabetes_model.predict([user_input])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
            st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = validate_input(user_input)
        
        if user_input is not None:
            heart_prediction = heart_disease_model.predict([user_input])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
            st.success(heart_diagnosis)

# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':
    st.title("Breast Cancer Prediction using ML")
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        mr = st.text_input('Mean Radius')
    with col2:
        mt = st.text_input('Mean Texture')
    with col3:
        mp = st.text_input('Mean Perimeter')
    with col4:
        ma = st.text_input('Mean Area')
    with col5:
        ms = st.text_input('Mean Smoothness')
    with col6:
        mc = st.text_input('Mean Compactness')
    with col1:
        mcc = st.text_input('Mean Concavity')
    with col2:
        mcp = st.text_input('Mean Concave Points')
    with col3:
        mss = st.text_input('Mean Symmetry')
    with col4:
        mfd = st.text_input('Mean Fractional Dimension')
    with col5:
        re = st.text_input('Radius Error')
    with col6:
        te = st.text_input('Texture Error')
    with col1:
        pe = st.text_input('Perimeter Error')
    with col2:
        ae = st.text_input('Area Error')
    with col3:
        se = st.text_input('Smoothness error')
    with col4:
        ce = st.text_input('Compactness Error')
    with col5:
        cce = st.text_input('Concavity Error')
    with col6:
        cpe = st.text_input('Concave Points Error')
    with col1:
        sse = st.text_input('Symmetry Error')
    with col2:
        fde = st.text_input('Fractional Dimension Error')
    with col3:
        wr = st.text_input('Worst Radius')
    with col4:
        wt = st.text_input('Worst Texture')
    with col5:
        wp = st.text_input('Worst Perimeter')
    with col6:
        wa = st.text_input('Worst Area')
    with col1:
        ws = st.text_input('Worst Smoothness')
    with col2:
        wc = st.text_input('Worst Compactness')
    with col3:
        wcc = st.text_input('Worst Concavity')
    with col4:
        wcp = st.text_input('Worst Concave Points')
    with col5:
        wss = st.text_input('Worst Symmetry')
    with col6:
        wfd = st.text_input('Worst Fractional Dimension')

    breast_cancer_diagnosis = ''

    if st.button("Breast Cancer Test Result"):
        user_input = [mr, mt, mp, ma, ms, mc, mcc, mcp, mss, mfd, re, te, pe, 
                      ae, se, ce, cce, cpe, sse, fde, wr, wt, wp, wa, ws, wc, 
                      wcc, wcp, wss, wfd]
        user_input = validate_input(user_input)
        
        if user_input is not None:
            breast_cancer_prediction = breast_cancer_model.predict([user_input])
            if breast_cancer_prediction[0] == 1:
                breast_cancer_diagnosis = "Breast Cancer is Benign"
            else:
                breast_cancer_diagnosis = "Breast Cancer is Malignant"
            st.success(breast_cancer_diagnosis)


    
    
    