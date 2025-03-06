#!/usr/bin/env python
# coding: utf-8

# In[13]:





# In[17]:


import streamlit as st
import pickle
from streamlit_option_menu import option_menu




# change Name & menu
st.set_page_config(page_title="Disease Prediction", page_icon = "⚕️")

# Hiding stramlit add-ons
hide_st_style = """
           <style>
           #MainMenu {visibility: hidden;}
           footer {visibility: hidden;}
           header {visibility: hidden;}
           </style>
           """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Adding Background Image
# Adding Background Image
background_image_url="data:image/jpeg;base64,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"

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"]{{
background-image: url({background_image_url});
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stAppViewContainer"]::before {{
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height:100%;
background-color: rgba(255, 252, 252, 0.7);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


#load the saved models
models = {
    'Breast_Cancer': pickle.load(open('Breast_cancer_model.sav', 'rb')),
    'PCOS': pickle.load(open('PCOS_model.sav', 'rb')),
    'Thyroid': pickle.load(open('Thyroid_model.sav', 'rb')),
    'Heart_Disease': pickle.load(open('Heart_Disease_model.sav', 'rb'))
}


# create a dropdown menu for disease prediction
selected = st.selectbox(
     'Select a Disease to predict',
    ['Breast Cancer Prediction',
     'PCOS Prediction',
     'Thyroid Prediction',
     'Heart Disease Prediction']
)

def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)
    
# Breast cancer prediction page
if selected == 'Breast Cancer Prediction':
    st.title('Breast Cancer')
    st.write("Enter the following details to predict Breast cancer:")
    
    mean_radius = display_input('Average Radius', 'Enter the average radius of tumor cells', 'mean_radius', 'number')
    mean_texture = display_input('Texture of tumor', 'Enter The variation in the gray-scale intensity in the tumor image' 'mean_texture', 'number')
    mean_Perimeter = display_input('mean Perimeter', 'Enter The average perimeter of the tumor cells', 'mean_Perimeter', 'number')
    mean_area = display_input('mean Area', 'Enter The mean area covered by the tumor cells', 'mean_area', 'number')
    
    breast_cancer_diagnosis = ''
    if st.button('Breast Cancer Test Result'):
        br_prediction = models['Breast_Cancer'].predict([[float(mean_radius), float(mean_texture), float(mean_Perimeter), float(mean_area)]])
        breast_cancer_diagnosis = 'The Person has Breast Cancer' if br_prediction[0] == 1 else 'The person does not have Breast Cancer'
        st.success(breast_cancer_diagnosis)
        
# PCOS Prediction page
if selected == 'PCOS Prediction':
    st.title('PCOS')
    st.write("Enter the following details to predict PCOS")
    
    Age = display_input('Age', 'Enter the Age of the person', 'age', 'number')
    BMI = display_input('BMI value', 'Enter Body Mass Index value', 'BMI', 'number')
    Menstrual_Irregularity = display_input('Menstrual Irregularity(1 = true; 0 = false)', 'Enter Menstrual Irregularity', 'Menstrual_Irregularity', 'number')
    Testosterone_Level = display_input('Testosterone Level', 'Enter Testosterone Level', 'Testosterone_Level', 'number')
    Antral_Follicle_Count = display_input('Antral Follicle Count', 'Enter Antra Follicel Count', 'Antral_Follicle_Count','number')
    
    PCOS_diagnosis = ''
    if st.button('PCOS Test Result'):
        pcos_prediction = models['PCOS'].predict([[Age, BMI, Menstrual_Irregularity, Testosterone_Level, Antral_Follicle_Count]])
        PCOS_diagnosis = 'The Person has PCOS' if pcos_prediction[0] == 1 else 'The person does not have PCOS'
        st.success(PCOS_diagnosis)
        
