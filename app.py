import streamlit as st
import pandas as pd
from data_preprocessing import data_preprocessing, encoder_Application_mode, encoder_Course, encoder_Daytime_evening_attendance, encoder_Debtor, encoder_Displaced, encoder_Educational_special_needs, encoder_Fathers_occupation, encoder_Fathers_qualification, encoder_Gender, encoder_International, encoder_Marital_status, encoder_Mothers_occupation, encoder_Mothers_qualification, encoder_Nacionality, encoder_Previous_qualification, encoder_Scholarship_holder, encoder_Tuition_fees_up_to_date 
from prediction import prediction

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=130)
with col2:
    st.header('Student Performance App (Prototype)')

data = pd.DataFrame()

col1, col2, col3 = st.columns(3)
 
with col1:
    inputs['Application_mode'] = st.selectbox(label='Application_mode', options=encoder_Application_mode.classes_, index=0, key='1')
 
with col2:
    inputs['Course'] = st.selectbox(label='Course', options=encoder_Course.classes_, index=0, key='2')
 
with col3:
    inputs['Daytime_evening_attendance'] = st.selectbox(label='Daytime_evening_attendance', options=encoder_Daytime_evening_attendance.classes_, index=0, key='3')

col1, col2, col3 = st.columns(3)
 
with col1:
    inputs['Debtor'] = st.selectbox(label='Debtor', options=encoder_Debtor.classes_, index=0, key='4')
 
with col2:
    inputs['Displaced'] = st.selectbox(label='Displaced', options=encoder_Displaced.classes_, index=0, key='5')

with col3:
    inputs['Educational_special_needs'] = st.selectbox(label='Educational_special_needs', options=encoder_Educational_special_needs.classes_, index=0, key='6')

col1, col2, col3 = st.columns(3)
 
with col1:
    inputs['Fathers_occupation'] = st.selectbox(label='Fathers_occupation', options=encoder_Fathers_occupation.classes_, index=0, key='7')
 
with col2:
    inputs['Fathers_qualification'] = st.selectbox(label='Fathers_qualification', options=encoder_Fathers_qualification.classes_, index=0, key='8')

with col3:
    inputs['Gender'] = st.selectbox(label='Gender', options=encoder_Gender.classes_, index=0, key='9')

col1, col2, col3 = st.columns(3)
 
with col1:
    inputs['International'] = st.selectbox(label='International', options=encoder_International.classes_, index=0, key='10')
 
with col2:
    inputs['Marital_status'] = st.selectbox(label='Marital_status', options=encoder_Marital_status.classes_, index=0, key='11')
 
with col3:
    inputs['Mothers_occupation'] = st.selectbox(label='Mothers_occupation', options=encoder_Mothers_occupation.classes_, index=0, key='12')

col1, col2, col3 = st.columns(3)
 
with col1:
    inputs['Mothers_qualification'] = st.selectbox(label='Mothers_qualification', options=encoder_Mothers_qualification.classes_, index=0, key='13')
 
with col2:
    inputs['Nacionality'] = st.selectbox(label='Nacionality', options=encoder_Nacionality.classes_, index=0, key='14')
 
with col3:
    inputs['Previous_qualification'] = st.selectbox(label='Previous_qualification', options=encoder_Previous_qualification.classes_, index=0, key='15')

col1, col2= st.columns(2)
 
with col1:
    inputs['Scholarship_holder'] = st.selectbox(label='Scholarship_holder', options=encoder_Scholarship_holder.classes_, index=0, key='16')
 
with col2:
    inputs['Tuition_fees_up_to_date'] = st.selectbox(label='Tuition_fees_up_to_date', options=encoder_Tuition_fees_up_to_date.classes_, index=0, key='17')

# CC

col1, col2, col3, col4 = st.columns(4)
 
with col1:
    inputs['Admission_grade'] = int(st.number_input(label='Admission_grade', value=0, key='18'))   
 
with col2:
    inputs['Age_at_enrollment'] = int(st.number_input(label='Age_at_enrollment', value=0, key='19')) 
 
with col3:
    inputs['Application_order'] = int(st.number_input(label='Application_order', value=0, key='20')) 
 
