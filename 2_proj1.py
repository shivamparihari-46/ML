import streamlit as st
import pandas as pd
import joblib

model=joblib.load("naive_bayes1.pkl")
standard=joblib.load("standard1.pkl")
columns=joblib.load("columns1.pkl")

st.title("Dil wala jhanjhat predictor❤️")
st.markdown("Details bharo :")
age=st.slider("Age",18,100,40)
sex=st.selectbox("SEX",['M','F'])
chest_pain=st.selectbox('chest pain type',['ATA','NAP','TA','ASY'])
resting_bp=st.number_input("resting blood pressure(mm Hg)",80,200,120)
cholesterol=st.number_input("cholestrolpressure(mg/dL)",80,200,120)
fasting_bs=st.selectbox("fasting blood sugar>120mg/dL",[0,1])
resting_ecg=st.selectbox("resting ECG",['normal','ST','LVH'])
max_HR= st.slider('Max heart rate',60,220,120)
exercise_angina=st.selectbox("exercise-induced anginia",['y','n'])
oldpeak=st.slider("oldpeak(ST depression)",0.0,6.0,1.0)
st_slope=st.selectbox("ST slope",['Up','Flat','Down'])

if st.button("Predict"):
        # Create a raw input dictionary
    sex_val = 1 if sex == 'M' else 0
    chest_dict = {'ATA': 0, 'NAP': 1, 'TA': 2, 'ASY': 3}
    resting_ecg_dict = {'normal': 1, 'ST': 2, 'LVH': 0}
    exercise_angina_val = 1 if exercise_angina == 'y' else 0
    st_slope_dict = {'Up': 2, 'Flat': 1, 'Down': 0}

    raw_input = {
        'Age': age,
        'Sex': sex_val,
        'ChestPainType': chest_dict[chest_pain],
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'RestingECG': resting_ecg_dict[resting_ecg],
        'MaxHR': max_HR,
        'ExerciseAngina': exercise_angina_val,
        'Oldpeak': oldpeak,
        'ST_Slope': st_slope_dict[st_slope]
    }

    input_df=pd.DataFrame([raw_input])
    
     # Fill in missing columns with 0s
    for col in columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[columns]

    # Scale the input
    scaled_input = standard.transform(input_df)

    # Make prediction
    prediction = model.predict(scaled_input)[0]

    # Show result
    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")