# Thyroid Prediction page
if selected == 'Thyroid Prediction':
    st.title('Thyroid')
    st.write("Enter the following details to predict Thyroid")
    
    Age = display_input('Age', 'Enter the Age of the person', 'age', 'number')
    Gender = display_input('gender(1 = male; 0 = female)', 'Enter Gender of the person', 'gender', 'number')
    smoking = display_input('smoking(1 = Yes; 0 = No)', 'Enter you have smoking habit or not', 'smoking', 'number')
    Hx_smoking = display_input('History of Smoking(1 = Yes; 0 = No)', 'Enter if you has a past history of smoking', 'Hx Smoking', 'number')
    Hx_Radiothreapy = display_input('History of Radiotherapy(1 = Yes; 0 = No)', 'Enter if you have undergone Radiotherapy', 'Hx Radiothreapy','number')
    Thyroid_Function = display_input('Thyroid Function(0 = Clinical Hyperthyroidism, 1= Clinical Hypothyroidism, 2 = Euthyroid, 3 = Subclinical Hyperthyroidism)', 'Enter Thyroid function', 'Thyroid Function', 'number')
    Physical_Examination = display_input('Physical Examination(0 = Diffuse goiter, 1 = Multinodular goiter, 2 = Normal, 3 = Single nodular goiter-left, 4 = Single nodular goiter-right)', 'Enter physical examination', 'Physical Examination', 'number')
    Adenopathy = display_input('Adenopathy(1 = Yes; 0 = No)', 'Enter Presence of lymph node enlargement','Adenopathy', 'number')
    Pathology = display_input('Pathology(0 = Follicular, 1 = Hurthel cell, 2 = Micropapillary, 3 = Papillary)','Enter Type of cancer pathology found','pathalogy','number')
    Focality = display_input('Focality(0 = Multi-Focal, 1 = Uni-Focal)', 'Enter wheather it is one tumor or multi-tumor', 'Focality', 'number')
    Risk = display_input('Risk(0 = High, 1 = Intermediate, 2 = Low)', 'Enter Risk', 'Risk', 'number')
    T = display_input('T(0 = T1a, 1 = T1b, 2 = T2, 3 = T3a, 4 = T3b, 5 = T4b)', 'Enter Tumor size', 'Tumor size', 'number')
    N = display_input('N(0 = No, 1 = Yes)', 'Enter wheather cancer has spread to nearby', 'N', 'number')
    M = display_input('M(0 = M0, 1 = M1)', 'Enter Meta statis', 'Meta statis', 'number')
    Stage = display_input('Stage(0 = I, 1 = II, 2 = III, 3 = IVA, 4 = IVB)', 'Enter Stage', 'Stage', 'number')
    Response = display_input('Response(0 = Biochemical Incomplete, 1 = Excellent, 2 = Indeterminate, 3 = Structural Incomplete)', 'Enter Patient’s response to treatment', 'Response', 'number')
       

    Thyroid_diagnosis = ''
    if st.button('Thyroid Test Result'):
        Thyroid_prediction = models['Thyroid'].predict([[Age, Gender, smoking, Hx_smoking, Hx_Radiothreapy, Thyroid_Function, Physical_Examination, Adenopathy, Pathology, Focality, Risk, T, N, M, Stage, Response]])
        Thyroid_diagnosis = 'The Person has Thyroid' if Thyroid_prediction[0] == 1 else 'The person does not have Thyroid'
        st.success(Thyroid_diagnosis)
    
# Heart Disease Prediction page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease')
    st.write("Enter the following details to predict Heart Disease")
    
    Age = display_input('Age', 'Enter the Age of the person', 'age', 'number')
    Sex = display_input('Sex(1 = Male; 0 = Female)', 'Enter sex of the person', 'sex', 'number')
    Chest_pain_type = display_input('Chest pain type(1 = Typical Angina; 2 = Atypical Angina; 3 = Non-Anginal pain; 4 = Asymptomatic)', 'Enter your Chest pain type', 'Chest pain type', 'number')
    BP = display_input('BP', 'Enter your blood pressure', 'Blood Pressure', 'number')
    Cholesterol = display_input('Cholesterol', 'Enter your Cholestrol', 'Cholesterol','number')
    FBS_over_120 = display_input('FBS over 120(1 = Yes; 0 = No)', 'Enter your Fast Blood Sugar', 'Fast Blood Sugar','number')
    EKG_results = display_input('EKG results(0 = Normal; 1 = ST-T wave abnormality; 2 = Left ventricular hypertrophy)', 'Enter your Electro Cardiogram', 'Electro Cardiogram','number')
    Max_HR = display_input('Max HR', 'Enter your Maximum Heart Rate', 'Maximum Heart Rate','number')
    Exercise_angina = display_input('Exercise angina(1 = Yes;0 = No)', 'Enter if you experienced chest pain', 'Exercise angina','number')
    ST_depression = display_input('ST depression', 'Enter ST segment depression', 'ST depression','number')
    Slope_of_ST = display_input('Slope of ST(1 = Upsloping; 2 = Flat; 3 = Downsloping)', 'Enter Slope of the ST segment during exercise', 'slope of ST segment','number')
    Number_of_vessels_fluro = display_input('Number of vessels fluro', 'Enter Number of major coronary arteries detected with fluoroscopy', 'Number of major coronary arteries','number')
    Thallium = display_input('Thallium(0-3)', 'Enter Results from Thallium Stress Test', 'Thallium','number')

    Heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        Heart_prediction = models['Heart_Disease'].predict([[Age, Sex, Chest_pain_type, BP, Cholesterol, FBS_over_120, EKG_results, Max_HR, 
                            Exercise_angina, ST_depression, Slope_of_ST, Number_of_vessels_fluro, Thallium]])
        Heart_diagnosis = 'The Person has Heart Disease' if Heart_prediction[0] == 1 else 'The person does not have Heart Disease'
        st.success(Heart_diagnosis)


# In[19]:


import os
print(os.getcwd())  # This prints your current working directory