with col4:
    inputs['Curricular_units_1st_sem_without_evaluations'] = int(st.number_input(label='Curricular_units_1st_sem_without_evaluations', value=0, key='21')) 

col1, col2, col3, col4 = st.columns(4)
 
with col1:
    inputs['Curricular_units_2nd_sem_without_evaluations'] = int(st.number_input(label='Curricular_units_2nd_sem_without_evaluations', value=0, key='22')) 
   
with col2:
    inputs['GDP'] = int(st.number_input(label='GDP', value=0, key='23')) 
 
with col3:
    inputs['Inflation_rate'] = int(st.number_input(label='Inflation_rate', value=0, key='24')) 
 
with col4:
    inputs['Previous_qualification_grade'] = int(st.number_input(label='Previous_qualification_grade', value=0, key='25')) 

col1, col2, col3, col4 = st.columns(4)
 
with col1:
    inputs['Unemployment_rate'] = int(st.number_input(label='Unemployment_rate', value=0, key='26')) 
 
with col2:
    inputs['Curricular_units_1st_sem_approved'] = int(st.number_input(label='Curricular_units_1st_sem_approved', value=0, key='27'))
  
with col3:
    inputs['Curricular_units_1st_sem_credited'] = int(st.number_input(label='Curricular_units_1st_sem_credited', value=0, key='28'))
 
with col4:
    inputs['Curricular_units_1st_sem_enrolled'] = int(st.number_input(label='Curricular_units_1st_sem_enrolled', value=0, key='29'))

col1, col2, col3, col4 = st.columns(4)
 
with col1:
    inputs['Curricular_units_1st_sem_evaluations'] = int(st.number_input(label='Curricular_units_1st_sem_evaluations', value=0, key='30'))

with col2:
    inputs['Curricular_units_1st_sem_grade'] = int(st.number_input(label='Curricular_units_1st_sem_grade', value=0, key='31'))
 
with col3:
    inputs['Curricular_units_2nd_sem_approved'] = int(st.number_input(label='Curricular_units_2nd_sem_approved', value=0, key='32'))

with col4:
    inputs['Curricular_units_2nd_sem_credited'] = int(st.number_input(label='Curricular_units_2nd_sem_credited', value=0, key='33'))

col1, col2, col3 = st.columns(3)
 
with col1:
    inputs['Curricular_units_2nd_sem_enrolled'] = int(st.number_input(label='Curricular_units_2nd_sem_enrolled', value=0, key='34'))

with col2:
    inputs['Curricular_units_2nd_sem_evaluations'] = int(st.number_input(label='Curricular_units_2nd_sem_evaluations', value=0, key='35'))

with col3:
    inputs['Curricular_units_2nd_sem_grade'] = int(st.number_input(label='Curricular_units_2nd_sem_grade', value=0, key='36'))


raw_data_df_display = pd.DataFrame([inputs]) # Buat DataFrame dari dictionary untuk ditampilkan
with st.expander("View the Raw Data"):
    st.dataframe(data=raw_data_df_display, width=800, height=10) # Tampilkan DataFrame ini


# Di dalam blok if st.button('Predict'):
if st.button('Predict'):
    # Buat DataFrame 'data' yang akan dikirim ke preprocessing
    data_for_preprocessing = pd.DataFrame([inputs]) # Membuat DataFrame dengan 1 baris dari dictionary inputs

    # 'data_for_preprocessing' sekarang adalah DataFrame dengan 1 baris,
    # di mana setiap sel berisi nilai tunggal (string dari selectbox, angka dari number_input).
    # Ini sesuai dengan ekspektasi data_preprocessing.py yang dimodifikasi
    # (yang menggunakan .iloc[0] untuk mengambil nilai dari Series).

    new_data = data_preprocessing(data_input=data_for_preprocessing) # Ganti nama argumen jika perlu

    # --- MULAI BLOK DEBUG ---
    # ... (kode debug Anda sudah baik) ...
    # --- AKHIR BLOK DEBUG ---

    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)

    st.write("Status: {}".format(prediction(new_data)))
