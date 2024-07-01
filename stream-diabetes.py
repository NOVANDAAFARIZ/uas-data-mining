import pickle
import streamlit as st

#untuk load model
model = pickle.load(open('diabetes_model.sav', 'rb'))

#website

#judul
st.title('Prediksi Penyakit Diabetes')

#GENDER	AGE	SMOKING	YELLOW_FINGERS	ANXIETY	PEER_PRESSURE	CHRONIC 
#DISEASE	FATIGUE 	ALLERGY 	WHEEZING	
# ALCOHOL CONSUMING	COUGHING	SHORTNESS OF BREATH	SWALLOWING DIFFICULTY	CHEST PAIN	LUNG_CANCER

#membagi kolom
Pregnancies = st.text_input('input nilai Kehamilan')

Glucose = st.text_input('input nilai Glukosa')

BloodPressure = st.text_input('input nilai Tekanan Darah')

SkinThickness = st.text_input('input nilai Ketebalan Kulit')

Insulin = st.text_input('input nilai Insulin')

BMI = st.text_input('input nilai BMI')

DiabetesPredigreeFunction = st.text_input ('input nilai Diabetes predigreeFunction')

Age = st.text_input ('input nilai Umur')

#code untuk prediksi 
diab_diagnosis = ''

#membuat tombol untuk prediksi 
if st.button('Test prediksi Diabetes'):
    diab_predict = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPredigreeFunction, Age]])

    if(diab_predict[0] == 1):
        diab_diagnosis = 'Pasien terkena Diabetes'
        st.error(diab_diagnosis)
    else :
        diab_diagnosis = 'Pasien tidak terkena Diabetes'
        st.success(diab_diagnosis)


        # Footer
st.markdown("---")
footer = """
    <style>
    .footer {
        left: 0;
        bottom: 0;
        width: 100%;
        color: White;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        © Novanda Afariz Yudi Batara 4152 | 2024
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)


    


