import os
import pickle
import streamlit as st  # type: ignore # Web app framework
from streamlit_option_menu import option_menu  # type: ignore


st.set_page_config(page_title='Disease Prediction System',
                   layout='wide', page_icon="🩺")


diabetes_model = pickle.load(open(r"MODELS/diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open(r"MODELS/heart_model.sav", 'rb'))
parkinsons_model = pickle.load(open(r"MODELS/parkinsons_model.sav", 'rb'))
pcod_model = pickle.load(open(r"MODELS/pcod_model.sav", 'rb'))

with st.sidebar:
    selected = option_menu("Disease Prediction System",
                           ["Diabetes Prediction", "Heart Disease Prediction",
                               "Parkinson's Prediction", "PCOD Prediction"],
                           menu_icon="hospital-fill", icons=["activity", "heart", "person", "gender-female"], default_index=0)


num_pregnancies, Glucose_level, blood_pressure, skin_thickness, insulin_con, BMI, DiabetesPedigreeFunction, patient_age = None, None, None, None, None, None, None, None
patient_age, gender, chest_pain, resting_bp, Cholesterol, FastingBloodSugar, RestECG, MaxHeartRate, exercise_angina, StDepression, st_slope, vessels, Thalassemia = None, None, None, None, None, None, None, None, None, None, None, None, None
mvdp_fo_hz, mvdp_fhi_hz, mvdp_flo_hz, mdvp_jitter_pct, mdvp_jitter_abs, mdvp_rap, mdvp_ppq, jitter_ddp, mdvp_shimmer, mdvp_shimmer_db, shimmer_apq3, shimmer_apq5, mdvp_apq, shimmer_dda, nhr, hnr, rpde, dfa, spread_1, spread_2, d2, ppe = None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None
Age, BMI, WaistHipRatio, FSH, LH, Testosterone, MenstrualCycleLength, InsulinLevel = None, None, None, None, None, None, None, None


if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using Machine Learning')
    col1, col2, col3 = st.columns(3)

    with col1:
        num_pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose_level = st.text_input('Glucose Level')
    with col3:
        blood_pressure = st.text_input('Blood Pressure value')
    with col1:
        skin_thickness = st.text_input('Skin Thickness')
    with col2:
        insulin_con = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input(
            'Diabetes Pedigree Function value')
    with col2:
        patient_age = st.text_input('Age of the person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [num_pregnancies, Glucose_level, blood_pressure,
                      skin_thickness, insulin_con, BMI, DiabetesPedigreeFunction, patient_age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'
    st.success(diab_diagnosis)


elif selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using Machine Learning')
    col1, col2, col3 = st.columns(3)

    with col1:
        patient_age = st.text_input('Age of the person')
    with col2:
        gender = st.text_input('Sex of the person (0 - Female/1 - Male)')
    with col3:
        chest_pain = st.text_input('Chest pain Type')
    with col1:
        resting_bp = st.text_input('Resting blood pressure')
    with col2:
        Cholesterol = st.text_input('Cholesterol')
    with col3:
        FastingBloodSugar = st.text_input('Fasting blood sugar')
    with col1:
        RestECG = st.text_input('Resting ECG')
    with col2:
        MaxHeartRate = st.text_input('Maximum Heart rate')
    with col3:
        exercise_angina = st.text_input(
            'Exercise Induced Angina of person')
    with col1:
        StDepression = st.text_input('ST Depression of person')
    with col2:
        st_slope = st.text_input('Slope of ST segment of person')
    with col3:
        vessels = st.text_input('Number of major vessels')
    with col1:
        Thalassemia = st.text_input('Thalassemia of person')

    heart_diagnosis = ''
    if st.button('Heart Test Result'):
        user_input = [patient_age, gender, chest_pain, resting_bp, Cholesterol, FastingBloodSugar,
                      RestECG, MaxHeartRate, exercise_angina, StDepression, st_slope, vessels, Thalassemia]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person has heart disease.'
        else:
            heart_diagnosis = 'The person does not have heart disease.'
        st.success(heart_diagnosis)

# Parkinson's Prediction Page
elif selected == "Parkinson's Prediction":
    st.title('Parkinson Disease Prediction using Machine Learning')
    col1, col2, col3 = st.columns(3)
    with col1:
        mvdp_fo_hz = st.text_input('MDVP:Fo(HZ)')
    with col2:
        mvdp_fhi_hz = st.text_input('MDVP:Fhi(HZ)')
    with col3:
        mvdp_flo_hz = st.text_input('MDVP:Flo(HZ)')
    with col1:
        mdvp_jitter_pct = st.text_input('MDVP:Jitter(%)')
    with col2:
        mdvp_jitter_abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        mdvp_rap = st.text_input('MDVP:RAP')
    with col1:
        mdvp_ppq = st.text_input('MDVP:PPQ')
    with col2:
        jitter_ddp = st.text_input('Jitter:DDP')
    with col3:
        mdvp_shimmer = st.text_input('MDVP:Shimmer')
    with col1:
        mdvp_shimmer_db = st.text_input('MDVP:Shimmer(db)')
    with col2:
        shimmer_apq3 = st.text_input('Shimmer:APQ3')
    with col3:
        shimmer_apq5 = st.text_input('Shimmer:APQ5')
    with col1:
        mdvp_apq = st.text_input('MDVP:APQ')
    with col2:
        shimmer_dda = st.text_input('Shimmer: DDA')
    with col3:
        nhr = st.text_input('NHR')
    with col1:
        hnr = st.text_input('HNR')
    with col2:
        rpde = st.text_input('RPDE')
    with col3:
        dfa = st.text_input('DFA')
    with col1:
        spread_1 = st.text_input('Spread1')
    with col2:
        spread_2 = st.text_input('Spread2')
    with col3:
        d2 = st.text_input('D2')
    with col1:
        ppe = st.text_input('PPE')

    parkinson_diagnosis = ''
    if st.button('Parkinson Test Result'):
        user_input = [mvdp_fo_hz, mvdp_fhi_hz, mvdp_flo_hz, mdvp_jitter_pct, mdvp_jitter_abs, mdvp_rap, mdvp_ppq, jitter_ddp, mdvp_shimmer,
                      mdvp_shimmer_db, shimmer_apq3, shimmer_apq5, mdvp_apq, shimmer_dda, nhr, hnr, rpde, dfa, spread_1, spread_2, d2, ppe]
        user_input = [float(x) for x in user_input]
        parkinson_prediction = parkinsons_model.predict([user_input])
        if parkinson_prediction[0] == 1:
            parkinson_diagnosis = 'The person is battling Parkinson’s disease.'
        else:
            parkinson_diagnosis = 'The person is free from Parkinson’s disease.'
        st.success(parkinson_diagnosis)


# PCOD Prediction Page
elif selected == "PCOD Prediction":
    st.title('PCOD Disease Prediction using Machine Learning')
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input('Patient age')
    with col2:
        BMI = st.text_input('Patient BMI')
    with col3:
        WaistHipRatio = st.text_input('Waist Hip Ratio')
    with col1:
        FSH = st.text_input('FSH')
    with col2:
        LH = st.text_input('LH')
    with col3:
        Testosterone = st.text_input('Testosterone')
    with col1:
        MenstrualCycleLength = st.text_input('Menstrual Cycle Length')
    with col2:
        InsulinLevel = st.text_input('Insulin Level')

        pcod_diagnosis = ''
    if st.button('pcod Test Result'):
        user_input = [Age, BMI, WaistHipRatio, FSH, LH,
                      Testosterone, MenstrualCycleLength, InsulinLevel]
        user_input = [float(x) for x in user_input]
        pcod_prediction = pcods_model.predict([user_input])
        if pcod_prediction[0] == 1:
            pcod_diagnosis = 'The person is battling pcod’s disease.'
        else:
            pcod_diagnosis = 'The person is free from pcod’s disease.'
        st.success(pcod_diagnosis)
